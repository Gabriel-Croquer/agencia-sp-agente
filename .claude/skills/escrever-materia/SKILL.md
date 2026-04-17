---
name: escrever-materia
description: Escreve materia jornalistica a partir de release, briefing ou tema. Use quando pedirem para redigir, escrever ou produzir um texto noticioso.
argument-hint: "[release ou tema]"
allowed-tools: Read, Write, Glob, Grep, Edit
---

# Skill: Escrever materia jornalistica

## Principio fundamental

**Cada afirmacao factual do texto precisa de fonte.** Se voce nao tem fonte para uma informacao, nao escreva. Se tem duvida, sinalize com [VERIFICAR]. Generalizacoes a partir de exemplos sao proibidas: citar 5 casos nao autoriza dizer "todos". Superlativos ("o maior do Brasil", "o primeiro") exigem fonte verificavel. Se a fonte e o proprio governo, atribua ("segundo o Governo de SP"). Afirmacao sem fonte e erro jornalistico grave.

## Antes de escrever

1. Leia `context/manual-redacao-agenciasp.pdf` se ainda nao leu nesta sessao
2. Consulte `feedback/padroes-aprendidos.md` para evitar erros recorrentes
3. Se o input for um release, extraia: fatos principais, numeros, citacoes, datas
4. Se for um tema generico, pesquise com `/apurar-web` primeiro

## Estrutura do output

Produza o texto no seguinte formato:

```markdown
# [TITULO — chamativo, com palavra-chave, ate 70 chars]

**Meta description:** [ate 155 caracteres]

**Tags sugeridas:** [3-5 tags para SEO]

---

[LIDE — 1o paragrafo. O QUE, QUEM, QUANDO, POR QUE. Maximo 3 linhas.]

[SUBLIDE — 2o paragrafo. COMO, ONDE, detalhes numericos.]

## [Intertitulo como pergunta do leitor]

[2-3 paragrafos desenvolvendo]

## [Outro intertitulo]

[2-3 paragrafos]

## [Contexto / historico se aplicavel]

[Paragrafos com links para materias anteriores]

---
*Dados incertos sinalizados com [VERIFICAR]*
```

## Ao finalizar

1. Salve o arquivo em `outputs/materias/YYYY-MM-DD-slug.md`
2. Informe ao editor (usuario) que o texto esta pronto para revisao
3. Liste os pontos que marcou como [VERIFICAR], se houver
4. Sugira possiveis desdobramentos ou materias complementares
