# Material de Estudo — Dia 4: Representação por Decomposição, Estruturas de Dados Espaciais e LOD

**Fonte:** Slides 13, 13a e 14 do professor Rosso + Mortenson Capítulo 11 (topologia, grafos, B-rep) + conhecimento complementar.

---

# PARTE A — Representação por Decomposição (Slide 13)

## 1. O que é Representação por Decomposição

Até agora estudamos representações **construtivas** (CSG, B-rep) — que constroem o sólido a partir de primitivas e operações. A representação por decomposição adota a abordagem oposta: **subdivide o espaço** e representa o objeto por quais células estão ocupadas.

**Definição do slide (Rosso):**
> "Essa representação consiste em subdividir o espaço em uma **família de células volumétricas**. O objeto é representado através da **enumeração das células** que o intersectam juntamente com uma amostra de seus atributos."

A decomposição é adequada para objetos cujos **atributos variam no interior** (ex: densidade, temperatura, composição).

### Duas formas principais

```
Representação por Decomposição
├── UNIFORME (Matricial / Voxels)
│   └── Reticulado regular, células de mesmo tamanho
│
└── NÃO-UNIFORME
    ├── Variação de Tamanho: Quadtree, Octree, BSP-tree
    └── Variação de Forma: Células quaisquer, Diagramas de Voronoi
```

---

## 2. Representação Matricial (Voxels)

### 2.1 Definição

A representação matricial é a extensão 3D do bitmap 2D. Assim como uma imagem 2D é uma matriz de **pixels** (picture elements), um sólido é representado por uma matriz 3D de **voxels** (volume elements).

> **Mortenson (Cap. 11.5, p. 371):** "Requicha (1980) viewed CSG as a generalization of cell decomposition. In cell decomposition models, we combine individual cells using a gluing operation... CSG operators are more versatile, since boundaries of joined components need not match."

A decomposição uniforme é o caso mais simples de cell decomposition: células idênticas em uma grade regular.

### 2.2 Como funciona

- Define-se um reticulado a partir do **produto cartesiano** de partições uniformes dos eixos x, y, z
- Cada célula do reticulado é um paralelepípedo (geralmente um cubo) = **voxel**
- Cada voxel armazena: dentro/fora do sólido + amostra de atributos
- Também chamada de **representação volumétrica** ou **imagem 3D**

```
Exemplo 2D (para simplificar):

  0 1 2 3 4 x
0 □ □ ■ □ □      ■ = célula ocupada
1 □ ■ ■ ■ □      □ = célula vazia
2 □ ■ ■ ■ □
3 □ ■ ■ ■ □
4 □ □ ■ □ □
```

No 3D, a mesma ideia com uma matriz tridimensional.

### 2.3 Características (do slide)

| Característica | Avaliação |
|---------------|-----------|
| **Unicidade** | Sim (tem unicidade) |
| **Ambiguidade** | Não é ambígua |
| **Validação** | Fácil de validar |
| **Precisão** | Depende do tamanho/forma do voxel |
| **Concisão** | **Não é concisa** (muitos voxels) |
| **Domínio** | Qualquer sólido |

> **Ponto de prova:** A representação por voxels é a única que combina não-ambiguidade com facilidade de validação. O preço é a falta de concisão.

### 2.4 Operações Booleanas em Voxels

As operações booleanas são extremamente simples no domínio de voxels, pois trabalham no domínio dos números inteiros (ocupado = 1, vazio = 0):

| Operação | Voxel A | Voxel B | Resultado |
|----------|---------|---------|-----------|
| União (A ∪ B) | 1 | 0 | 1 |
| | 0 | 1 | 1 |
| | 1 | 1 | 1 |
| | 0 | 0 | 0 |
| Interseção (A ∩ B) | 1 | 1 | 1 |
| | qualquer outro | | 0 |
| Diferença (A − B) | 1 | 0 | 1 |
| | qualquer outro | | 0 |

**Vantagem:** Operações booleanas em voxels são triviais — são operações lógicas bit a bit.

### 2.5 Vantagens e aplicações

- Diversas técnicas de análise e processamento de imagens podem ser aplicadas
- A visualização é simples devido à estrutura regular
- Usada pela grande maioria dos equipamentos de captura de objetos volumétricos (tomografia, ressonância magnética, scanners 3D)
- Muito utilizada em **Visualização Volumétrica** (Volume Rendering)

---

## 3. Decomposição Não-Uniforme

### 3.1 Por que não-uniforme?

O problema do voxel uniforme é o consumo de memória: para boa precisão, precisa-se de muitos voxels, mas regiões homogêneas (totalmente dentro ou totalmente fora do objeto) não precisam de tanta resolução.

**Solução:** usar células de tamanhos variáveis — maiores em regiões homogêneas, menores perto das bordas.

### 3.2 Decomposição Celular com Células Quaisquer

- Células podem ter qualquer formato
- Não tem unicidade (mesmo objeto pode ser decomposto de várias formas)
- É um caso particular da representação universal
- **É exata, mas não concisa**
- Domínio restrito (depende das células existentes)
- Difícil de validar (as colagens geram interseção indesejada?)

---

## 4. Quadtree (2D) e Octree (3D)

### 4.1 Conceito

São as estruturas de decomposição adaptativa mais importantes. Caracterizam-se por:

- Estrutura de dados **hierárquica** (árvore)
- **Espacialmente endereçável** (posição de cada nó é determinada por sua localização na árvore)
- **Naturalmente pré-ordenada**
- Baseadas no princípio de **decomposição recursiva**

### 4.2 Funcionamento da Quadtree (2D)

1. Começa com uma região quadrada representando todo o espaço
2. Se a região é **totalmente vazia** → nó folha **Empty (E)**
3. Se a região é **totalmente ocupada** → nó folha **Full (F)**
4. Se a região é **parcialmente ocupada** → nó **Partial (P)** — subdivide em 4 quadrantes iguais (NW, NE, SW, SE) e repete o processo
5. Continua recursivamente até um critério de parada (profundidade máxima ou célula homogênea)

```
Exemplo de Quadtree:

┌──────┬──┬──┐           Raiz (P)
│      │  │  │          / / \ \
│      ├──┼──┤      NW(P) NE(F) SW(E) SE(F)
│      │  │  │      / / \ \
├──┬──┼──┼──┤   NW(F) NE(E) SW(E) SE(F)
│  │  │  │  │
└──┴──┴──┴──┘
```

### 4.3 Octree (3D)

Mesmo princípio, mas em 3D: cada nó parcial é subdividido em **8 octantes** (daí o nome).

- Cada subdivisão gera 2³ = 8 filhos
- Acesso em **O(log n)** onde n é o número de elementos
- **Estrutura estática** — difícil mover voxels dentro dela; transformações exigem recriação da árvore

### 4.4 Operações Booleanas em Quadtree/Octree

| Folha A | Folha B | A ∪ B | A ∩ B |
|---------|---------|-------|-------|
| E | E | E | E |
| E | F | F | E |
| E | P | P (desce 1 nível) | E |
| F | E | F | E |
| F | F | F | F |
| F | P | F | P (desce 1 nível) |
| P | P | recursão | recursão |

### 4.5 Vantagens das estruturas hierárquicas (Quadtree/Octree)

- Simplificam operações como:
  - Detecção de interseção de objetos
  - Localização de um ponto ou bloco no espaço
  - Remoção de superfícies escondidas
- Redução de consumo de memória por agregação de dados homogêneos
- Informações podem ser armazenadas em nós intermediários (ex: soma de populações dos filhos)

### 4.6 Limitação: Padrão Xadrez

Em casos extremamente heterogêneos (ex: padrão de tabuleiro de xadrez), a Quadtree pode consumir **mais** memória que o grid equivalente, pois cada célula alternada força subdivisões até o nível máximo.

```
Xadrez 4×4: Grid = 16 elementos, Quadtree = 21 nós
```

### 4.7 MX Quadtree e PR Quadtree

**MX Quadtree (Matrix):**
- Para pontos com índices discretos (ex: elementos não-zero de matriz)
- Cada folha tem 2 estados: preto (dado presente) ou branco (vazio)
- A posição do dado está implícita na posição na árvore (convenção NW, NE, SW, SE)
- **Limitação séria:** dobrar a precisão custa 2²× (2D) ou 2³× (3D) de memória adicional
- Geralmente usada em imagens e representações discretas de funções contínuas

**PR Quadtree (Point Region):**
- Similar à MX, mas armazena coordenadas dos pontos nas folhas
- Máximo de 1 ponto por folha
- Inserir ponto próximo a outro existente pode causar muitas subdivisões

### 4.8 Extended Octree e Graftree

**Extended Octree:**
- Folhas armazenam **polígonos** que representam a superfície
- Resolve o problema de aproximação grosseira de voxels binários para superfícies
- Usa a Octree como acelerador para operações locais (booleanas)

**Graftree:**
- Folhas armazenam a **raiz de uma árvore CSG** (Constructive Solid Geometry)
- Estados de nó: FULL (dentro), EMPTY (fora), BOUNDARY (raiz da CSG)
- Permite operações CSG locais — útil quando booleanas afetam apenas regiões pequenas
- Octree como estrutura aceleradora

---

## 5. BSP-tree (Binary Space Partitioning)

### 5.1 Conceito

**Do slide (baseado em Foley 1996):**
- Criada como algoritmo de visibilidade em 1987
- Posteriormente usada para representar poliedros quaisquer
- **Árvore binária** que indica que o objeto está em um dos lados das ramificações
- Permite representar **côncavos e convexos**
- Potencialmente não compacta
- Elegante e simples conceitualmente

### 5.2 Como funciona

A ideia é similar à Octree, mas o espaço é sucessivamente dividido em **2 partes** (daí "binária") por um **plano de corte** (splitting plane).

```
Cada nó da árvore:
  - Armazena um plano de corte
  - Filho esquerdo = região "dentro" (ou atrás)
  - Filho direito = região "fora" (ou na frente)
  - Recursão até critério de parada
```

### 5.3 Dois tipos de BSP-tree

**Axis-Aligned BSP Trees:**
- Inicia com uma bounding box em torno de todo o mundo
- Divide com planos de corte paralelos aos eixos (xy, xz ou yz)
- Continua recursivamente, cada subdivisão divide apenas seu half-space
- Mais simples, mas menos eficiente em termos de compactação

**Polygon-Aligned BSP Trees:**
- Um polígono 3D qualquer (parte de um plano) é usado como splitting plane
- A escolha do polígono divisor afeta:
  - Balanceamento da árvore
  - Número de triângulos extras gerados por splitting
- **Trade-off:** árvore balanceada com muitos splits vs. árvore desbalanceada com poucos splits
- Maioria escolhe árvore desbalanceada com menos splits

---

## 6. Conversão entre Representações

**Do slide (baseado em Mantyla):**

| Conversão | Dificuldade |
|-----------|-------------|
| CSG → B-rep | **Possível** |
| B-rep → CSG | **Muito mais complicada** |
| B-rep → Células | **Simples** |
| Células → B-rep | **Relativamente simples** (marching cubes) |
| CSG → Células | **Simples** |
| Células → CSG | **Complicado** |

**Ponto de prova:** O método de modelagem (a interface do usuário) **não restringe** o modelo de representação interna e vice-versa. Um software pode ter uma interface rica em meios de modelagem e usar uma única representação interna.

---

# PARTE B — Estruturas de Dados Espaciais (Slide 13a)

## 7. Winged-Edge e Half-Edge

Estas são estruturas de dados para **malhas de triângulos** — como armazenar e navegar eficientemente em uma superfície composta por triângulos conectados.

### 7.1 Malha de Triângulos (Triangle Mesh)

> "Rede de triângulos que conecta uns aos outros por meio do compartilhamento de arestas e vértices para formar uma única superfície contínua. Uma lista de triângulos não conectados **não** é uma malha de triângulos."

Requisitos de gerência eficiente: armazenamento em disco, memória, largura de banda, acesso a triângulos adjacentes (subdivisão, modificação, compressão).

### 7.2 Manifold

**Definição (do slide):**
> "Superfície onde uma pequena vizinhança de qualquer ponto possa ser achatada em uma superfície plana."

**Verificação de manifold (regra da "entrada/saída de água"):**
1. Todas as arestas são compartilhadas por exatamente **dois** triângulos
2. Todos os vértices têm um único e completo **círculo de triângulos** em sua volta

**Importante:** Manifold **não** garante consistência na orientação das faces. É uma condição necessária mas não suficiente para uma malha bem formada.

> **Mortenson (Cap. 11.1, p. 319):** "The properties of geometric shapes that are invariant under transformations that stretch, bend, twist, or compress a figure, without tearing, puncturing, nor inducing self-intersection, are topological properties."

O conceito de manifold é fundamental para garantir que estruturas de dados para malhas funcionem sem problemas.

### 7.3 Winged-Edge

Estrutura que armazena informação de conectividade nas **arestas**. Cada aresta mantém ponteiros para:

```
             left predecessor
                   ↑
    left face ← [ARESTA] → right face
                   ↓
             right successor
                   
Também: vértice inicial, vértice final,
        left successor, right predecessor
```

- Acesso **O(1)** para acessar as arestas de uma face ou vértice
- Sempre precisa verificar a **orientação** da aresta antes de ir para a próxima

### 7.4 Half-Edge

Resolve o problema de orientação do Winged-Edge: cada aresta é dividida em **duas metades** com orientações opostas.

- Uma metade para cada triângulo que compartilha a aresta
- As duas metades têm orientações opostas entre si (uma no sentido horário, outra anti-horário)
- A travessia é igual ao Winged-Edge, mas **sem necessidade de verificar orientação**

Cada half-edge armazena ponteiros para:
- Vértice de origem
- Half-edge oposta (pair)
- Face à qual pertence
- Próxima half-edge na face (next)
- Half-edge anterior (prev)

> **Ponto de prova:** Half-Edge é mais elegante que Winged-Edge porque elimina testes condicionais de orientação durante a travessia.

---

## 8. Grid, KD-Tree e BVH

### 8.1 Grid (Matriz 3D)

- Voxels armazenados em matriz 3D
- Acesso **O(1)** a qualquer voxel e sua vizinhança
- Alto consumo de memória: Grid 20³ = 8.000 voxels (8× mais que 10³ = 1.000)
- Espaços homogêneos (ex: ar) ocupam mesmo espaço que espaços heterogêneos
- Grids uniformes **não se ajustam** a diferentes complexidades do modelo
- Consumo de memória é previsível (vantagem em sistemas com memória limitada)

### 8.2 KD-Tree

- Tipo especial de árvore BSP para organização de **pontos**
- Cada nó subdivide o espaço em **2 regiões** com plano perpendicular a um eixo
- Cada nível da árvore divide em uma dimensão diferente (alternando x, y, z)
- Suporta qualquer número de dimensões (k dimensões)
- A ordem de inserção influencia o balanceamento
- Geralmente usada em cenas com bastante espaçamento entre objetos

**Complexidade:**

| Operação | Na média | Pior caso |
|----------|----------|-----------|
| Busca | O(log n) | O(n) |
| Inserção | O(log n) | O(n) |
| Remoção | O(log n) | O(n) |
| Espaço | O(n) | O(n) |

### 8.3 BVH (Bounding Volume Hierarchy)

**Bounding Volume (BV):** volume simples (esfera, AABB) que contém completamente um conjunto de objetos.

**BVH:** organização hierárquica (árvore) de bounding volumes:
- Nó pai contém todos os objetos dos nós filhos
- Usado para acelerar testes de colisão e interseção (ray tracing)
- Se um raio não atinge o BV do nó pai, não precisa testar nenhum filho

**BVH vs. Octree (do slide):**

| BVH | Octree |
|-----|--------|
| Agrupa objetos por proximidade espacial | Subdivide o espaço uniformemente |
| Bounding volumes aninhados | Células de tamanhos variáveis por subdivisão |
| Adapta-se à distribuição dos objetos | Independente dos objetos |

---

# PARTE C — LOD: Level of Detail (Slide 14)

## 9. Conceito e Motivação

**Do slide (Hounsell/Rosso):**
> "É muito custoso mostrar um objeto completo sempre com o maior nível de detalhes. Quanto mais longe você está de um objeto, menos detalhes são necessários (isto também depende do ângulo de visão e do tamanho da tela em que é mostrado)."

### 9.1 Por que LOD?

Renderizar um modelo 3D complexo consome recursos de GPU proporcionais ao número de triângulos. Mas se o objeto está distante e ocupa poucos pixels na tela, muitos desses triângulos são menores que um pixel — ou seja, **desperdício computacional**.

**Solução:** Criar vários modelos do objeto com diferentes níveis de detalhe e usar o mais adequado para a distância/tamanho na tela.

### 9.2 Exemplo do slide

Um mesmo modelo com:
- **50 vértices** — para quando está muito distante
- **500 vértices** — distância média
- **2000 vértices** — close-up / detalhe máximo

### 9.3 O cálculo do threshold

**Exemplo do slide (tela 640×480):**
- Tela tem 640 × 480 = 307.200 pixels
- Se o objeto ocupa metade da tela → ~150K pixels
- Conclusão: Mais que ~300K triângulos é desperdício nessa distância e resolução
  - (Porque metade dos triângulos está voltada para o outro lado — back-face culling)

### 9.4 Questões práticas de implementação

1. **Como criar múltiplos níveis de detalhe?**
   - Iniciar com o mais detalhado e reconstruir com menos vértices (simplificação de malha)
   - Refazer a triangulação para cada nível

2. **Quando trocar de LOD durante a renderização?**
   - Baseado na distância do objeto à câmera e na resolução da tela
   - Critério: número de triângulos vs. número de pixels ocupados

3. **Artefatos visuais (popping):**
   - Podem ocorrer nos pontos de troca de LOD
   - O objeto "salta" de aparência quando o sistema troca de um nível para outro
   - Soluções: transições suaves (morphing), LOD contínuo (geomorphs)

> **Ponto de prova:** LOD é uma técnica de otimização, não de modelagem. Não cria geometria nova — apenas seleciona qual versão pré-computada do modelo é mais adequada para a situação atual de visualização.

---

## 10. Autoavaliação do Dia 4

Responda sem consultar:

1. O que é representação por decomposição e como ela difere das representações construtivas (CSG/B-rep)?
2. Quais as duas formas principais de decomposição?
3. O que é um voxel e quais suas características (unicidade, ambiguidade, concisão, validação)?
4. Por que a representação matricial **não é concisa**?
5. Como funciona uma Quadtree? (papel dos nós Empty, Full, Partial)
6. Como funciona uma Octree? Qual a diferença para a Quadtree?
7. O que é uma BSP-tree e quais os dois tipos?
8. Quais conversões entre representações são simples e quais são complicadas?
9. O que é uma malha manifold? Como verificar?
10. Qual a diferença entre Winged-Edge e Half-Edge?
11. O que é uma KD-Tree e como ela se diferencia de uma Octree?
12. Para que serve uma BVH?
13. O que é uma Extended Octree? E uma Graftree?
14. O que é LOD e qual o critério para trocar de nível de detalhe?
15. Por que existe um limite de triângulos além do qual é desperdício renderizar?
