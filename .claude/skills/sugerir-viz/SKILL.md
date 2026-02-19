---
name: sugerir-viz
description: Sugere visualizacoes e infograficos a partir de dados ou briefing. Use quando precisar decidir que tipo de grafico, mapa ou infografico usar para contar uma historia com dados.
argument-hint: "[base de dados ou briefing de dados]"
allowed-tools: Read, Write, Glob, Grep
---

# Skill: Sugestao de visualizacoes e infograficos

## Ao receber dados ou briefing

### 1. Identifique o tipo de historia
- **Comparacao**: Valores entre categorias → barras, lollipop
- **Evolucao temporal**: Mudanca ao longo do tempo → linhas, areas
- **Composicao**: Partes de um todo → pizza (max 5 fatias), treemap, stacked bars
- **Distribuicao**: Como valores se espalham → histograma, box plot
- **Correlacao**: Relacao entre duas variaveis → scatter plot
- **Geografico**: Dados por regiao → mapa coropletico, mapa de bolhas
- **Ranking**: Ordenacao por valor → barras horizontais, table chart
- **Fluxo**: De onde para onde → Sankey, alluvial

### 2. Regras de ouro para visualizacao jornalistica

- **Menos e mais**: um grafico, uma mensagem
- **Titulo conta a historia**: "SP lidera ranking de vacinacao" > "Vacinacao por estado"
- **Eixo Y comeca em zero** para barras (evitar distorcao visual)
- **Maximo 7 categorias** por grafico; agrupe o resto em "Outros"
- **Cores com proposito**: destaque o dado principal, cinza para o resto
- **Acessibilidade**: nao dependa so de cor; use rotulos diretos
- **Mobile first**: o grafico precisa funcionar em tela de celular

### 3. Ferramentas sugeridas

| Ferramenta | Melhor para | Custo |
|-----------|-------------|-------|
| Datawrapper | Graficos rapidos, mapas, tabelas | Gratis (basico) |
| Flourish | Graficos interativos, storytelling | Gratis (basico) |
| Infogram | Infograficos completos, dashboards | Pago |
| RAWGraphs | Graficos nao-convencionais | Gratis |
| Canva | Infograficos estaticos simples | Freemium |

## Output

```markdown
# Sugestoes de visualizacao: [tema]
**Data:** [YYYY-MM-DD]

## Dados disponiveis
[Resumo dos dados que temos]

## Visualizacao 1 (principal)
- **Tipo:** [ex: grafico de barras horizontais]
- **O que mostra:** [descricao clara]
- **Titulo sugerido:** [titulo que conta a historia]
- **Eixos/dimensoes:** [X = ..., Y = ..., Cor = ...]
- **Ferramenta recomendada:** [Datawrapper / Flourish / etc.]
- **Por que esse tipo:** [justificativa]

## Visualizacao 2 (complementar)
...

## Visualizacao 3 (se aplicavel)
...

## Dados que faltam
[O que seria necessario para melhorar as visualizacoes]

## Briefing para designer/infografista
[Descricao em linguagem simples do que precisa ser feito]
```

Salve em `outputs/analises-dados/YYYY-MM-DD-viz-tema.md`
