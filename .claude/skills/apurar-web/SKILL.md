---
name: apurar-web
description: Pesquisa e apura informacoes na web sobre um tema. Use quando precisar buscar contexto, materias anteriores, dados oficiais ou noticias relacionadas.
argument-hint: "[tema ou URL para apurar]"
context: fork
allowed-tools: Read, Write, Glob, Grep, WebSearch, WebFetch
---

# Skill: Apuracao e pesquisa web

## Estrategia de pesquisa

Ao receber um tema para apurar, execute as seguintes buscas em ordem:

### 1. Site da Agencia SP
- Busque: `site:agenciasp.sp.gov.br [tema]`
- Objetivo: saber o que ja publicamos sobre o assunto
- Registre: titulos, datas, angulos ja cobertos

### 2. Portais de noticias
- Busque em g1, Folha, Estadao, UOL
- Objetivo: ver como a midia esta cobrindo o tema
- Registre: angulos diferentes, dados adicionais, fontes citadas

### 3. Fontes oficiais do governo de SP (FONTES PRIMARIAS)
- PRIORIDADE MAXIMA: dominios `sp.gov.br` (agenciasp.sp.gov.br, semil.sp.gov.br, ppi.sp.gov.br, etc.)
- Tambem validos: `gov.br` (federal), portais de transparencia
- Objetivo: dados primarios, decretos, leis, portarias
- Registre: numeros oficiais, datas de vigencia, links diretos
- IMPORTANTE: nos SOMOS a Agencia SP. Portais de noticias (Terra, VTV News, GMC Online, etc.) NAO sao fontes — sao republicadores dos nossos releases. Sempre buscar a materia ORIGINAL no dominio sp.gov.br

### 4. Dados e estatisticas
- Busque em IBGE, SEADE, DataSUS, INEP conforme o tema
- Objetivo: dados quantitativos para embasar o texto
- Registre: numeros, series historicas, comparacoes

## Output

Produza um relatorio de apuracao:

```markdown
# Apuracao: [tema]
**Data:** [YYYY-MM-DD]

## O que ja publicamos (Agencia SP)
- [titulo] — [data] — [link]
- [titulo] — [data] — [link]

## Cobertura da midia
- [veiculo]: [angulo principal] — [link]
- [veiculo]: [angulo principal] — [link]

## Dados oficiais encontrados
- [fonte]: [dado relevante]
- [fonte]: [dado relevante]

## Sugestao de angulos para nova materia
1. [angulo 1 — por que e relevante]
2. [angulo 2 — por que e relevante]
3. [angulo 3 — por que e relevante]

## Fontes para contato (se identificadas)
- [nome, cargo, orgao]
```

Salve em `outputs/apuracoes/YYYY-MM-DD-tema.md`
