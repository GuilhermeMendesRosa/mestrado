# Roteiro de estudo para a prova — P2

Baseado nos tópicos do arquivo `topicos.md`.

**Observação sobre as fontes:**
O livro do Mortenson (Geometric Modeling, 3rd ed.) cobre apenas parcialmente estes tópicos. Os capítulos 10 (Solids: instancing paramétrico, primitivas, sweeps) e 11 (CSG, B-rep) servem de fundação para entender de onde veio o CAD tradicional e por que paramétrico/features foi necessário. O conteúdo sobre troca de dados (IGES, STEP) e features não está no Mortenson — usei conhecimento complementar (padrões ISO, literatura de CAD/CAM) para preencher.

---

# 1. Interoperabilidade e Padrões de Troca de Dados CAD

**Fonte:** Conhecimento complementar (padrões ISO, literatura CAD/CAM). Não está no Mortenson.

## 1.1 Estratégias de Comunicação

### Estudar

- O problema fundamental: N softwares diferentes precisam trocar dados entre si
- **Tradutor direto (point-to-point):** um conversor para cada par de sistemas
  - Se N=10 sistemas, são necessários N*(N-1) = 90 tradutores
  - Vantagem: tradução otimizada para cada par
  - Desvantagem: explosão combinatória, difícil manter quando softwares evoluem
- **Arquivo/interf��cie neutro (neutral file):** cada sistema exporta/importa de um formato comum
  - Apenas 2N conversores (N exportadores + N importadores)
  - Vantagem: escalável, manutenível
  - Desvantagem: arquivo neutro tende a ser maior, pode perder informação específica
- **Trade-off:** tamanho de arquivo vs. escalabilidade e custo de manutenção

### Saber explicar

- Por que a abordagem de arquivo neutro ganhou da abordagem de tradutor direto ao longo do tempo
- O que significa "custo-benefício" na escolha da estratégia de troca
- Por que o arquivo neutro costuma ser maior

## 1.2 Padrões Clássicos e Histórico

### Estudar

- **Programa ICAM (Integrated Computer-Aided Manufacturing):**
  - Programa da Força Aérea dos EUA nos anos 1970
  - Objetivo: integrar design e manufatura de forma computacional
  - Deu origem à necessidade de padrões de troca de dados
- **IGES (Initial Graphics Exchange Specification):**
  - Padrão ANSI desde 1980 (ANSI Y14.26M)
  - Primeiro grande padrão neutro de troca CAD
  - Foco: geometria (curvas, superfícies, wireframe)
  - Limitações: apenas geometria, não captura informação de produto, semântica pobre
  - Ainda usado em alguns contextos legados
- **SET (Standard d'Échange et de Transfert):**
  - Padrão francês, competidor/precursor do STEP
  - Similar ao IGES em escopo
- **VDA-FS (Verband der Automobilindustrie — Flächenschnittstelle):**
  - Padrão da indústria automotiva alemã
  - Foco: troca de dados de superfícies (curvas e superfícies de forma livre)
  - Usado principalmente entre montadoras e fornecedores na Alemanha

### Saber explicar

- Contexto histórico: por que surgiram vários padrões diferentes (automotivo alemão vs. aeroespacial americano vs. francês)
- Limitações comuns dos padrões pré-STEP: foco geométrico, sem semântica de produto

## 1.3 O Padrão STEP (Norma ISO 10303)

### Estudar

- **STEP (STandard for the Exchange of Product model data):**
  - Norma ISO 10303, evolução dos padrões anteriores
  - **DIFERENÇA CRUCIAL PARA O IGES (questão de prova):**
    - IGES troca apenas geometria (formato de desenho)
    - STEP troca informação completa de produto: geometria + estrutura + materiais + tolerâncias + ciclo de vida + manufatura
    - STEP é semanticamente rico; IGES é apenas uma "imagem" matemática do objeto
    - STEP cobre o ciclo de vida completo do produto; IGES cobre só a representação gráfica

- **Arquitetura do STEP (três camadas):**
  1. **Description Methods (Métodos de Descrição):** linguagem EXPRESS, esquemas de modelagem
  2. **Integrated Resources (Recursos Integrados):** bibliotecas reutilizáveis de definições (geometria, topologia, materiais, tolerâncias)
  3. **Application Protocols (Protocolos de Aplicação — APs):** definem o que trocar para cada domínio
     - AP203: Configuration Controlled 3D Design (design mecânico com controle de configuração)
     - AP214: Core Data for Automotive Design (dados automotivos)
     - AP224: Feature-Based Process Planning (planejamento de processo baseado em features)
     - AP242: Managed Model-Based 3D Engineering (sucessor que unifica AP203 e AP214)

- **Linguagem EXPRESS:**
  - Linguagem de modelagem de dados para produto (ISO 10303-11)
  - Orientada a objetos, schema-based
  - Permite definir entidades, atributos, relações, restrições (WHERE rules)
  - Não é uma linguagem de programação — é uma linguagem de especificação de dados
  - EXPRESS-G: notação gráfica da EXPRESS

- **SDAI (Standard Data Access Interface — ISO 10303-22):**
  - API padronizada para acessar dados STEP programaticamente
  - Define operações de leitura, escrita, consulta e manipulação de modelos STEP
  - Permite que aplicações acessem dados STEP sem precisar entender o formato de arquivo físico

### Saber explicar

- Por que STEP é superior ao IGES (além da diferença básica de geometria vs. produto)
- A diferença entre as três camadas da arquitetura STEP
- O que é um Application Protocol e por que existem vários (AP203, AP214, AP242)
- Para que serve a linguagem EXPRESS (e por que não é uma linguagem de programação)
- O papel do SDAI na arquitetura STEP

## 1.4 Modelos de Produto (Product Models)

### Estudar

- **Domínios de um modelo de produto:**
  1. **Domínio Estrutural (Structural):**
     - Estrutura de montagem, BOM (Bill of Materials)
     - Relações pai-filho entre componentes
     - Versões e configurações
  2. **Domínio Geométrico (Geometry):**
     - Forma, dimensões, posição
     - Representação CSG, B-rep, etc.
  3. **Domínio de Conhecimento (Knowledge):**
     - Regras de projeto, restrições, intenções
     - Relacionamentos funcionais
     - Tolerâncias e especificações

- **Integrated Product Model (Modelo de Produto Integrado):**
  - Combina os três domínios em uma representação única e coerente
  - Não é só geometria + anotações; é um modelo computável
  - Permite análise, simulação e validação automáticas
  - É a base sobre a qual o STEP foi construído

### Saber explicar

- Por que não basta armazenar geometria para ter um modelo de produto completo
- O que cada domínio acrescenta que a geometria sozinha não provê
- Como o conceito de Integrated Product Model se relaciona com o STEP

## 1.5 Aplicações na Manufatura

### Estudar

- **Verificação de conformidade:**
  - STEP permite validação automática de que dados estão de acordo com o schema
  - Reduz erros de interpretação humana
  - Benefício: consistência entre sistemas diferentes
- **Integração com NC (Comando Numérico) e CNC:**
  - STEP-NC (ISO 14649): extensão do STEP para comando numérico
  - Em vez de enviar código G (baixo nível), envia informação de features e operações
  - Permite que a máquina CNC "entenda" o que está usinando, não apenas coordenadas
  - Vantagens: interoperabilidade, otimização automática, independência de máquina

### Saber explicar

- O que significa "verificação de conformidade" no contexto do STEP
- A diferença entre código G tradicional e STEP-NC
- Benefícios práticos da integração CAD-CAM via STEP

---

# 2. Modelagem Paramétrica, Variacional e Restrições

**Fonte:** Capítulos 10 e 11 do Mortenson (instancing paramétrico, primitivas, CSG, B-rep) + conhecimento complementar para restrições e sistemas de resolução.

## 2.1 Conceitos Fundamentais

### Estudar

- **Intenção de Projeto (Design Intent):**
  - Conjunto de regras, relações e restrições que capturam o raciocínio do projetista
  - Exemplo: "este furo deve estar sempre centralizado na face, independentemente da largura"
  - Exemplo: "a espessura da parede deve ser sempre ≥ 3 mm"
  - Sem design intent, ao modificar uma cota o modelo "quebra" ou perde coerência
  - Com design intent, o modelo se adapta automaticamente preservando as regras

- **Famílias de Peças (Family of Parts):**
  - Um modelo paramétrico que gera múltiplas variantes alterando parâmetros
  - Exemplo: parafusos M6, M8, M10 — mesmo design, parâmetros diferentes
  - Exemplo: uma família de engrenagens com número de dentes variável
  - Relação com o conceito de instancing do Mortenson (Cap. 10)

- **Modelagem Paramétrica vs. Variacional:**
  - **Paramétrica:** mudanças seguem uma ordem/hierarquia definida (dependências direcionais)
    - Exemplo: "L2 = L1 + 10" — se L1 muda, L2 muda; se L2 muda, L1 não muda
    - Histórico de construção importa
  - **Variacional:** todas as restrições são resolvidas simultaneamente como um sistema
    - Exemplo: "L1 + L2 = 100" e "L1 = 2*L2" são resolvidas juntas
    - Não há direção preferencial; o solver encontra a solução
    - Mais flexível, mas computacionalmente mais caro

### Saber explicar

- O que é design intent e por que é crucial para modelagem paramétrica
- A diferença prática entre paramétrico e variacional (exemplo concreto)
- Como o conceito de family of parts se relaciona com instancing do Mortenson
- Por que um modelo sem design intent se comporta mal quando editado

## 2.2 Tipos de Restrições (Constraints)

### Estudar

- **Restrições Geométricas:**
  - Definem relações espaciais entre entidades geométricas
  - Exemplos: paralelismo, perpendicularidade, tangência, concentricidade, coincidência
  - Restrições dimensionais: distância, ângulo, raio, comprimento fixo
  - São as mais comuns em CAD paramétrico comercial (SolidWorks, Inventor, etc.)

- **Restrições Funcionais (ou de Engenharia):**
  - Relacionadas a requisitos de desempenho do produto
  - Exemplos: tensão máxima admissível (stress ≤ σ_adm), deflexão limite, temperatura, peso máximo, vazão
  - Conectam geometria com análise de engenharia
  - Exemplo: "a área da seção deve ser ≥ X para que a tensão não exceda Y"

- **Restrições Variacionais:**
  - Permitem intervalos de valores (desigualdades) em vez de valores fixos
  - Exemplos: "comprimento entre 50 e 100 mm", "ângulo ≥ 30°"
  - Definem espaço de soluções viáveis, não uma única solução
  - Úteis para otimização e projeto preliminar

### Saber explicar

- A diferença entre os três tipos de restrição com exemplos
- Por que restrições funcionais são mais complexas de implementar que geométricas
- Como restrições variacionais se relacionam com otimização de projeto

## 2.3 Métodos Matemáticos e Computacionais de Resolução

### Estudar

- **Modelos Baseados em Restrições vs. Métodos Procedurais:**
  - **Procedural:** define passo a passo como construir a geometria (sequência fixa)
    - Exemplo: "desenhe um retângulo, depois faça um furo a 10 mm da borda"
    - Parecido com programação imperativa
  - **Baseado em restrições:** declara o que se deseja, não como construir
    - Exemplo: "existe um retângulo e um furo; o centro do furo está a 10 mm da borda"
    - Parecido com programação declarativa
    - O solver encontra a solução que satisfaz todas as restrições

- **Uso de Grafos e Predicados:**
  - Elementos geométricos são nós do grafo
  - Restrições são arestas que conectam os nós
  - Exemplo: linha L1 (nó) —[paralelo]— linha L2 (nó) —[distância=50]— linha L3 (nó)
  - **Predicado:** condição lógica que deve ser verdadeira (ex: "a distância entre P1 e P2 é d")
  - Grafos permitem: análise de dependências, detecção de restrições redundantes ou contraditórias, ordenação de resolução

- **Sistemas de Equações Simultâneas:**
  - Cada restrição gera uma ou mais equações
  - Conjunto de equações é resolvido simultaneamente
  - Métodos numéricos comuns: Newton-Raphson, métodos de otimização
  - Desafios: múltiplas soluções, convergência, restrições redundantes ou inconsistentes
  - Sistemas sub-restritos (under-constrained): mais incógnitas que equações → infinitas soluções
  - Sistemas sobre-restritos (over-constrained): mais equações que incógnitas → pode não ter solução

- **Função Implícita:**
  - Forma F(x, y, z, ...) = 0
  - Define relação sem isolar uma variável
  - Exemplo: x² + y² - R² = 0 (círculo, sem isolar y)
  - Vantagem: pode representar relações que não têm forma explícita
  - Desvantagem: mais difícil de avaliar e manipular computacionalmente
  - Relação com restrições: uma restrição pode ser expressa como F(...) = 0

### Saber explicar

- A diferença conceitual entre procedural e declarativo (baseado em restrições)
- Como um grafo de restrições ajuda a resolver o sistema
- O que são sistemas sub-restritos e sobre-restritos e suas consequências práticas
- Quando usar função implícita em vez de explícita

---

# 3. Modelagem Avançada CAD e Baseada em Feições (Features)

**Fonte:** Capítulo 11 do Mortenson (CSG, B-rep e suas limitações como "CAD tradicional") + conhecimento complementar para classificação de features.

## 3.1 Deficiências do CAD Tradicional

### Estudar

- **Contexto:** O CAD tradicional (CSG, B-rep puro) opera com entidades geométricas de baixo nível, herdadas das limitações discutidas ao longo do Mortenson.

- **"Dados microscópicos" e sub-especificação geométrica:**
  - Trabalha com pontos, linhas, arestas, faces — elementos sem significado de engenharia
  - Um furo é representado como um conjunto de faces cilíndricas, não como "furo passante M8"
  - A geometria existe, mas o significado não
  - Sub-especificação: a geometria pode estar correta, mas sem informação suficiente para manufatura

- **Falta de intenção de projeto na estrutura de dados:**
  - O modelo armazena "o quê" (geometria), mas não "por quê" (razão de ser)
  - Se um engenheiro vê um furo, não sabe se é para parafuso, pino, passagem de fluido, alívio de peso
  - Manufatura e análise não conseguem extrair automaticamente o significado

- **Construção tediosa para o usuário:**
  - Cada aresta, face e vértice precisa ser definido explicitamente
  - Operações booleanas complexas exigem muitos passos
  - Modificar um detalhe pode exigir reconstruir grande parte do modelo

- **Estrutura de dados de um único nível:**
  - Não há hierarquia de features, agrupamentos ou relações
  - Tudo está no mesmo plano (flat structure)
  - Dificulta navegação, modificação e reuso

### Saber explicar

- Por que "dados microscópicos" são um problema para além do desenho
- A diferença entre ter a geometria e ter o significado da geometria
- Como as deficiências do CAD tradicional motivaram a modelagem por features
- Relacionar com o que foi visto na P1 sobre limitações do wireframe e CSG/B-rep puros

## 3.2 Feições Geométricas (Features)

### Estudar

- **Definição de Feature:**
  - Elemento geométrico que carrega significado de engenharia
  - Agrega geometria + semântica + comportamento
  - Exemplo: um "furo passante" é geometria (cilindro) + semântica ("passante", "para fixação") + comportamento (como se comporta quando a peça muda)

- **Classificação Física vs. Abstrata:**
  - **Features Físicas (Physical/Concrete Features):**
    - Correspondem a geometria real na peça
    - Exemplos: furo (hole), cavidade (pocket), rasgo (slot), ressalto (boss), nervura (rib), chanfro (chamfer), arredondamento (fillet)
    - Visíveis e mensuráveis no modelo 3D
  - **Features Abstratas (Abstract Features):**
    - Não têm representação geométrica direta
    - Exemplos: tolerância dimensional, acabamento superficial, especificação de material, tratamento térmico, notas de fabricação
    - Informação anexada ao modelo, mas não visível como geometria

- **Classificação de Aplicação — Form Features vs. Manufacturing Features:**
  - **Form Features (Feições de Forma):**
    - Orientadas ao design/projeto
    - Descrevem a forma funcional da peça como o projetista a concebe
    - Exemplo: um "ressalto" (boss) é uma feature de forma — o projetista pensa "aqui vai um ressalto para apoiar o mancal"
  - **Manufacturing Features (Feições de Manufatura):**
    - Orientadas ao processo de fabricação
    - A mesma geometria pode ser uma feature diferente dependendo do processo
    - Exemplo: um "ressalto" no design pode ser uma "cavidade a ser fresada" na manufatura (porque o que se remove é o material ao redor)
    - Exemplo: um furo passante pode ser "furo a ser broqueado" ou "furo a ser mandrilhado", dependendo da precisão
  - **Problema do mapeamento Design ↔ Manufatura:** nem sempre há correspondência 1:1

- **Tipologia Geométrica — Features Rotacionais vs. Prismáticas:**
  - **Features Rotacionais:**
    - Associadas a peças torneadas (eixo de simetria)
    - Geradas por revolução de um perfil 2D
    - Exemplos: cilindro externo, cone, ressalto torneado, canal para anel de retenção
    - Usinagem típica: torno
  - **Features Prismáticas:**
    - Associadas a peças fresadas (faces planas, geometria prismática)
    - Definidas por faces planas ortogonais ou inclinadas
    - Exemplos: cavidade retangular, rasgo, face rebaixada (step), furo
    - Usinagem típica: fresadora, centro de usinagem
  - Uma peça pode conter ambas (ex: eixo com rasgo de chaveta = rotacional + prismática)

- **Feature Recognition vs. Feature-Based Design:**
  - **Feature Recognition:** parte de um modelo geométrico (B-rep) e identifica features automaticamente
    - Desafio: features podem se intersectar e ficar difíceis de reconhecer
  - **Feature-Based Design (Design by Features):** o projetista constrói o modelo usando features desde o início
    - Cada feature é uma operação com significado
    - Vantagem: intenção de projeto é capturada naturalmente

### Saber explicar

- A diferença entre feature física e abstrata com exemplos concretos
- Por que uma mesma geometria pode ser uma form feature e uma manufacturing feature diferente
- A diferença entre feature recognition e feature-based design
- Como classificar uma peça entre rotacional e prismática (critérios)
- Por que o mapeamento entre features de design e de manufatura não é trivial

## 3.3 Definições, Taxonomias e Representação de Features (Slide 18)

### Estudar

- **Definições históricas de features:**
  - Grayer (1976): "característica geométrica que corresponde a uma operação de usinagem"
  - Pratt (1985): "região de interesse na superfície da peça"
  - Lenau (1993): "conjuntos de informações que referem-se a aspectos de forma ou outro atributo"
  - Henderson (1990): "padrões geométrico/topológicos interessantes de alto nível"
  - Por que não há definição única (Pratt93): diversidade de usos, produtos, métodos e filosofias

- **Features Abstratas — subtipos:**
  - Estruturais: relacionamentos entre features (precedência, conectividade, simetria)
  - Físicas: fenômenos físicos e elementos mecânicos (cunha, alavanca)
  - Precisão: tolerâncias, acabamento superficial, circularidade, planicidade
  - Material: rigidez, elasticidade, durabilidade

- **Taxonomias de Form Features:**
  - **Pratt:** ThroughHole, Depression (rotational/prismatic), Protrusion (rotational/prismatic), Area, Other
  - **Gindy:** classificação por EAD's (External Access Directions); 0 a 5 EAD's; subdivisão em Quadrangular e Cylindrical
  - **Hounsell (1998):** tabela bilíngue Pocket/Reentrância, Hole/Furo, Slot/Canal Cego, Step/Degrau, Notch/Entalhe, Boss/Protuberância, etc.

- **4 Formas de representar features:**
  1. B-rep ou CSG puros
  2. Simplificações (ex: DSG — apenas diferença)
  3. Híbridos B-rep + CSG (redundância como desvantagem)
  4. Melhoramentos adaptados para features

- **DSG (Destructive Solid Geometry):** CSG apenas com operador de diferença

- **Tipos de sistemas de features:**
  - FeR (Feature Recognition): pós-processamento, aproveita legado, mas lento e limitado
  - DbF (Design-by-Features): captura Design Intent, mas limitado a features pré-definidas
  - Híbridos: 4 formas de integrar FeR em DbF

### Saber explicar

- Por que não existe uma definição única de feature
- A diferença entre features abstratas estruturais, físicas, de precisão e de material
- Como a taxonomia de Gindy (EAD's) conecta geometria com manufaturabilidade
- O que é DSG e como ela simplifica a representação de features
- Vantagens e desvantagens de FeR vs. DbF

## 3.4 Problemas de Validação em Features (Slide 19)

### Estudar

- **Motivação:** "Mesmo sendo uma tecnologia promissora, ainda é muito imatura" (Hounsell/Rosso)

- **Interações entre Features:**
  - Adjacência (encostadas)
  - Compartilhamento de faces/arestas
  - Cruzamento (interseção)
  - Sobreposição (mesmo volume)

- **Thin Walls (Paredes Finas):**
  - Feature-to-Feature
  - Feature-to-STOCK
  - Casos adjacentes (Adjoint)
  - Casos disjuntos (Disjoint)

- **8 Problemas de Edição:**
  1. Remoção ≠ reinserção de volume
  2. Desconexão de feature por edição de parâmetros
  3. Colisão ou redundância entre features
  4. Cobertura ou fechamento (feature "tampada")
  5. Absorção de intenções de projeto
  6. Apagamento de intenções por modificação de valores
  7. Alterações geométricas implícitas
  8. Invalidação total por inserção de nova feature

- **Fatores simultâneos de validação:** renomeação, união de intenções, reparametrização

- **Validação Geométrica vs. Validação Semântica:**
  - Geométrica: homogeneidade dimensional, fronteiras, auto-interseções
  - Semântica: preservação das intenções de projeto
  - Operações semânticas: Split, Delete, Merge, Label

- **Changeability:** uma feature deve, de alguma forma, mudar a geometria/topologia do modelo

### Saber explicar

- Por que boss e slot têm a mesma topologia e por que isso dificulta FeR
- Os 4 tipos de interação entre features com exemplos
- Por que Thin Walls são um problema de manufaturabilidade
- Pelo menos 4 dos 8 problemas de edição, com exemplos
- A diferença entre validação geométrica e validação semântica
- O que significa "a tecnologia de features ainda é imatura"

---

# 4. Representação por Decomposição e Estruturas de Dados Espaciais

**Fonte:** Slides 13 e 13a do professor + Mortenson Capítulo 11.

## 4.1 Representação por Decomposição (Slide 13)

### Estudar

- **Conceito:** subdividir o espaço em família de células volumétricas; objeto = enumeração das células que o intersectam

- **Duas formas:**
  - **Uniforme (Matricial/Voxels):** reticulado regular, células de mesmo tamanho
  - **Não-Uniforme:** tamanho variável (Quadtree, Octree, BSP-tree) ou forma variável (Voronoi, células quaisquer)

- **Voxels (Representação Matricial):**
  - Extensão 3D da representação matricial 2D (pixel → voxel)
  - Características: tem unicidade, não-ambígua, fácil validar, precisão depende do tamanho, **não é concisa**
  - Operações booleanas em domínio inteiro (muito simples)
  - Também chamada de representação volumétrica (imagem 3D)
  - Vantagens: técnicas de processamento de imagens, visualização simples, usada em equipamentos de captura

- **Decomposição Celular (células quaisquer):**
  - Não tem unicidade, é exata mas não concisa
  - Domínio restrito (depende das células disponíveis)
  - Difícil validar (colagens geram interseção?)

- **Quadtree (2D) e Octree (3D):**
  - Estruturas hierárquicas, decomposição recursiva
  - Cada nó gera 2^d filhos (d=2: Quadtree, d=3: Octree)
  - Estados: Empty (vazio), Full (cheio), Partial (parcial → subdivide)
  - Vantagens: simplificam interseção, localização, remoção de superfícies
  - Acesso O(log n); estrutura estática (difícil mover elementos)

- **BSP-tree (Binary Space Partitioning):**
  - Árvore binária, divide espaço em 2 partes por plano de corte
  - Axis-Aligned (planos paralelos aos eixos) e Polygon-Aligned (polígono define plano)
  - Representa côncavos e convexos; potencialmente não compacta
  - Lado direito = fora, lado esquerdo = dentro

- **Conversão entre representações:**

  | Conversão | Dificuldade |
  |-----------|-------------|
  | CSG → B-rep | Possível |
  | B-rep → CSG | Muito mais complicada |
  | B-rep → Células | Simples |
  | Células → B-rep | Relativamente simples (marching cubes) |
  | CSG → Células | Simples |
  | Células → CSG | Complicado |

### Saber explicar

- A diferença entre decomposição uniforme e não-uniforme
- Por que voxels "não são concisos" e quando isso é um problema
- Como funciona a subdivisão recursiva em Quadtree/Octree
- A diferença entre Axis-Aligned e Polygon-Aligned BSP-tree
- Quais conversões entre representações são viáveis e quais são difíceis
- Por que o método de modelagem (interface) não restringe a representação interna

## 4.2 Estruturas de Dados Espaciais (Slide 13a)

### Estudar

- **Malha de Triângulos:** rede de triângulos conectados por compartilhamento de arestas e vértices
  - Lista de triângulos desconectados **não** é uma malha

- **Manifold:**
  - Vizinhança de qualquer ponto é "achatável" em superfície plana
  - Verificação: toda aresta compartilhada por exatamente 2 triângulos; todo vértice tem círculo completo de triângulos
  - Manifold não garante orientação consistente das faces

- **Winged-Edge:**
  - Armazena conectividade nas arestas (2 faces, 2 vértices, 4 arestas vizinhas)
  - Acesso O(1) para arestas de face/vértice
  - Sempre verifica orientação antes de navegar

- **Half-Edge:**
  - Cada aresta dividida em 2 metades com orientações opostas
  - Elimina necessidade de verificar orientação
  - Cada half-edge: vértice origem, half-edge oposta (pair), face, next, prev

- **MX Quadtree:** para pontos discretos, posição implícita na árvore, folha = preto ou branco
- **PR Quadtree:** armazena coordenadas, máximo 1 ponto por folha

- **Extended Octree:** folhas armazenam polígonos para representar superfícies
- **Graftree:** folhas armazenam raiz de árvore CSG; estados: FULL, EMPTY, BOUNDARY

- **KD-Tree:**
  - Tipo especial de BSP para pontos; cada nível divide em uma dimensão
  - Busca/inserção/remoção: O(log n) médio, O(n) pior caso
  - Ordem de inserção afeta balanceamento

- **BVH (Bounding Volume Hierarchy):**
  - Organiza bounding volumes (esferas, AABB) em árvore
  - BVH agrupa por proximidade; Octree subdivide espaço uniformemente

### Saber explicar

- A diferença entre Winged-Edge e Half-Edge (e por que Half-Edge é mais elegante)
- Como verificar se uma malha é manifold
- O que é uma MX Quadtree e qual sua principal limitação (dobrar precisão = 2^d × memória)
- A diferença entre Extended Octree e Graftree
- Como uma KD-Tree organiza pontos e por que a ordem de inserção importa
- BVH vs. Octree: quando usar cada uma

---

# 5. Otimização de Modelos — LOD (Level of Detail)

**Fonte:** Slide 14 do professor.

## 5.1 Conceito e Implementação

### Estudar

- **Motivação:** é custoso mostrar objeto completo sempre com maior detalhe; quanto mais longe, menos detalhes necessários

- **Solução LOD:** criar múltiplos níveis de detalhe do mesmo modelo

- **Critério de troca:** baseado em distância e resolução da tela
  - Exemplo: tela 640×480 = 307K pixels; objeto ocupa metade → ~150K pixels
  - Mais que ~300K triângulos é desperdício (metade está em back-face)

- **Questões práticas:**
  - Como criar múltiplos níveis? (simplificação de malha)
  - Quando trocar? (distância + resolução)
  - Artefatos visuais (popping) nos pontos de troca

### Saber explicar

- Por que existe um limite de triângulos além do qual é desperdício
- Como decidir quando trocar de LOD
- O que são artefatos de popping e por que ocorrem
