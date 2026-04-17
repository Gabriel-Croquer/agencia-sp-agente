"""
Transcritor de lives do YouTube — Agencia SP
Captura audio de uma live do YouTube e transcreve em tempo real usando Whisper.

Uso:
    python scripts/transcrever_live.py URL_DA_LIVE [--modelo base] [--chunk 10] [--output transcricao.md]

Dependencias (instalar antes):
    pip install faster-whisper yt-dlp imageio-ffmpeg
"""

import argparse
import subprocess
import sys
import tempfile
import time
from datetime import datetime, timedelta
from pathlib import Path


def get_ffmpeg_path():
    """Tenta encontrar ffmpeg: imageio-ffmpeg > sistema."""
    try:
        import imageio_ffmpeg
        return imageio_ffmpeg.get_ffmpeg_exe()
    except ImportError:
        pass

    # Tenta ffmpeg do sistema
    try:
        subprocess.run(
            ["ffmpeg", "-version"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            check=True,
        )
        return "ffmpeg"
    except (FileNotFoundError, subprocess.CalledProcessError):
        pass

    print("ERRO: ffmpeg nao encontrado.")
    print("Instale com: pip install imageio-ffmpeg")
    sys.exit(1)


def get_stream_url(youtube_url):
    """Usa yt-dlp para extrair a URL direta do audio da live."""
    print("Extraindo URL do stream de audio (pode levar ate 60s)...")
    try:
        result = subprocess.run(
            [
                sys.executable, "-m", "yt_dlp",
                "--get-url",
                "-f", "worstaudio/bestaudio/worst",  # tenta audio isolado, senao pega combinado
                "--no-warnings",
                "--socket-timeout", "30",
                youtube_url,
            ],
            capture_output=True,
            text=True,
            check=True,
            timeout=90,
        )
        url = result.stdout.strip()
        if not url:
            print("ERRO: yt-dlp nao retornou URL. Verifique se a live esta ativa.")
            sys.exit(1)
        print("URL do stream extraida com sucesso.")
        return url
    except subprocess.CalledProcessError as e:
        print(f"ERRO ao extrair URL:\n{e.stderr}")
        sys.exit(1)
    except subprocess.TimeoutExpired:
        print("ERRO: Timeout ao conectar com o YouTube (90s).")
        print("Possiveis causas:")
        print("  - A live nao esta ativa ou a URL esta errada")
        print("  - Conexao lenta / proxy / VPN bloqueando")
        print("  - Tente rodar manualmente: python -m yt_dlp --get-url -f worstaudio URL")
        sys.exit(1)


def start_ffmpeg_segmenter(ffmpeg_path, stream_url, tmpdir, chunk_duration):
    """Inicia um unico processo ffmpeg que segmenta o audio em chunks sequenciais."""
    pattern = str(Path(tmpdir) / "chunk_%04d.wav")
    cmd = [
        ffmpeg_path,
        "-y",
        "-i", stream_url,
        "-vn",                        # sem video
        "-acodec", "pcm_s16le",       # WAV 16-bit
        "-ar", "16000",               # 16kHz
        "-ac", "1",                   # mono
        "-f", "segment",              # modo segmentacao
        "-segment_time", str(chunk_duration),
        "-loglevel", "error",
        pattern,
    ]
    proc = subprocess.Popen(cmd, stderr=subprocess.PIPE)
    return proc


def wait_for_chunk(chunk_path, timeout=60):
    """Espera um arquivo de chunk ficar pronto (ffmpeg terminou de escrever)."""
    start = time.time()
    # Espera o arquivo aparecer
    while not chunk_path.exists():
        if time.time() - start > timeout:
            return False
        time.sleep(0.3)

    # Espera o ffmpeg parar de escrever (tamanho estabiliza)
    last_size = -1
    stable_count = 0
    while stable_count < 3:
        try:
            current_size = chunk_path.stat().st_size
        except OSError:
            return False
        if current_size == last_size and current_size > 0:
            stable_count += 1
        else:
            stable_count = 0
        last_size = current_size
        time.sleep(0.3)

    return True


def format_timestamp(seconds):
    """Formata segundos em HH:MM:SS."""
    return str(timedelta(seconds=int(seconds)))


def main():
    parser = argparse.ArgumentParser(description="Transcreve live do YouTube em tempo real")
    parser.add_argument("url", help="URL da live do YouTube")
    parser.add_argument("--modelo", default="base", help="Modelo Whisper: tiny, base, small, medium, large (default: base)")
    parser.add_argument("--chunk", type=int, default=15, help="Duracao de cada chunk em segundos (default: 15)")
    parser.add_argument("--output", default=None, help="Arquivo de saida (default: transcricao-YYYY-MM-DD-HHMMSS.md)")
    parser.add_argument("--idioma", default="pt", help="Idioma do audio (default: pt)")
    args = parser.parse_args()

    # Arquivo de saida
    if args.output is None:
        timestamp = datetime.now().strftime("%Y-%m-%d-%H%M%S")
        args.output = f"outputs/transcricao-{timestamp}.md"

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    # Setup
    ffmpeg_path = get_ffmpeg_path()
    print(f"ffmpeg: {ffmpeg_path}")

    print(f"Carregando modelo Whisper '{args.modelo}' (primeira vez baixa ~150MB)...")
    from faster_whisper import WhisperModel
    model = WhisperModel(args.modelo, device="cpu", compute_type="int8")
    print("Modelo carregado.")

    stream_url = get_stream_url(args.url)

    # Header do arquivo
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(f"# Transcricao de live\n\n")
        f.write(f"- **URL**: {args.url}\n")
        f.write(f"- **Inicio**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"- **Modelo**: {args.modelo}\n")
        f.write(f"- **Chunks**: {args.chunk}s\n\n")
        f.write(f"---\n\n")

    print(f"\nTranscrevendo para: {output_path}")
    print(f"Chunks de {args.chunk}s | Modelo: {args.modelo} | Idioma: {args.idioma}")
    print("Pressione Ctrl+C para parar.\n")

    tmpdir = tempfile.mkdtemp()
    ffmpeg_proc = None

    try:
        # Inicia UM unico ffmpeg que segmenta o audio continuamente
        print("Iniciando captura de audio (processo unico)...")
        ffmpeg_proc = start_ffmpeg_segmenter(ffmpeg_path, stream_url, tmpdir, args.chunk)
        time.sleep(2)  # Espera ffmpeg iniciar

        # Verifica se ffmpeg nao morreu imediatamente
        if ffmpeg_proc.poll() is not None:
            stderr = ffmpeg_proc.stderr.read().decode() if ffmpeg_proc.stderr else ""
            print(f"ERRO: ffmpeg encerrou inesperadamente.\n{stderr}")
            sys.exit(1)

        chunk_num = 0
        elapsed = 0

        while True:
            # O chunk ATUAL esta sendo escrito pelo ffmpeg.
            # Transcrevemos o chunk ANTERIOR (que ja esta completo).
            # Entao esperamos o chunk N+1 aparecer pra saber que o chunk N esta pronto.
            current_chunk = Path(tmpdir) / f"chunk_{chunk_num:04d}.wav"
            next_chunk = Path(tmpdir) / f"chunk_{chunk_num + 1:04d}.wav"

            # Espera o proximo chunk comecar (= chunk atual terminou)
            print(f"[{format_timestamp(elapsed)}] Aguardando chunk {chunk_num + 1}...", end=" ", flush=True)

            if not wait_for_chunk(next_chunk, timeout=args.chunk + 30):
                # ffmpeg pode ter encerrado (fim do video ou erro)
                if ffmpeg_proc.poll() is not None:
                    # Processa o ultimo chunk se existir
                    if current_chunk.exists() and current_chunk.stat().st_size > 0:
                        print("Fim do stream. Transcrevendo ultimo chunk...", end=" ", flush=True)
                        segments, _ = model.transcribe(
                            str(current_chunk),
                            language=args.idioma,
                            beam_size=3,
                            vad_filter=True,
                            vad_parameters=dict(min_silence_duration_ms=500),
                        )
                        chunk_text = " ".join(s.text.strip() for s in segments)
                        if chunk_text:
                            print(f"OK ({len(chunk_text)} chars)")
                            print(f"    > {chunk_text}\n")
                            with open(output_path, "a", encoding="utf-8") as f:
                                f.write(f"**[{format_timestamp(elapsed)}]** {chunk_text}\n\n")
                    print("\nStream encerrado (fim do video ou conexao perdida).")
                    break
                print("Timeout, tentando continuar...")
                continue

            # Chunk atual esta completo, transcreve
            if current_chunk.exists() and current_chunk.stat().st_size > 0:
                print("Transcrevendo...", end=" ", flush=True)
                segments, _ = model.transcribe(
                    str(current_chunk),
                    language=args.idioma,
                    beam_size=3,
                    vad_filter=True,
                    vad_parameters=dict(min_silence_duration_ms=500),
                )
                chunk_text = " ".join(s.text.strip() for s in segments)

                if chunk_text:
                    print(f"OK ({len(chunk_text)} chars)")
                    print(f"    > {chunk_text}\n")
                    with open(output_path, "a", encoding="utf-8") as f:
                        f.write(f"**[{format_timestamp(elapsed)}]** {chunk_text}\n\n")
                else:
                    print("(silencio)")

                # Limpa chunk ja transcrito
                current_chunk.unlink(missing_ok=True)
            else:
                print("(chunk vazio, pulando)")

            chunk_num += 1
            elapsed += args.chunk

    except KeyboardInterrupt:
        print(f"\n\nTranscricao encerrada apos {format_timestamp(elapsed)}.")
        print(f"Arquivo salvo: {output_path}")

        with open(output_path, "a", encoding="utf-8") as f:
            f.write(f"\n---\n\n")
            f.write(f"*Transcricao encerrada em {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*\n")
            f.write(f"*Duracao total: ~{format_timestamp(elapsed)}*\n")

    finally:
        if ffmpeg_proc and ffmpeg_proc.poll() is None:
            ffmpeg_proc.terminate()
            try:
                ffmpeg_proc.wait(timeout=5)
            except subprocess.TimeoutExpired:
                ffmpeg_proc.kill()

        import shutil
        shutil.rmtree(tmpdir, ignore_errors=True)


if __name__ == "__main__":
    main()
