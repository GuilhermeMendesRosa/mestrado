# Roteiro de estudos para 6 dias — P2 (Atualizado com slides do professor)

Este cronograma cobre todos os blocos da P2 em 6 dias, incluindo os novos tópicos dos slides do professor (decomposição, estruturas espaciais, LOD, problemas de validação em features).

Objetivo:
- cobrir os 5 blocos de tópicos da P2
- revisar teoria com foco em explicar e comparar conceitos (a prova é mais teórica que matemática)
- deixar os dias 4-5 para os tópicos novos e o dia 6 para consolidação

Sugestão de ritmo diário:
- Bloco 1: 1h30 a 2h de leitura do material
- Bloco 2: 1h a 1h30 de resumo próprio e mapa mental
- Bloco 3: 45min a 1h de autoexplicação ou questões

Se tiver menos tempo, priorize:
1. Bloco 1 (Interoperabilidade/STEP): maior e com mais conceitos para decorar
2. Bloco 4 (Decomposição/Estruturas Espaciais): totalmente novo, provável questão de prova
3. Bloco 3 (Features + Validação): muito conteúdo nos slides do professor

---

## Dia 1: Interoperabilidade e Padrões de Troca de Dados

### Objetivo do dia

Entender como softwares CAD trocam dados, os padrões históricos e o padrão STEP como evolução.

### Estudar

Ler `material-dia-1.md` (seções 1-3):
- Estratégias de Comunicação (tradutor direto vs. arquivo neutro)
- Padrões Clássicos (ICAM, IGES, SET, VDA-FS)
- STEP (arquitetura, EXPRESS, SDAI, Application Protocols)

### Foco principal

- Tradutor direto vs. arquivo neutro (trade-off, fórmula N×(N−1) vs. 2N)
- IGES: o que é, estrutura de 5 seções (Start, Global, Directory Entry, Parameter Data, Terminate), coluna 73 com identificador S/G/D/P/T
- STEP: diferença crucial em relação ao IGES (dado de produto vs. geometria)
- Arquitetura STEP em três camadas + séries (10, 40/100, 30)
- EXPRESS com exemplo de código e SDAI: para que servem
- Tabela comparativa IGES vs. SET vs. VDA-FS vs. STEP
- Centros STEP mundiais (PDES Inc, ProSTEP, Nippon, GOSET, C-STEP, **B-STEP Brasil**)

### O que você precisa sair sabendo

- **Explicar a diferença STEP vs. IGES** (questão certa de prova)
- Descrever as 5 seções do arquivo IGES
- Descrever as três camadas da arquitetura STEP
- Explicar por que o modelo de arquivo neutro é mais escalável
- Dizer o que é e para que serve EXPRESS e SDAI
- Citar ao menos 3 Application Protocols

### Revisão ativa do dia

Responda sem consultar:
- Qual a grande diferença entre IGES e STEP?
- Quais as 5 seções de um arquivo IGES e o identificador de cada uma?
- O que é um Application Protocol? Dê dois exemplos.
- Para que serve EXPRESS? E SDAI?
- Por que N tradutores diretos não escalam bem?

### Entrega do dia

Escreva uma folha-resumo com:
- Desenho comparativo: tradutor direto vs. arquivo neutro
- Diagrama da arquitetura STEP (3 camadas + séries)
- Tabela STEP vs. IGES

---

## Dia 2: Modelos de Produto, STEP-NC + Paramétrico (parte 1)

### Objetivo do dia

Fechar o Bloco 1 (Product Models e STEP-NC) e começar o Bloco 2 com os conceitos fundamentais de modelagem paramétrica.

### Estudar

Ler `material-dia-2.md`:
- Modelos de Produto (três domínios, Integrated Product Model)
- STEP-NC e integração com manufatura
- Design Intent, famílias de peças (com Mortenson Cap. 10)
- Paramétrico vs. Variacional
- Tipos de Restrições (geométricas, funcionais, variacionais)

### Foco principal

- Três domínios do modelo de produto
- STEP-NC: o que muda em relação ao código G
- Design Intent: o que é, por que importa
- Famílias de peças e group technology (Mortenson)
- Paramétrico vs. Variacional: diferença fundamental
- Restrições geométricas, funcionais e variacionais

### O que você precisa sair sabendo

- Explicar os três domínios do product model
- Dizer por que STEP-NC é mais inteligente que código G
- Definir design intent com exemplo
- Diferenciar paramétrico de variacional com exemplo concreto
- Dar exemplo de cada tipo de restrição (geométrica, funcional, variacional)

### Revisão ativa do dia

Responda sem consultar:
- Quais os três domínios de um product model? O que cada um contém?
- O que é STEP-NC e como difere do código G tradicional?
- O que é Design Intent? Dê um exemplo.
- Qual a diferença entre modelagem paramétrica e variacional?
- Dê um exemplo de restrição funcional.

### Entrega do dia

Escreva uma folha-resumo com:
- Diagrama dos três domínios do product model
- Tabela: paramétrico vs. variacional
- Tabela dos 3 tipos de restrições com exemplos

---

## Dia 3: Métodos de Resolução + Features (clássico)

### Objetivo do dia

Fechar o Bloco 2 (métodos de resolução) e cobrir o Bloco 3 clássico (features — classificação, FeR, DbF).

### Estudar

Ler `material-dia-3.md`:
- Procedural vs. Constraint-Based
- Grafos de restrições (com fundação Mortenson)
- Sistemas de equações simultâneas (sub-restrito, bem-restrito, sobre-restrito)
- Função implícita
- 4 deficiências do CAD tradicional
- Features (classificações, FeR, DbF)

### Foco principal

- Procedural vs. declarativo (constraint-based)
- Grafos de restrições (nós = geometria, arestas = restrições)
- Sistemas sub-restritos e sobre-restritos
- 4 deficiências do CAD tradicional
- Classificações de features: física/abstrata, forma/manufatura, rotacional/prismática
- Feature recognition vs. feature-based design

### O que você precisa sair sabendo

- Comparar procedural com constraint-based
- Explicar o que acontece com sistemas sub-restritos e sobre-restritos
- Listar as 4 deficiências do CAD tradicional e explicar cada uma
- Classificar features nos três eixos de classificação
- Diferenciar feature recognition de feature-based design

### Revisão ativa do dia

Responda sem consultar:
- Qual a diferença entre abordagem procedural e constraint-based?
- O que é um sistema sub-restrito? E sobre-restrito?
- Quais as 4 deficiências do CAD tradicional?
- Qual a diferença entre feature física e abstrata?
- Por que form feature e manufacturing feature podem ser diferentes para a mesma geometria?

### Entrega do dia

Escreva uma folha-resumo com:
- Tabela comparativa: CAD tradicional vs. CAD baseado em features
- Diagrama de classificação de features (3 eixos)
- Mapa mental: deficiências do CAD tradicional → como features resolvem

---

## Dia 4: Decomposição + Estruturas de Dados Espaciais + LOD 🆕

### Objetivo do dia

Cobrir o Bloco 4 inteiro — os tópicos novos dos slides 13, 13a e 14 que não estavam no material anterior.

### Estudar

Ler `material-dia-4.md`:
- Representação por Decomposição (uniforme e não-uniforme)
- Voxels (características, operações booleanas)
- Quadtree (2D) e Octree (3D) — subdivisão recursiva
- BSP-tree (Axis-Aligned e Polygon-Aligned)
- Conversão entre representações
- Winged-Edge e Half-Edge
- Manifold
- MX Quadtree, PR Quadtree, Extended Octree, Graftree
- KD-Tree, BVH
- LOD (Level of Detail)

### Foco principal

- Decomposição uniforme (voxels) vs. não-uniforme (quadtree, octree)
- Características dos voxels: unicidade, não-ambiguidade, **não-concisão**
- Estados de nós na Quadtree/Octree: Empty, Full, Partial
- Operações booleanas em quadtree (tabela)
- BSP-tree: diferença Axis-Aligned vs. Polygon-Aligned
- Winged-Edge vs. Half-Edge (orientação)
- MX vs. PR Quadtree
- KD-Tree: complexidade O(log n) médio
- BVH vs. Octree
- LOD: critério de troca (triângulos vs. pixels)

### O que você precisa sair sabendo

- Explicar como funciona uma Quadtree (subdivisão recursiva)
- Comparar Winged-Edge e Half-Edge
- Dizer o que é manifold e como verificar
- Explicar a diferença entre MX Quadtree e PR Quadtree
- Calcular threshold de LOD (ex: 640×480, objeto ocupa metade)
- Listar conversões viáveis e inviáveis entre representações

### Revisão ativa do dia

Responda sem consultar:
- Quais as duas formas de decomposição? Qual a diferença?
- O que caracteriza um voxel? (unicidade, ambiguidade, concisão)
- Como funciona a subdivisão em uma Octree?
- O que é uma BSP-tree? Quais os dois tipos?
- Qual a diferença entre Winged-Edge e Half-Edge?
- O que é LOD e como se decide quando trocar de nível?

### Entrega do dia

Escreva uma folha-resumo com:
- Diagrama Quadtree (subdivisão NW, NE, SW, SE)
- Tabela de operações booleanas em Quadtree
- Tabela de conversão entre representações (CSG↔B-rep↔Células)
- Comparação Winged-Edge vs. Half-Edge

---

## Dia 5: Complementos de Features + Problemas de Validação 🆕

### Objetivo do dia

Cobrir o Bloco 3 expandido (taxonomias, DSG, sistemas híbridos, problemas de validação) e os complementos de restrições do slide 17.

### Estudar

Ler `material-dia-5.md`:
- Complementos de restrições (slide 17): definições formais, quadro comparativo detalhado, 80% das tarefas são variacionais
- Definições históricas de features (Grayer, Pratt, Lenau, Henderson)
- Features abstratas detalhadas (estruturais, físicas, precisão, material)
- Taxonomias: Pratt, Gindy (EAD's), Hounsell (1998)
- DSG (Destructive Solid Geometry)
- 4 formas de representar features
- Tipos de sistemas (FeR, DbF, Híbridos) aprofundado
- Problemas de validação: interações, thin walls, 8 problemas de edição
- Validação geométrica vs. semântica (split, delete, merge, label)

### Foco principal

- Quadro comparativo paramétrico vs. variacional (14 critérios)
- Definições: variáveis do modelo, dimensões, parâmetros
- Por que "boss e slot têm a mesma topologia"
- Taxonomia de Gindy (EAD's): 0 a 5 direções de acesso
- DSG: CSG apenas com diferença
- 4 formas de integrar FeR em DbF
- 4 tipos de interação entre features
- 8 problemas de edição (saber pelo menos 4)
- Validação semântica: Split, Delete, Merge, Label

### O que você precisa sair sabendo

- Listar pelo menos 5 diferenças entre paramétrico e variacional
- Explicar a taxonomia de Gindy (EAD's)
- Dizer por que não há definição única de feature (Pratt93)
- Explicar os 4 tipos de interação entre features
- Descrever 4 dos 8 problemas de edição
- Diferenciar validação geométrica de validação semântica

### Revisão ativa do dia

Responda sem consultar:
- Por que "boss e slot têm a mesma topologia" e isso é um problema?
- Como Gindy classifica features? O que são EAD's?
- O que é DSG?
- Quais os 4 tipos de interação entre features?
- Cite 4 dos 8 problemas de edição em features.
- O que são as operações split, delete, merge e label?

### Entrega do dia

Escreva uma folha-resumo com:
- Tabela completa: paramétrico vs. variacional (todos os critérios)
- Mapa das taxonomias (Pratt, Gindy, Hounsell)
- Lista dos 8 problemas de edição com descrição curta

---

## Dia 6: Consolidação e Simulado

### Objetivo do dia

Revisar tudo, fazer o simulado e identificar pontos fracos para reforçar.

### Atividades

1. **Revisão rápida (1h):** Reler as folhas-resumo que você produziu nos dias 1-5
2. **Simulado (1h30):** Resolver o arquivo `simulado-teorico-50-questoes.md` (atualizado com novas questões)
3. **Correção e reforço (1h):** Corrigir pelo gabarito e voltar ao material nos tópicos em que errou

### Checklist de prontidão para a prova

Antes de dormir no dia 6, você deve conseguir responder estas 15 perguntas sem consultar:

1. Qual a diferença fundamental entre STEP e IGES?
2. O que é um Application Protocol? Cite dois.
3. Para que servem EXPRESS e SDAI?
4. Quais são os três domínios de um product model?
5. O que é Design Intent? Dê um exemplo.
6. Qual a diferença entre modelagem paramétrica e variacional? (liste 3 critérios)
7. Quais são as quatro deficiências do CAD tradicional?
8. Como funciona uma Octree? (Empty, Full, Partial)
9. O que é uma BSP-tree e quais os dois tipos?
10. Winged-Edge vs. Half-Edge: qual a diferença principal?
11. O que é LOD e qual o critério para trocar de nível?
12. Como a taxonomia de Gindy classifica features?
13. Quais os 4 tipos de interação entre features?
14. Cite 3 dos 8 problemas de edição em features.
15. O que é validação semântica? (operações split, delete, merge, label)

Se travar em alguma, volte ao material e revise a seção correspondente.

### Dica final

A prova é teórica — foque em **explicar conceitos com suas palavras**, **comparar ideias** (STEP vs. IGES, paramétrico vs. variacional, FeR vs. DbF, Winged-Edge vs. Half-Edge, BVH vs. Octree), e **justificar por que certas evoluções foram necessárias**.
