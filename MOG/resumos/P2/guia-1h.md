# Guia de Estudo — 60 minutos (P2)

**Premissa:** Você já domina o Dia 1 (Interoperabilidade/STEP). Este guia cobre os blocos 2 a 5 com foco no que cai na prova. Siga os tempos sugeridos.

---

## 0–15 min | Bloco 2: Modelagem Paramétrica, Variacional e Restrições

### Design Intent (certo de cair)
- **Definição:** conjunto de regras, relações e restrições que capturam o raciocínio do projetista no modelo
- **Exemplo:** "os furos devem estar sempre centralizados na face, independente da largura"; "espessura ≥ 3 mm"
- **Sem Design Intent** → ao mudar uma cota o modelo "quebra"
- **Com Design Intent** → o modelo se adapta automaticamente

### Paramétrico vs. Variacional (questão clássica de prova)
| Paramétrico | Variacional |
|---|---|
| Dependências **direcionais** (hierarquia) | Todas equações resolvidas **simultaneamente** |
| L2 = L1 + 10 → L1 determina L2, não o contrário | L1 + L2 = 100 e L1 = 2*L2 → resolvidas juntas |
| Ordem de construção importa | Não há direção preferencial |
| Mais simples, mais rápido | Mais flexível, mais caro computacionalmente |

### 3 Tipos de Restrições
| Tipo | O que define | Exemplo |
|---|---|---|
| **Geométrica** | Relações espaciais | paralelismo, tangência, concentricidade, distância fixa |
| **Funcional (engenharia)** | Requisitos de desempenho | tensão ≤ σ_adm, peso ≤ 5 kg, deflexão ≤ 1 mm |
| **Variacional** | Intervalos (desigualdades) | 50 ≤ comprimento ≤ 100 mm |

### Métodos de Resolução
- **Procedural:** sequência fixa de passos (como programação imperativa) — "faça isso, depois isso"
- **Baseado em restrições:** declara o que quer, solver resolve (como programação declarativa)
- **Grafo de restrições:** elementos geométricos = nós, restrições = arestas
- **Predicado:** condição lógica que deve ser verdadeira (ex: "distância(P1,P2) = d")
- **Função implícita:** F(x,y,z) = 0 — define relação sem isolar variável (ex: x²+y²-R²=0)

### Under vs. Over-constrained
- **Under-constrained:** mais variáveis que equações → **infinitas soluções** → geometria "flutua"
- **Over-constrained:** mais equações que variáveis → pode ser **impossível** → restrições conflitantes

### Family of Parts
- Um modelo paramétrico → múltiplas variantes mudando parâmetros (ex: parafusos M6, M8, M10)
- Relaciona com instancing do Mortenson: reutilizar definição base com parâmetros diferentes

---

## 15–35 min | Bloco 3: Features e Validação (mais pesado, mais provável)

### 4 Deficiências do CAD Tradicional
1. **Dados microscópicos:** opera com pontos/linhas/faces sem significado — um furo é só faces cilíndricas
2. **Sub-especificação geométrica:** geometria existe mas falta informação para manufatura/análise
3. **Construção tediosa:** cada elemento definido manualmente; modificar = reconstruir
4. **Estrutura plana (single-level):** sem hierarquia, agrupamento ou relações

### O que é uma Feature
> **Geometria + Semântica + Comportamento.** Ex: "furo passante M8" = cilindro (geometria) + "passante, para fixação M8" (semântica) + atravessa a peça, atualiza-se parametricamente (comportamento).

### Classificações (saiba o conceito, não decore nome)

**Física vs. Abstrata:**
- **Física:** tem geometria visível (furo, cavidade, rasgo, ressalto, chanfro)
- **Abstrata:** sem geometria direta (tolerância, acabamento superficial, material, tratamento térmico)

**Form Features vs. Manufacturing Features:**
- **Form:** visão do projetista (ex: "ressalto para apoiar mancal")
- **Manufacturing:** visão da fabricação (ex: o mesmo ressalto = "material a remover ao redor")
- **Não há mapeamento 1:1** entre elas

**Rotacional vs. Prismática:**
- **Rotacional:** simetria axial, gerada por revolução, usinada em torno (ex: eixo, cilindro, cone)
- **Prismática:** faces planas, usinada em fresadora (ex: cavidade, rasgo, degrau)
- Peça pode ser híbrida (ex: eixo com rasgo de chaveta)

### Feature Recognition (FeR) vs. Design by Features (DbF)
| | FeR | DbF |
|---|---|---|
| **Como funciona** | Analisa B-rep pronto e identifica features | Constrói com features desde o início |
| **Vantagem** | Aproveita legado | Captura Design Intent naturalmente |
| **Desvantagem** | Lento, ambíguo, limitado a features pré-definidas | Limitado a features pré-definidas, perda de liberdade |

### DSG (Destructive Solid Geometry)
- CSG **apenas com operador de diferença** (subtração)
- Natural para usinagem: sempre se remove material do blank

### Taxonomia de Gindy — EAD's
- **EAD = External Access Direction** — direção pela qual ferramenta acessa a feature
- Varia de 0 a 5 EAD's; subdivide em Quadrangular e Cylindrical
- **Exemplos:** Pocket fechado = 0 EAD's, Slot passante = 1 EAD, Step = 2 EAD's

### 4 Tipos de Interação entre Features
1. **Adjacência** — encostadas (furo com rebaixo encostado)
2. **Compartilhamento** — dividem face/aresta (duas cavidades com parede comum)
3. **Cruzamento** — interseção (furo atravessando cavidade)
4. **Sobreposição** — mesmo volume (dois furos parcialmente sobrepostos)

### Thin Walls (paredes finas)
- Features muito próximas → parede fina demais para fabricação
- 4 casos: Feature-to-Feature, Feature-to-STOCK, Adjoint, Disjoint

### 8 Problemas de Edição (saiba citar pelo menos 4)
1. Remoção ≠ reinserção de volume (deixa "cicatrizes" topológicas)
2. Desconexão por edição de parâmetros
3. Colisão ou redundância entre features
4. Cobertura/fechamento (feature "tampada" por outra)
5. Absorção de intenções de projeto
6. Apagamento de intenções por modificação
7. Alterações geométricas implícitas
8. Invalidação total por inserção de nova feature

### Validação Geométrica vs. Semântica
- **Geométrica:** modelo matematicamente válido? (sem auto-interseção, fronteiras ok)
- **Semântica:** intenções de projeto preservadas? (features mantêm significado após edições)
- **Operações semânticas:** Split, Delete, Merge, Label
- Um modelo pode ser geometricamente válido mas semanticamente inválido

### Frase do slide: "a tecnologia de features ainda é muito imatura" (Hounsell/Rosso)

---

## 35–50 min | Bloco 4: Decomposição Espacial e Estruturas de Dados

### Representação por Decomposição
**Conceito:** subdivide o espaço em células volumétricas; objeto = células que o intersectam.

```
Decomposição
├── UNIFORME → Voxels (reticulado regular, células iguais)
└── NÃO-UNIFORME
    ├── Tamanho variável: Quadtree, Octree, BSP-tree
    └── Forma variável: Voronoi, células quaisquer
```

### Voxels (Representação Matricial)
- Pixel 2D → Voxel 3D
- **Características-chave:** unicidade ✓, não-ambíguo ✓, fácil validar ✓, **NÃO é conciso** ✗
- Operações booleanas em domínio inteiro = muito simples
- Também chamada de representação volumétrica / imagem 3D

### Quadtree (2D) e Octree (3D)
- Estrutura **hierárquica**, decomposição recursiva
- 2^d filhos: Quadtree = 4, Octree = 8
- Estados: **Empty** (vazio), **Full** (cheio), **Partial** (parcial → subdivide)
- Acesso **O(log n)**
- **Estática:** difícil mover elementos (melhor recriar que transformar)

### MX Quadtree vs. PR Quadtree
| MX Quadtree | PR Quadtree |
|---|---|
| Posição implícita na árvore | Armazena coordenadas |
| Folha = preto (dado) ou branco (vazio) | Máximo 1 ponto por folha |
| Dobrar precisão = 4× memória (2D) | |

### BSP-tree (Binary Space Partitioning)
- **Árvore binária**, divide espaço em 2 por plano de corte
- **Axis-Aligned:** planos paralelos aos eixos (xy, xz, yz)
- **Polygon-Aligned:** polígono 3D define o plano
- Lado direito = fora, lado esquerdo = dentro
- Representa côncavos e convexos; potencialmente não compacta

### Conversão entre Representações (tabela — decore)
| Conversão | Dificuldade |
|---|---|
| CSG → B-rep | Possível |
| B-rep → CSG | **Muito mais complicada** |
| B-rep → Células | Simples |
| Células → B-rep | Relativamente simples (marching cubes) |
| CSG → Células | Simples |
| Células → CSG | Complicado |
> **Importante:** o método de modelagem (interface) NÃO restringe a representação interna.

### Winged-Edge vs. Half-Edge
| Winged-Edge | Half-Edge |
|---|---|
| 2 faces + 2 vértices + 4 arestas vizinhas por aresta | Cada aresta = 2 metades com orientações opostas |
| Sempre verifica orientação antes de navegar | **Elimina** verificação de orientação |
| | Cada half-edge: vértice origem, pair, face, next, prev |

### Manifold
- Vizinhança de qualquer ponto é "achatável" em superfície plana
- **Verificação:** toda aresta = exatamente 2 triângulos; todo vértice = círculo completo de triângulos
- Manifold **não garante** orientação consistente

### KD-Tree
- BSP especial para pontos; cada nível divide em 1 dimensão
- O(log n) médio, O(n) pior caso
- Ordem de inserção afeta balanceamento

### BVH vs. Octree
| BVH | Octree |
|---|---|
| Agrupa objetos por **proximidade** | Subdivide espaço **uniformemente** |
| Adapta-se à distribuição dos objetos | Estrutura previsível, independente dos objetos |

### Extended Octree vs. Graftree
- **Extended Octree:** folhas armazenam polígonos (superfícies)
- **Graftree:** folhas armazenam raiz de árvore CSG; estados: FULL, EMPTY, BOUNDARY

---

## 50–55 min | Bloco 5: LOD (Level of Detail)

- **Motivação:** custoso renderizar objeto completo com detalhe máximo; quanto mais longe, menos detalhes necessários
- **Solução:** criar múltiplos níveis (ex: 50, 500, 2000 vértices) e usar o adequado
- **Critério de troca:** distância + resolução da tela
- **Regra prática:** tela 640×480 = ~307K pixels; objeto ocupa metade = ~150K pixels → mais que ~300K triângulos é desperdício
- **Popping:** artefato visual na troca de LOD (modelo "salta" de um nível para outro)

---

## 55–60 min | Bloco 1: Revisão-relâmpago (você já sabe, só refrescar)

- **Tradutor direto:** N×(N−1) tradutores → explosão combinatória
- **Arquivo neutro:** 2N conversores → escalável; arquivo maior (precisa ser abrangente)
- **IGES (1980):** só geometria — como uma "foto" da peça, sem semântica
- **STEP (ISO 10303):** informação completa de produto (geometria + material + tolerância + ciclo de vida)
- **Arquitetura STEP — 3 camadas:**
  1. Description Methods: EXPRESS (linguagem de especificação, NÃO de programação)
  2. Integrated Resources: bibliotecas reutilizáveis (geometria, topologia, materiais, tolerâncias)
  3. Application Protocols: AP203 (design 3D), AP214 (automotivo), AP242 (unifica AP203+AP214)
- **EXPRESS:** define ENTITY, atributos, WHERE rules (restrições), SUBTYPE/SUPERTYPE (herança)
- **SDAI:** API padronizada para acessar dados STEP sem parser próprio
- **STEP-NC (ISO 14649):** envia features e operações para CNC, não código G de baixo nível
- **3 domínios do Product Model:** Estrutural (BOM, assembly) + Geométrico (CSG/B-rep) + Conhecimento (regras, tolerâncias)
- **SET:** padrão francês; **VDA-FS:** alemão, foco em superfícies automotivas — ambos precursores do STEP

---

## Dicas finais para a prova

- **STEP vs. IGES** é questão quase garantida — saiba a diferença de cor
- **Paramétrico vs. Variacional** — saiba explicar com exemplo
- Das **4 deficiências do CAD tradicional**, cite pelo menos 3
- Das **conversões entre representações**, saiba que B-rep→CSG é "muito mais complicada"
- **Half-Edge elimina verificação de orientação** (vantagem sobre Winged-Edge)
- **Voxels não são concisos** — isso sempre aparece
- **Octree: Empty, Full, Partial** — os 3 estados
- **EAD's de Gindy** — conceito de direções de acesso da ferramenta
- **DSG = CSG só com diferença** (subtração)
- **LOD: critério = distância + resolução da tela**
