---
name: checar-informacao
description: Checa veracidade de uma afirmacao, dado ou informacao. Use quando precisar verificar se algo e verdade, confirmar numeros ou validar declaracoes.
argument-hint: "[afirmacao ou dado a checar]"
context: fork
allowed-tools: Read, Write, Glob, Grep, WebSearch, WebFetch
---

# Skill: Checagem de informacao

## Metodologia

Ao receber uma afirmacao para checar:

### 1. Identifique o que precisa ser verificado
- Separe a afirmacao em claims individuais
- Classifique: fato verificavel, opiniao, ou previsao?

### 2. Busque fontes primarias
- Dados do governo: gov.br, sp.gov.br, portais de transparencia
- Estatisticas: IBGE, SEADE, DataSUS, Banco Central
- Legislacao: planalto.gov.br, al.sp.gov.br
- Documentos oficiais: Diario Oficial, atas, editais

### 3. Busque fontes secundarias
- Agencias de checagem: Aos Fatos, Lupa, Estadao Verifica
- Reportagens investigativas sobre o tema
- Artigos academicos se relevante

### 4. Cruze as informacoes
- A afirmacao bate com as fontes primarias?
- Ha contradicoes entre fontes?
- O contexto original foi preservado ou houve distorcao?

## Classificacao

Atribua um nivel de confianca:

- **CONFIRMADO** — Fontes primarias confirmam. Alta confianca
- **PARCIALMENTE VERDADEIRO** — Parte confere, parte nao ou falta contexto
- **NAO VERIFICAVEL** — Nao encontrei fontes suficientes para confirmar ou negar
- **INCORRETO** — Fontes contradizem a afirmacao
- **DESATUALIZADO** — Era verdade, mas dados mais recentes mostram outra coisa

## Output

```markdown
# Checagem: [afirmacao resumida]
**Data:** [YYYY-MM-DD]

## Afirmacao original
"[transcricao exata]"

## Veredicto: [CONFIRMADO / PARCIALMENTE VERDADEIRO / etc.]

## Evidencias
1. [Fonte primaria] — [o que diz] — [link]
2. [Fonte secundaria] — [o que diz] — [link]

## Contexto adicional
[O que falta na afirmacao original, nuances, ressalvas]

## Recomendacao para o texto
[Como usar essa informacao no texto jornalistico]
```

Salve em `outputs/checagens/YYYY-MM-DD-tema.md`
