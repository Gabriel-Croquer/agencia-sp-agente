---
name: registrar-feedback
description: Registra correcoes e criticas do editor para aprendizado continuo. Use apos receber feedback sobre um texto produzido.
argument-hint: "[correcoes e comentarios do editor]"
allowed-tools: Read, Write, Edit, Glob
---

# Skill: Registrar feedback e correcoes

## Ao receber feedback

### 1. Analise as correcoes
- Identifique o que foi corrigido
- Classifique cada correcao:
  - **ERRO GRAMATICAL** — erro de portugues
  - **ERRO DE ESTILO** — nao seguiu as regras editoriais
  - **ERRO DE ESTRUTURA** — lide enterrado, piramide invertida quebrada
  - **ERRO DE DADOS** — numero errado, conta mal feita, falta de contexto
  - **ERRO DE APURACAO** — informacao incompleta ou sem fonte
  - **MELHORIA** — nao era erro, mas pode melhorar
  - **ELOGIO** — algo que funcionou bem e deve ser mantido

### 2. Registre no log

Adicione ao final de `feedback/correcoes-log.md`:

```markdown
## [YYYY-MM-DD] — [slug da materia]

- [TIPO]: [descricao do erro] → REGRA: [o que fazer da proxima vez]
- [TIPO]: [descricao] → REGRA: [correcao]
```

### 3. Atualize padroes aprendidos

Leia `feedback/padroes-aprendidos.md`. Se a correcao revela um padrao recorrente (apareceu mais de uma vez no log), adicione ou atualize a regra correspondente.

Formato de `padroes-aprendidos.md`:

```markdown
## Erros recorrentes — EVITAR
- [regra 1 — extraida de N ocorrencias]
- [regra 2]

## Boas praticas — MANTER
- [pratica 1 — elogiada N vezes]
- [pratica 2]

## Preferencias do editor
- [preferencia 1]
- [preferencia 2]
```

### 4. Confirme ao editor

Informe:
- Quantas correcoes foram registradas
- Quais padroes foram atualizados (se algum)
- Resumo do que vai mudar nos proximos textos
