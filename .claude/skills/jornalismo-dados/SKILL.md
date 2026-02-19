---
name: jornalismo-dados
description: Analisa bases de dados e encontra historias jornalisticas. Use quando receber um CSV, Excel ou base de dados para analisar e encontrar pautas.
argument-hint: "[caminho para base de dados]"
allowed-tools: Read, Write, Glob, Grep, Bash, Edit
---

# Skill: Jornalismo de dados

## Ao receber uma base de dados

### 1. Reconhecimento (sempre primeiro)
- Leia as primeiras linhas para entender a estrutura
- Liste colunas, tipos de dados, volume de registros
- Identifique o que cada coluna representa
- Verifique qualidade: nulos, duplicatas, inconsistencias, encodings

### 2. Analise exploratoria
- Estatisticas descritivas: media, mediana, min, max, desvio padrao
- Distribuicao das variaveis principais
- Serie temporal se houver coluna de data
- Agrupamentos por categorias relevantes (regiao, tipo, orgao)

### 3. Caca as historias

Procure sistematicamente:

**Rankings**
- Top 10 e bottom 10 de cada metrica relevante
- Quem gasta mais? Quem atende mais? Quem cresce mais?

**Tendencias**
- Comparacao ano a ano, mes a mes
- Algo esta crescendo ou caindo de forma acentuada?
- Ha sazonalidade?

**Outliers e anomalias**
- Valores que destoam muito da media
- Municipios/orgaos com comportamento atipico
- Zeros suspeitos ou valores extremos

**Desigualdades**
- Disparidades regionais (capital vs interior)
- Diferencas por porte de municipio
- Concentracao (poucos responsaveis por muito)

**Impacto no cidadao**
- Quanto isso representa per capita?
- Como traduzir para a realidade do leitor?

### 4. Producao do briefing

## Output

```markdown
# Analise de dados: [nome da base]
**Data:** [YYYY-MM-DD]
**Fonte:** [origem da base]
**Periodo:** [periodo coberto pelos dados]
**Registros:** [quantidade]

## Estrutura da base
| Coluna | Tipo | Descricao | Exemplo |
|--------|------|-----------|---------|
| ... | ... | ... | ... |

## Qualidade dos dados
- Registros completos: [X%]
- Problemas encontrados: [listar]

## Top 5 historias encontradas

### 1. [Titulo da historia]
- **Dado-chave:** [numero ou comparacao]
- **Por que importa:** [relevancia para o leitor]
- **Angulo sugerido:** [como contar no texto]

### 2. [Titulo da historia]
...

## Dados de apoio
[Tabelas resumidas, agrupamentos, comparacoes que sustentam as historias]

## Sugestao de proximos passos
- [Cruzamento com outra base?]
- [Fonte para ouvir?]
- [Pedido de LAI necessario?]
```

Salve em `outputs/analises-dados/YYYY-MM-DD-nome-base.md`
