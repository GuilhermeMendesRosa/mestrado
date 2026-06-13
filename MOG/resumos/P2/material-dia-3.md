# Material de Estudo — Dia 3: Métodos de Resolução e Modelagem Baseada em Features

**Fontes:** Mortenson Capítulo 11 (topologia, grafos, CSG, B-rep, operações booleanas) + Capítulo 10 (limitações das primitivas parametrizadas) + conhecimento complementar para métodos de resolução, deficiências do CAD tradicional e features.

---

# PARTE A — Fechando o Bloco 2: Métodos Matemáticos e Computacionais de Resolução

## 1. Modelagem Procedural vs. Baseada em Restrições

### 1.1 Abordagem Procedural

Na abordagem procedural, o modelo é construído por uma **sequência fixa de operações**. Cada passo depende dos anteriores, e o resultado é determinado pela ordem de execução.

> **Mortenson, Cap. 11.4 (p. 364):** "A Boolean model is a **procedural model**... This Boolean statement defining D says nothing quantitative about the new solid it creates. It only specifies the **procedure** for combining the primitive constituents."

Embora Mortenson esteja falando de modelos booleanos, o conceito de procedural se aplica amplamente: define-se **como** construir, não apenas **o que** se deseja.

**Exemplo procedural:**
```
1. Criar um retângulo de 100 × 50
2. Fazer um furo circular de diâmetro 10 a 15 mm da borda esquerda
3. Arredondar as 4 arestas verticais com raio 5
```

Se você quiser mudar a posição do furo, precisa voltar ao passo 2. A ordem importa.

**Analogia:** Programação imperativa — você diz "faça isso, depois isso, depois aquilo".

### 1.2 Abordagem Baseada em Restrições (Constraint-Based / Declarativa)

Na abordagem baseada em restrições, declara-se **o que se deseja**, e um mecanismo de resolução (solver) encontra a geometria que satisfaz todas as condições.

**Exemplo declarativo (mesmo resultado):**
```
Existe um retângulo R com largura=100 e altura=50
Existe um furo F circular com diâmetro=10
A distância do centro de F à borda esquerda de R é 15
As arestas verticais de R têm raio de arredondamento 5
```

A ordem das declarações não importa — o solver resolve todas juntas.

**Analogia:** Programação declarativa (SQL, Prolog) — você diz "quero os registros que satisfaçam estas condições", e o motor de busca decide como encontrar.

### 1.3 Comparação

| Abordagem | Procedural | Constraint-Based |
|-----------|-----------|------------------|
| **Define** | Como construir | O que obter |
| **Ordem** | Importa | Não importa |
| **Modificação** | Requer reexecutar passos | Requer re-resolver |
| **Previsibilidade** | Alta (determinístico) | Média (múltiplas soluções) |
| **Complexidade do solver** | Baixa | Alta |
| **Captura de Design Intent** | Implícita (na sequência) | Explícita (nas restrições) |

---

## 2. Grafos de Restrições

### 2.1 Fundação do Mortenson: Grafos na Modelagem Geométrica

O Mortenson dedica a Seção 11.2 (p. 335-341) a **graph-based models**. Ele define os conceitos fundamentais:

> "A geometric model emphasizing topological structure, with data pointers linking together an object's faces, edges, and vertices, is a **graph-based model**."

Conceitos do Mortenson que se aplicam a grafos de restrições:

- **Grafo:** "a set of nodes (or points) connected by branches (lines)." (p. 335)
- **Nó (node/vertex):** representa um elemento (ponto, reta, círculo, face)
- **Aresta (branch/edge):** representa uma relação entre dois elementos
- **Grau (degree):** número de arestas incidentes em um nó
- **Árvore (tree):** grafo conexo sem circuitos
- **Árvore binária:** cada nó tem no máximo dois descendentes
- **Percursos (traversals)** de árvore binária (p. 339-340):
  - **Preorder:** raiz → esquerda → direita
  - **Postorder:** esquerda → direita → raiz
  - **Inorder:** esquerda → raiz → direita

> "Two kinds of information define a graph-based representation: **pointers** defining topology or connectivity between vertices, edges, and faces... and **numerical data** defining curve and surface equations and vertex coordinates." (p. 335)

### 2.2 Aplicação a Restrições: Grafo de Restrições

Em um sistema de restrições de CAD, o grafo é construído de forma análoga:

- **Nós:** elementos geométricos (pontos, linhas, círculos, planos)
- **Arestas:** restrições entre esses elementos

```
[C1] ──tangente── [L1]
  │                 │
  │              [dist=50]
  │                 │
[concêntrico]     [L2]
  │                 │
[C2] ──paralelo── [L3]
```

**O que o grafo permite:**

1. **Análise de dependências:** identificar quais elementos são afetados quando uma restrição muda
2. **Detecção de redundância:** duas arestas impondo a mesma restrição
3. **Detecção de conflitos:** restrições contraditórias (ex: L1 paralela a L2 E L1 perpendicular a L2)
4. **Ordenação de resolução:** planejar a sequência de avaliação para reduzir o tamanho do sistema
5. **Decomposição:** dividir um grafo grande em subgrafos menores e independentes (divide and conquer)

### 2.3 Predicados

Um **predicado** é uma condição lógica que deve ser verdadeira para que o modelo seja válido. É a formalização de uma restrição.

Exemplos de predicados:
- `Parallel(L1, L2)` — deve ser verdadeiro
- `Distance(P1, P2) = d` — deve ser verdadeiro
- `Angle(L1, L2) = 90°` — deve ser verdadeiro

O conjunto de todos os predicados forma o sistema que o solver deve satisfazer.

---

## 3. Sistemas de Equações Simultâneas

Quando cada restrição gera uma ou mais equações, o problema de modelagem se transforma em um sistema de equações que precisa ser resolvido.

### 3.1 Caracterização

Sejam:
- **n** = número de variáveis (graus de liberdade do sistema)
- **m** = número de equações (restrições independentes)

| Situação | Relação | Consequência |
|----------|---------|-------------|
| **Sub-restrito** (under-constrained) | n > m | Infinitas soluções — geometria "flutua" |
| **Bem-restrito** (well-constrained) | n = m | Solução finita (idealmente única) |
| **Sobre-restrito** (over-constrained) | n < m | Pode não ter solução — restrições conflitantes |

**Exemplo sub-restrito:**
- 3 pontos no plano (n = 6 coordenadas)
- Restrições: distância P1-P2 = 10, distância P2-P3 = 10 (m = 2)
- Como n > m, os pontos podem girar e transladar livremente (infinitas posições satisfazem as distâncias)

**Exemplo bem-restrito:**
- 3 pontos no plano (n = 6)
- Restrições: P1 fixo na origem (2 eq.), P2 no eixo X (1 eq.), distância P1-P2 = 10 (1 eq.), distância P2-P3 = 10 (1 eq.), distância P1-P3 = 10 (1 eq.)
- 6 equações para 6 variáveis → triângulo equilátero de lado 10 (solução única, exceto por simetria)

**Exemplo sobre-restrito:**
- 2 pontos (n = 4 coordenadas)
- Restrições: distância = 10, distância = 20, P1 fixo, P2 fixo em outra posição
- Impossível satisfazer todas ao mesmo tempo

### 3.2 Métodos de Resolução

**Newton-Raphson (método numérico iterativo):**
- Lineariza o sistema não-linear a cada iteração
- Requer um chute inicial próximo da solução
- Pode divergir ou convergir para solução errada
- É o método mais usado em CAD comercial

**Outros métodos:**
- Métodos de otimização (minimizar soma dos quadrados dos erros)
- Métodos simbólicos (para sistemas polinomiais pequenos)
- Métodos híbridos (decomposição do grafo + resolução numérica)

### 3.3 Desafios práticos

1. **Múltiplas soluções:** um sistema bem-restrito pode ter várias soluções (ex: um ponto a distância d de dois pontos fixos tem 2 posições possíveis)
2. **Convergência:** o solver pode não convergir se o chute inicial for ruim
3. **Redundâncias:** restrições redundantes precisam ser detectadas e ignoradas
4. **Performance interativa:** para CAD, o solver precisa rodar em tempo real enquanto o usuário arrasta elementos

---

## 4. Função Implícita

### 4.1 Definição

Uma função implícita é da forma **F(x, y, z, ...) = 0**, sem isolar uma variável.

| Forma | Exemplo | Característica |
|-------|---------|----------------|
| **Explícita** | y = f(x) → y = x² | Uma variável isolada |
| **Implícita** | F(x,y) = 0 → x² + y² − R² = 0 | Nenhuma variável isolada |

### 4.2 Quando usar função implícita

- A relação não pode ser facilmente isolada (ex: interseção de superfícies complexas)
- A forma implícita é mais compacta ou expressiva (ex: círculo: x² + y² = R² é mais elegante que y = ±√(R² − x²))
- Para representar restrições: uma restrição pode ser expressa como F(...) = 0

### 4.3 Vantagens e desvantagens

| Vantagens | Desvantagens |
|-----------|-------------|
| Pode representar relações que não têm forma explícita | Mais difícil de avaliar computacionalmente |
| Natural para expressar restrições | Para obter y dado x, precisa resolver equação |
| Útil para detecção de inside/outside (F < 0 vs. F > 0) | Pode ser ambígua (qual ramo usar?) |
| Invariante sob transformações | Nem sempre é fácil construir a função F |

### 4.4 Relação com modelagem geométrica

**Mortenson, Cap. 11.3:** A classificação inside/outside/boundary de um ponto em relação a um sólido frequentemente usa funções implícitas. Por exemplo, para testar se um ponto (x,y,z) está dentro de uma esfera de raio R centrada na origem: se x² + y² + z² − R² < 0, está dentro; se > 0, está fora; se = 0, está na superfície.

**Em restrições:** uma restrição geométrica "distância entre P1 e P2 é d" pode ser expressa como:

```
|P1 − P2| − d = 0    (forma implícita da restrição)
```

---

# PARTE B — Bloco 3: CAD Tradicional e Modelagem Baseada em Features

## 5. Deficiências do CAD Tradicional

### 5.1 Contexto: o que é "CAD tradicional"

O CAD tradicional refere-se aos sistemas baseados em CSG e B-rep puros, tais como descritos por Mortenson no Capítulo 11:

- **CSG (Constructive Solid Geometry):** árvore binária de operações booleanas sobre primitivas
- **B-rep (Boundary Representation):** representação explícita da fronteira (faces, arestas, vértices)

Estes sistemas representam a geometria de forma matematicamente rigorosa (como Mortenson demonstra extensivamente), mas têm limitações do ponto de vista da **engenharia** — ou seja, da utilidade do modelo para projetar, fabricar e manter produtos reais.

### 5.2 As quatro deficiências

#### Deficiência 1: Dados "Microscópicos"

O CAD tradicional opera com entidades geométricas de baixo nível: pontos, linhas, arestas, faces.

**Mortenson, Cap. 11.6 (B-rep, p. 377):**
> "The objective of a boundary model (or b-rep) is to build a complete representation of a solid as an organized collection of surfaces. We can represent a solid as a union of faces (surfaces), bounded by edges (curves), which in turn are bounded by vertices (points)."

Esta hierarquia (faces → arestas → vértices) é matematicamente completa, mas não carrega significado de engenharia. Um furo não é "um furo" — é uma coleção de superfícies cilíndricas e arestas circulares. Um rasgo de chaveta não é "um rasgo" — é um conjunto de faces planas.

**O problema:** O engenheiro pensa em furos, rasgos, ressaltos, chanfros. O computador vê vértices, arestas, faces. Há um gap semântico entre o que o humano quer comunicar e o que a estrutura de dados armazena.

#### Deficiência 2: Sub-especificação Geométrica

A geometria pode estar matematicamente correta, mas sem informação suficiente para manufatura e análise.

**O que falta:**
- Um cilindro modelado como superfície não informa se é um furo passante ou cego
- Não informa se é roscado, qual o material, qual a tolerância
- Não informa como deve ser fabricado (broqueado? mandrilhado? fresado?)

**Mortenson, Cap. 11.5 (CSG, p. 372-373), aponta que mesmo a dual representation (CSG + B-rep) resolve o problema de representação geométrica, mas não o problema semântico:**
> "More powerful modeling systems often generate two representations of a solid. The first is the procedural or constructive representation... The second is the boundary representation... The boundary representation is computed from the constructive representation by a set of algorithms called the **boundary evaluator**."

Ambas as representações (CSG e B-rep) são geométricas. Nenhuma delas carrega significado de engenharia.

#### Deficiência 3: Construção Tediosa

**Mortenson, Cap. 11.5 (p. 371), descreve o processo CSG:**
> "Constructive solid geometry representations of complex solids are ordered binary trees whose leaf or terminal nodes are either primitives or transformations. The nonterminal nodes are either regularized Boolean operators or transformations that operate on their two subnodes."

Para criar uma peça complexa, o usuário precisa:
1. Definir múltiplas primitivas (blocos, cilindros, etc.)
2. Posicioná-las e dimensioná-las
3. Aplicar uma sequência de operações booleanas (união, diferença, interseção)
4. Repetir para cada detalhe

Isso é conceitualmente equivalente a "esculpir" a peça removendo material com formas simples — tedioso e contra-intuitivo. Uma mudança de projeto pode exigir reconstruir toda a árvore CSG.

#### Deficiência 4: Estrutura de Dados de um Único Nível

**Mortenson, Cap. 11.1 (p. 318):**
> "Model connectivity and homogeneity are topological properties, so consideration of topology is also an important part of the modeling process."

Embora Mortenson enfatize a importância da topologia para garantir modelos válidos, ele também mostra que a estrutura resultante é **plana**: a hierarquia B-rep (solid → shell → face → loop → edge → vertex) e a árvore CSG (primitivas → operações → resultado) descrevem a geometria, mas não agrupam elementos por função.

**O que falta:**
- Agrupamento de elementos relacionados (ex: todos os furos de fixação)
- Relações funcionais (ex: "este furo é para o parafuso que prende a tampa")
- Histórico de design com significado (a árvore CSG registra operações booleanas, não decisões de projeto)

### 5.3 Síntese: por que evoluir?

| Deficiência | Causa raiz | Solução (features) |
|-------------|-----------|-------------------|
| Dados microscópicos | Entidades de baixo nível sem semântica | Features = geometria + significado |
| Sub-especificação | Só geometria, sem engenharia | Features carregam tolerâncias e parâmetros de processo |
| Construção tediosa | Operações booleanas sobre primitivas | Operações de feature de alto nível |
| Estrutura plana | Sem hierarquia funcional | Árvore de features com agrupamentos |

---

## 6. Feições Geométricas (Features)

### 6.1 Definição de Feature

Uma **feature** (feição) é um elemento geométrico que carrega **significado de engenharia**. Diferente de uma face ou aresta (pura geometria), uma feature agrega:

```
FEATURE = GEOMETRIA + SEMÂNTICA + COMPORTAMENTO
```

| Componente | O que é | Exemplo para feature "furo passante M8" |
|-----------|---------|------------------------------------------|
| **Geometria** | Forma, dimensões, posição | Cilindro de diâmetro 8 mm atravessando a peça |
| **Semântica** | Significado de engenharia | "Para parafuso de fixação M8, com tolerância H7" |
| **Comportamento** | Como se adapta a mudanças | Se a espessura da peça muda, o furo permanece passante |

### 6.2 Classificação 1: Features Físicas vs. Abstratas

#### Features Físicas (Physical/Concrete Features)

Correspondem a geometria real, visível e mensurável no modelo 3D.

| Feature Física | Descrição | Exemplo de uso |
|---------------|-----------|---------------|
| **Hole (furo)** | Remoção cilíndrica de material | Fixação, passagem, alívio |
| **Pocket (cavidade)** | Remoção prismática de material | Alojamento, redução de peso |
| **Slot (rasgo)** | Remoção alongada | Chaveta, guia |
| **Boss (ressalto)** | Adição cilíndrica de material | Apoio de mancal, reforço |
| **Rib (nervura)** | Adição alongada para rigidez | Reforço estrutural |
| **Chamfer (chanfro)** | Corte em ângulo na aresta | Facilitação de montagem, segurança |
| **Fillet (arredondamento)** | Transição curva entre faces | Redução de concentração de tensão |

#### Features Abstratas (Abstract Features)

Não têm geometria própria — são informações anexadas ao modelo.

| Feature Abstrata | Exemplo |
|-----------------|---------|
| **Tolerância dimensional** | 10 ± 0.05 mm |
| **Tolerância geométrica** | Planicidade 0.02 mm |
| **Acabamento superficial** | Ra 1.6 μm |
| **Especificação de material** | Aço SAE 1045 |
| **Tratamento térmico** | Cementação, têmpera |
| **Nota de fabricação** | "Rebarbar após usinagem" |

> **Ponto de prova:** Features abstratas são tão importantes quanto físicas para a manufatura, mesmo que não tenham representação geométrica. Um furo sem tolerância é inútil para a produção.

### 6.3 Classificação 2: Form Features vs. Manufacturing Features

Esta classificação é ligada ao **ponto de vista**: design ou manufatura.

#### Form Features (Feições de Forma)

Orientadas ao **projeto/design**. Representam como o projetista concebe a peça.

- Exemplos: ressalto (boss), nervura (rib), flange, grade de reforço
- O projetista pensa em termos funcionais: "aqui preciso de um apoio para o mancal" → ressalto
- A geometria é uma **adição** de material com propósito funcional

#### Manufacturing Features (Feições de Manufatura)

Orientadas ao **processo de fabricação**. Representam como a peça será produzida.

- Exemplos: cavidade a ser fresada (pocket), furo a ser broqueado, face a ser faceada
- O engenheiro de manufatura pensa em termos de remoção de material: operações, ferramentas, trajetórias
- A geometria é um **volume a remover** do blank

#### O problema do mapeamento Design ↔ Manufatura

A mesma geometria pode ser feature diferente dependendo do ponto de vista:

- No design: "ressalto para apoio do mancal" (adição de material)
- Na manufatura: "cavidade a ser fresada ao redor do ressalto" (o que se remove é o material em volta)

**Não existe mapeamento 1:1.** Uma feature de design pode corresponder a múltiplas operações de manufatura, e uma operação de manufatura pode afetar múltiplas features de design.

> **Ponto de prova:** Esta discrepância é um dos grandes desafios da integração CAD-CAM automatizada.

### 6.4 Classificação 3: Features Rotacionais vs. Prismáticas

Esta classificação é baseada na **geometria e no processo de usinagem**.

#### Features Rotacionais

- Associadas a peças **torneadas** (simetria axial)
- A geometria é gerada por **revolução** de um perfil 2D em torno de um eixo
- Usinagem principal: **torno** (a peça gira, a ferramenta translada)

| Feature Rotacional | Descrição |
|-------------------|-----------|
| Cilindro externo | Diâmetro externo torneado |
| Cone | Transição cônica |
| Faceamento | Face perpendicular ao eixo |
| Canal (groove) | Canal para anel de retenção |
| Rosca externa | Rosca torneada |
| Furo de centro | Furo de centragem para montagem no torno |

**Critério de identificação:** A peça tem um eixo de simetria principal? A maior parte da usinagem é feita em um torno? Se sim, é rotacional.

#### Features Prismáticas

- Associadas a peças **fresadas** (faces planas)
- A geometria é baseada em planos ortogonais ou inclinados
- Usinagem principal: **fresadora / centro de usinagem** (ferramenta gira, peça se move)

| Feature Prismática | Descrição |
|-------------------|-----------|
| Cavidade (pocket) | Rebaixo de faces planas |
| Rasgo (slot) | Canal alongado |
| Face rebaixada (step) | Degrau entre duas faces |
| Furo (hole) | Furo não-coaxial com eixo de revolução da peça |
| Face inclinada | Plano não-ortogonal à base |

**Critério de identificação:** A geometria é predominantemente formada por faces planas, típicas de operações de fresamento, furação e mandrilhamento?

#### Peças híbridas

Muitas peças combinam ambos os tipos. Exemplo clássico: **eixo com rasgo de chaveta**.
- O corpo do eixo é rotacional (cilindros, cones, ressalto — torneados)
- O rasgo de chaveta é prismático (fresado)

**Para a prova:** saiba distinguir qual parte da peça pertence a cada categoria.

### 6.5 Feature Recognition vs. Feature-Based Design

#### Feature Recognition (Reconhecimento de Features)

Parte de um modelo geométrico **já pronto** (tipicamente B-rep) e tenta identificar features automaticamente.

```
B-rep (faces, arestas, vértices)
       │
       ▼
  Algoritmo de reconhecimento
       │
       ▼
  Lista de features: furo, cavidade, rasgo...
```

**Desafios:**
- Features que se intersectam podem ser difíceis de separar
- Mesma geometria pode ser interpretada como diferentes features
- Depende de heurísticas e regras que podem falhar
- Exemplo: um furo que atravessa uma cavidade — como saber que é um furo e não parte da cavidade?

#### Feature-Based Design (Design by Features)

O projetista constrói o modelo **desde o início** usando operações de feature com significado.

```
Feature "Base retangular" → Feature "Furo passante" → Feature "Rasgo de chaveta" → ...
```

**Vantagens:**
- Design Intent é capturado naturalmente durante a construção
- A árvore de features é o próprio histórico de projeto
- Modificações preservam a intenção original
- Cada feature pode carregar tolerâncias e parâmetros de manufatura

| Critério | Feature Recognition | Feature-Based Design |
|----------|-------------------|---------------------|
| **Ponto de partida** | Modelo geométrico pronto | Construção desde o zero |
| **Design Intent** | Tentar recuperar depois | Capturar durante |
| **Flexibilidade** | Funciona com modelos legados | Requer sistema feature-based |
| **Robustez** | Sujeita a falhas de interpretação | Robusta (intenção explícita) |
| **Uso típico** | Migração, interoperabilidade | Projeto novo |

---

## 7. Como as Features Resolvem as Deficiências do CAD Tradicional

| Deficiência | Como as features resolvem |
|-------------|--------------------------|
| **Dados microscópicos** | Features são entidades de alto nível com significado (furo, não faces cilíndricas) |
| **Sub-especificação** | Cada feature carrega parâmetros de manufatura, tolerâncias e especificações |
| **Construção tediosa** | Operações de alto nível ("criar furo passante" vs. modelar cada face) |
| **Estrutura plana** | Árvore de features hierárquica com agrupamentos, relações e histórico |

---

## 8. Autoavaliação do Dia 3

Responda sem consultar:

1. Qual a diferença entre abordagem procedural e abordagem baseada em restrições?
2. Como um grafo de restrições é estruturado (o que são os nós? o que são as arestas?)?
3. O que é um sistema sub-restrito? E um sistema sobre-restrito?
4. O que é uma função implícita? Dê um exemplo e explique quando ela é usada.
5. Quais são as quatro deficiências do CAD tradicional? Explique cada uma brevemente.
6. Como Mortenson descreve a estrutura plana do B-rep? (solid → shell → ...)
7. Qual a diferença entre feature física e feature abstrata? Dê exemplos.
8. Por que uma mesma geometria pode ser uma Form Feature diferente de uma Manufacturing Feature?
9. O que caracteriza uma feature como rotacional? E como prismática?
10. Qual a diferença entre Feature Recognition e Feature-Based Design?
11. Como a árvore CSG do Mortenson se relaciona com a crítica de "estrutura de dados plana"?
12. O que Mortenson diz sobre a limitação do número de primitivas parametrizadas (Cap. 10, p. 301)?
