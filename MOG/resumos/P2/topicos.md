# 1. Interoperabilidade e Padrões de Troca de Dados CAD

*(Baseado nas anotações de 27/05 e 03/06)*

Este bloco trata de como diferentes softwares conversam entre si e como as informações de projeto e manufatura são armazenadas e transportadas.

## Estratégias de Comunicação

- O objetivo é a troca de arquivos de manufatura com o melhor custo-benefício para transportar dados entre aplicativos.
- Duas opções principais: Usar um tradutor direto ou usar uma interface/arquivo neutro.
- **Trade-off**: O arquivo neutro costuma ser muito maior em tamanho.

## Padrões Clássicos e Histórico

- Programa ICAM (Integrated Computer-Aided Manufacturing).
- Padrões de mercado: IGES, SET, VDA-FS.

## O Padrão STEP (Norma ISO 10303)

- **Atenção (Questão de Prova)**: Qual a diferença do STEP para o IGES?
- Arquitetura do STEP: Protocolos STEP, Description Methods (métodos de descrição), Integrated Resources (recursos integrados).
- Linguagem e Acesso: EXPRESS Language e SDAI (Standard Data Access Interface).

## Modelos de Produto (Product Models)

- Divisão em domínios: Estrutural (Structural), Geometria (Geometry), Conhecimento (Knowledge), resultando em Integrated Product Models.

## Aplicações na Manufatura

- Benefícios advindos da verificação de conformidade.
- Integração com NC (Comando Numérico) e CNC.

---

# 2. Modelagem Paramétrica, Variacional e Restrições

*(Baseado nas anotações de 10/06 e início da página sem data)*

Aqui o foco muda da troca de arquivos para a lógica de construção do modelo e como o software entende as regras do seu projeto.

## Conceitos Fundamentais

- Intenção de Projeto (Design Intent).
- Criação de Famílias de Peças.

## Tipos de Restrições (Constraints)

- Restrições Geométricas.
- Restrições Funcionais (ex: stress, fluência).
- Restrições Variacionais.

## Métodos Matemáticos e Computacionais de Resolução

- Modelos baseados a restrições vs. Métodos procedurais.
- Uso de Grafos e Predicados.
- Sistemas de Equações Simultâneas.
- Função Implícita.

---

# 3. Modelagem Avançada CAD e Baseada em Feições (Features)

*(Baseado nas anotações da página sem data)*

*(Baseado nas anotações da página sem data e slides 18-19)*

Este bloco aborda as limitações dos sistemas CAD mais antigos e a evolução para a modelagem orientada a features, incluindo os problemas de validação.

## Deficiências do CAD Tradicional

- Utiliza "dados microscópicos" (linhas, pontos) que levam à sub-especificação geométrica.
- Faltam as intenções de projeto na estrutura de dados.
- Construção tediosa para o usuário.
- A estrutura de dados é de um único nível.
- **Solução**: Tecnologia de Feições Geométricas como entidades macroscópicas e modelagem em alto nível.

## Definições e Significado de Features

- Definições históricas: Grayer (1976) — "característica geométrica que corresponde a uma operação de usinagem"; Pratt (1985); Lenau (1993); Henderson (1990).
- Features como padrões geométrico/topológicos de alto nível.
- Features carregam informações implícitas e explícitas sobre transformações do produto (Case92a).
- Dificuldade de definição única devido à diversidade de modos de uso (Pratt93).

## Classificações de Features

- **Física/Abstrata**: Features Físicas vs. Features Abstratas (Estruturais, Físicas, Precisão, Material, Geométricas).
- **Orientação**: Features de Projeto (alto nível) vs. Features de Aplicação (manufatura, fixação, datum, montagem, tecnológica, inspeção).
- **Form Features**: Prismáticas vs. Rotacionais vs. Chapas vs. Injeção/Molde.
- **Taxonomias**: Pratt, Gindy (baseada em EAD's — External Access Directions), Hounsell (1998).

## Representação de Features

- 4 formas: B-rep/CSG puros, simplificações (DSG), híbridos (B-rep + CSG), melhoramentos.
- DSG (Destructive Solid Geometry): CSG apenas com operador de diferença.
- Esquemas híbridos oferecem melhor opção, com desvantagem da redundância.

## Tipos de Sistemas de Features

- **Feature Recognition (FeR)**: reconhece features a partir de modelo geométrico pronto. Vantagens: aproveita legado, integração CAD-CAPP-CAM. Desvantagens: hard-coded, lento, limitado a features pré-definidas, redundante (dupla tradução).
- **Design-by-Features (DbF)**: constrói modelo usando features desde o início. Vantagens: captura Design Intent, linguagem natural, facilita padronização. Desvantagens: limitado a features pré-definidas, interações comprometem validade, perda de liberdade.
- **Sistemas Híbridos**: combinam FeR e DbF. 4 formas de integrar FeR em DbF: (1) converter arquivos legados, (2) validação, (3) resolver interações, (4) conversão para espaços de aplicação.

## Problemas de Validação em Features (DbF)

- **Interações entre Features**: adjacência, compartilhamento de faces/arestas, cruzamento, sobreposição.
- **Paredes Finas (Thin Walls)**: Feature-to-Feature, Feature-to-STOCK, casos adjacentes e disjuntos.
- **8 Problemas de Edição**: remoção ≠ reinserção de volume, desconexão, colisão/redundância, cobertura/fechamento, absorção de intenções, apagamento de intenções, alterações implícitas, invalidação por inserção.
- **Fatores de validação simultâneos**: renomeação, união de intenções, reparametrização.
- **Validação Geométrica** vs. **Validação Semântica** (operações split, delete, merge, label).

---

# 4. Representação por Decomposição e Estruturas de Dados Espaciais

*(Baseado nos slides 13 e 13a)*

Este bloco aborda métodos alternativos de representação de sólidos e as estruturas de dados usadas para organizar informação espacial.

## Representação por Decomposição do Espaço

- Subdivide o espaço em família de células volumétricas; o objeto é representado pela enumeração das células que o intersectam.
- Duas formas: **Uniforme** (matricial/voxels) e **Não-Uniforme** (quadtree, octree, BSP-tree, Voronoi).

### Representação Matricial (Voxels)

- Extensão 3D da representação matricial 2D (pixel → voxel).
- Reticulado uniforme via produto cartesiano de partições dos eixos.
- Características: unicidade, não-ambígua, fácil validar, precisão depende do tamanho do voxel, **não é concisa**.
- Operações booleanas regularizadas em domínio inteiro (simples).
- Também chamada de representação volumétrica (imagem 3D).
- Vantagens: técnicas de processamento de imagens aplicáveis, visualização simples, usada em equipamentos de captura volumétrica.

### Decomposição Não-Uniforme

- Células com tamanho e/ou geometria variáveis.
- **Variação de tamanho**: Quadtree (2D), Octree (3D), BSP-tree.
- **Variação de forma**: Diagramas de Voronoi, células quaisquer.
- Células quaisquer: não têm unicidade, domínio restrito, difícil validar colagens.

### Quadtree e Octree

- Estruturas de dados hierárquicas, espacialmente endereçáveis, naturalmente pré-ordenadas.
- Decomposição recursiva: cada nó gera 2^d filhos (d=2 para Quadtree, d=3 para Octree).
- Nós: Empty (vazio), Full (cheio), Partial (parcial — subdivide).
- Vantagens: simplificam detecção de interseção, localização espacial, remoção de superfícies escondidas.
- Acesso em O(log n). Estrutura estática (difícil mover elementos).
- **MX Quadtree**: para pontos discretos, cada folha é preto (dado) ou branco (vazio). Posição implícita na árvore.
- **PR Quadtree**: similar à MX, mas armazena coordenadas. Máximo 1 ponto por folha.
- **Extended Octree**: armazena polígonos nas folhas para representar superfícies de sólidos.
- **Graftree**: folhas armazenam raiz de árvore CSG; permite operações booleanas locais.

### BSP-tree (Binary Space Partitioning)

- Árvore binária que divide o espaço recursivamente em 2 partes por um plano de corte.
- Dois tipos: **Axis-Aligned** (planos paralelos aos eixos) e **Polygon-Aligned** (polígono 3D define o plano).
- Lado direito da árvore = fora do objeto; lado esquerdo = dentro do objeto.
- Representa côncavos e convexos. Potencialmente não compacta.
- Polygon-Aligned: escolha do polígono divisor afeta balanceamento e número de splits.

### Conversão entre Representações

- CSG → B-rep: Possível.
- B-rep → CSG: Muito mais complicada.
- B-rep → Células: Simples.
- Células → B-rep: Relativamente simples (marching cubes).
- CSG → Células: Simples.
- Células → CSG: Complicado.
- O método de modelagem (interface) não restringe a representação interna.

## Estruturas de Dados para Malhas (Winged-Edge e Half-Edge)

- **Winged-Edge**: armazena conectividade nas arestas (2 faces, 2 vértices, 4 arestas vizinhas). Acesso O(1) para arestas de face/vértice. Sempre verifica orientação.
- **Half-Edge**: cada aresta dividida em 2 metades com orientações opostas. Elimina verificação de orientação.
- **Manifold**: superfície onde vizinhança de qualquer ponto é "achatável". Verificação: toda aresta compartilhada por exatamente 2 triângulos; todo vértice tem círculo completo de triângulos. Manifold não garante orientação consistente.

## Outras Estruturas Espaciais

- **Grid (matriz 3D)**: acesso O(1), alto consumo de memória, não se adapta a complexidade variável.
- **KD-Tree**: tipo especial de BSP para organização de pontos. Cada nível divide em uma dimensão. Suporta k dimensões. Busca/inserção/remoção O(log n) médio, O(n) pior caso.
- **BVH (Bounding Volume Hierarchy)**: organiza bounding volumes (esferas, AABB) em árvore. Nó pai contém objetos dos filhos. Comparação BVH vs. Octree: BVH agrupa por proximidade; Octree subdivide espaço uniformemente.

---

# 5. Otimização de Modelos — LOD (Level of Detail)

*(Baseado no slide 14)*

## Conceito

- É muito custoso mostrar objeto completo sempre com maior nível de detalhes.
- Quanto mais longe do objeto, menos detalhes são necessários (depende também de ângulo de visão e resolução da tela).
- Solução: criar múltiplos níveis de detalhe do mesmo modelo e usar o adequado à distância.

## Implementação

- Criar o mesmo modelo em múltiplos níveis de detalhe (ex: 50, 500, 2000 vértices).
- Troca de LOD baseada em distância e resolução da tela.
- Relação triângulos vs. pixels: se o objeto ocupa metade de uma tela 640×480 (~150K pixels), mais que ~300K triângulos é desperdício.
- Artefatos visuais podem ocorrer nos pontos de troca.
