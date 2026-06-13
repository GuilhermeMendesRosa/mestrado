# Material de Estudo — Dia 2: Modelos de Produto, STEP-NC e Fundamentos da Modelagem Paramétrica

**Fontes:** Mortenson Capítulo 10 (instancing, parameterized shapes, group technology) + conhecimento complementar para STEP-NC, product models, modelagem variacional e restrições.

---

# PARTE A — Fechando o Bloco 1: Modelos de Produto e Aplicações na Manufatura

## 1. Modelos de Produto (Product Models)

### 1.1 Além da geometria

Vimos no Dia 1 que o IGES troca geometria e o STEP troca informação de produto. Mas o que significa exatamente "informação de produto"?

Um produto não é apenas uma forma geométrica. Um suporte mecânico, por exemplo, envolve:
- **Forma e dimensões** (geometria)
- **De que material é feito** (aço, alumínio, polímero)
- **Como é fabricado** (fundido, usinado, injetado)
- **Quais tolerâncias deve respeitar** (dimensional, geométrica)
- **Como se monta com outras peças** (estrutura de assembly)
- **Em qual revisão está** (versionamento)
- **Quem aprovou** (workflow de engenharia)

Um modelo de produto integrado tenta capturar tudo isso em uma representação computável — não apenas "desenhar" a peça, mas criar uma base de dados que responda a perguntas como "esta peça pode ser fabricada?", "qual o custo?", "ela resiste à carga especificada?".

### 1.2 Três domínios do modelo de produto

```
┌────────────────────────────────────────────────────┐
│              INTEGRATED PRODUCT MODEL               │
│                                                     │
│  ┌──────────────┐ ┌──────────────┐ ┌─────────────┐ │
│  │  ESTRUTURAL  │ │  GEOMÉTRICO  │ │ CONHECIMENTO │ │
│  │              │ │              │ │              │ │
│  │ • Montagem   │ │ • Forma      │ │ • Regras     │ │
│  │ • BOM        │ │ • Dimensões  │ │ • Restrições │ │
│  │ • Relações   │ │ • Posição    │ │ • Tolerâncias│ │
│  │ • Versões    │ │ • CSG/B-rep  │ │ • Intenção   │ │
│  └──────────────┘ └──────────────┘ └─────────────┘ │
└────────────────────────────────────────────────────┘
```

#### Domínio Estrutural

Responde à pergunta: **"Do que esta peça faz parte?"**

- **BOM (Bill of Materials):** lista hierárquica de todos os componentes
- **Estrutura de montagem:** relações pai-filho entre conjuntos e subconjuntos
- **Relações entre componentes:** posição relativa, restrições de montagem
- **Versionamento e configuração:** revisões do produto e variantes

Exemplo: um motor é composto por bloco + cabeçote + virabrequim + pistões + bielas... Cada um desses é um nó na hierarquia estrutural.

#### Domínio Geométrico

Responde à pergunta: **"Qual é a forma e onde está?"**

- Forma (shape) da peça — via CSG, B-rep, sweep, etc.
- Dimensões e posição no espaço
- É o que o IGES cobre (parcialmente), e o que sistemas CAD tradicionais sempre fizeram
- É a base sobre a qual os outros domínios se apoiam

**Ponto de prova:** Geometria sozinha é condição necessária mas não suficiente para um modelo de produto completo.

#### Domínio de Conhecimento

Responde à pergunta: **"Por que esta peça é assim e como deve ser julgada?"**

- **Regras de projeto:** "a parede deve ter no mínimo 3 mm de espessura"
- **Restrições funcionais:** "a deflexão máxima é 0.1 mm sob carga X"
- **Tolerâncias:** "o furo deve ter diâmetro 10 ± 0.05 mm"
- **Especificações:** acabamento superficial, tratamento térmico, normas aplicáveis
- **Intenção de projeto:** o raciocínio do projetista por trás de cada decisão

Este domínio é o que torna o modelo "inteligente" — ele não apenas mostra a peça, mas carrega as regras que a definem.

### 1.3 Integrated Product Model

O conceito de **Integrated Product Model** (Modelo de Produto Integrado) é exatamente a combinação dos três domínios em uma única representação coerente e computável.

Por que isso importa:
- **Análise automática:** Verificar se a peça satisfaz as regras de conhecimento sem intervenção humana
- **Simulação:** Avaliar desempenho estrutural, térmico, fluídico sobre o modelo integrado
- **Manufatura assistida:** Extrair automaticamente o plano de fabricação a partir das features e tolerâncias
- **Rastreabilidade:** Saber quem aprovou o quê e quando

O STEP foi construído sobre este conceito — ele não é apenas um formato de arquivo, é uma implementação do paradigma de modelo de produto integrado.

---

## 2. STEP-NC e Integração com a Manufatura

### 2.1 O problema do código G tradicional

O código G (ISO 6983) é o padrão tradicional de comando numérico. Ele diz à máquina CNC **como** se mover, instrução por instrução:

```
N10 G00 X0 Y0 Z5      (movimento rápido para posição inicial)
N20 G01 Z-10 F100     (descer a ferramenta a 100 mm/min)
N30 G01 X50 F200      (cortar até X=50)
N40 G00 Z5            (subir a ferramenta)
...
```

**Limitações do código G:**
- Descreve movimentos de eixos, não features de usinagem
- Não sabe o que está usinando — só sabe coordenadas
- Dependente da máquina específica (precisa de pós-processador)
- Mudar de máquina = reprogramar
- Não contém tolerâncias, material, ou estratégia de usinagem

### 2.2 STEP-NC (ISO 14649)

O **STEP-NC** é uma extensão do STEP que eleva o nível de abstração do comando numérico: em vez de enviar movimentos de eixo, envia **informação de features e operações de usinagem**.

**Diferença fundamental:**

| Código G tradicional | STEP-NC |
|---------------------|---------|
| "Como" usinar | "O quê" usinar |
| Movimentos de eixo | Features + operações |
| Baixo nível | Alto nível |
| Dependente de máquina | Independente de máquina |
| Interpretação humana necessária | Interpretável pela máquina |
| Tolerâncias ignoradas | Tolerâncias incluídas |

**Exemplo do que o STEP-NC envia:**
- "Usinar uma cavidade retangular (pocket) com dimensões X, tolerância Y, usando estratégia de fresamento em espiral"
- A máquina CNC interpreta isso e gera as trajetórias de ferramenta otimizadas para seu hardware específico

**Benefícios:**
1. **Independência de máquina:** o mesmo arquivo STEP-NC serve para diferentes CNCs
2. **Otimização automática:** o controlador da máquina pode adaptar a estratégia ao hardware
3. **Bidirectionalidade:** modificações na usinagem podem realimentar o modelo de design
4. **Integração real CAD-CAM-CNC:** o modelo de design alimenta diretamente a manufatura sem perda de informação

---

# PARTE B — Bloco 2: Modelagem Paramétrica e Variacional

## 3. Conceitos Fundamentais

### 3.1 Design Intent (Intenção de Projeto)

**Definição:** Design Intent é o conjunto de regras, relações e restrições que capturam o raciocínio do projetista e ficam embutidas no modelo paramétrico.

**Sem Design Intent:**
- Você desenha um flange com 6 furos igualmente espaçados
- Alguém muda o diâmetro do flange para 200 mm em vez de 150 mm
- Os furos **não** se reposicionam — permanecem onde estavam, agora errados
- O modelo "quebrou" porque a geometria não carrega as regras de projeto

**Com Design Intent:**
- Você desenha o flange e define: "os furos estão em um círculo concêntrico ao flange, igualmente espaçados, com diâmetro proporcional ao diâmetro do flange"
- Alguém muda o diâmetro do flange
- Os furos se reposicionam e redimensionam automaticamente
- O modelo permanece coerente

**Conceito para a prova:** Design Intent é o que transforma um modelo geométrico passivo em um modelo paramétrico ativo. Sem ele, o modelo é apenas um desenho; com ele, o modelo é uma "máquina" que gera geometria correta sob variação de parâmetros.

### 3.2 Famílias de Peças (Family of Parts)

#### O que o Mortenson diz (Capítulo 10, p. 298-301)

Mortenson aborda este conceito sob o nome de **group technology** (tecnologia de grupo) e **parameterized shapes** (formas parametrizadas):

> "A related scheme, called **group technology**, came into use in concert with certain computer-aided manufacturing techniques to encourage standardization in part design and production. The central thesis and main advantage of group technology is that **many manufactured parts can be grouped into classes or families of similar shapes, where individual members are distinguished by a few parameters (key dimensions)**."

Mortenson define os conceitos fundamentais:
- **Generic primitive** (primitiva genérica): uma família inteira de formas similares
- **Primitive instance** (instância primitiva): um membro individual da família
- **Key dimensions** (dimensões-chave): os parâmetros que distinguem os membros

> "A few key dimensions are usually sufficient to define the shapes of simple objects. If each dimension is an independent variable, then we can produce a **particular shape within a class of objects by specifying the key dimensions or parameters**."

#### O conceito na prática

Uma família de peças é o equivalente moderno do que Mortenson chamava de generic primitive. Exemplos:

- **Família de parafusos:** mesmo design (cabeça sextavada + rosca), parâmetros diferentes (M6×20, M8×30, M10×40)
- **Família de engrenagens:** mesmo perfil de dente, variando número de dentes e módulo
- **Família de flanges:** mesmo padrão de furos, variando diâmetro nominal e classe de pressão

**Relação com instancing do Mortenson (Cap. 10.5):**

Mortenson define uma instância como uma transformação linear de uma primitiva:
> "A direct way of defining a new solid shape is as a **simple linear transformation of an existing one**... Each new cube or rectangular solid is a particular **instance** of the initial cube."

A modelagem paramétrica moderna estende esse conceito: em vez de apenas transformar (escalar, transladar, rotacionar) primitivas predefinidas, permite definir relações paramétricas arbitrárias entre quaisquer elementos geométricos.

**Limitação apontada por Mortenson (Cap. 10, p. 301):**
> "Parameterized-shape or group-technology models are easy to validate and use. They are **unquestionably concise**; however, the **number of useful generic primitives, though large, is limited**. Modeling systems built on this type of representation only are highly specialized; a **large repertoire of generic primitives** is required for them to have wide application."

Isso explica por que sistemas puramente baseados em primitivas parametrizadas evoluíram para sistemas com modelagem paramétrica de geometria arbitrária.

### 3.3 Modelagem Paramétrica vs. Modelagem Variacional

Esta é uma distinção conceitual importante que costuma aparecer em provas.

#### Modelagem Paramétrica

Características:
- As dependências entre parâmetros têm **direção definida** (unidirecionais)
- O modelo é resolvido em **ordem sequencial**, seguindo o histórico de construção
- Cada parâmetro é calculado a partir dos que já foram definidos antes dele

Exemplo:
```
L1 = 100          (parâmetro base)
L2 = L1 / 2       (L2 depende de L1 — se L1 mudar, L2 atualiza)
L3 = L2 + 10      (L3 depende de L2)
```

Se você muda L1, tudo atualiza. Mas se você tentar mudar L2 diretamente, L1 **não** muda — a dependência é unidirecional. O sistema dirá que L2 é "driven" (conduzido por L1).

**É como uma planilha Excel:** cada célula tem uma fórmula que aponta para outras células. A direção das referências define a direção da propagação de mudanças.

#### Modelagem Variacional

Características:
- As restrições são tratadas como **equações simultâneas**
- Não há direção preferencial — o sistema resolve tudo junto
- Usa um **solver** que encontra valores que satisfazem todas as restrições

Exemplo:
```
L1 + L2 = 300     (restrição 1)
L1 = 2 * L2       (restrição 2)
```

O solver resolve este sistema: L1 = 200, L2 = 100. Se você tentar mudar L1 para 150, o solver recalcula L2 = 150. Se você tentar mudar L2 para 60, o solver recalcula L1 = 240. Não importa qual variável você mexa — o sistema encontra a solução que satisfaz todas as equações.

**É como um sistema de equações algébricas:** as incógnitas são resolvidas simultaneamente, sem hierarquia.

#### Comparação direta

| Critério | Paramétrico | Variacional |
|----------|-------------|-------------|
| **Direção das dependências** | Unidirecional (definida) | Bidirecional (simultânea) |
| **Ordem de resolução** | Sequencial (histórico) | Simultânea (solver) |
| **O que acontece se eu mudo uma cota?** | Só afeta o que vem depois | Afeta tudo o que for necessário |
| **Flexibilidade** | Menor (rígido) | Maior (flexível) |
| **Custo computacional** | Menor (simples) | Maior (precisa de solver numérico) |
| **Previsibilidade** | Alta (sequência clara) | Média (múltiplas soluções possíveis) |
| **Exemplo de software** | SolidWorks, Inventor, Creo (histórico) | SolidWorks (equações), Catia (knowledgeware) |

> **Ponto de prova:** A maioria dos sistemas CAD comerciais modernos (SolidWorks, Inventor, Creo) usa modelagem **paramétrica** com histórico, mas incorpora elementos **variacionais** (equações simultâneas, restrições de sketch 2D). Não são puramente um nem outro.

---

## 4. Tipos de Restrições (Constraints)

### 4.1 Restrições Geométricas

Definem relações espaciais entre entidades geométricas. São as mais comuns e as mais fáceis de implementar computacionalmente.

**Categorias:**

| Tipo | Exemplos |
|------|----------|
| **Orientação** | Paralelo, perpendicular, colinear, tangente |
| **Posição** | Coincidente, concêntrico, midpoint, fixo |
| **Dimensional** | Distância, ângulo, raio, diâmetro, comprimento |
| **Simetria** | Simétrico em relação a linha ou plano |
| **Padrão** | Igual (equal), padrão circular, padrão retangular |

**Exemplo de sketch 2D com restrições geométricas:**
- Linha L1 é horizontal (restrição de orientação)
- Linha L2 é paralela a L1 (restrição de orientação)
- A distância entre L1 e L2 é 50 mm (restrição dimensional)
- O círculo C1 é concêntrico à origem (restrição de posição)
- C2 tem o mesmo raio que C1 (restrição de padrão/equal)

### 4.2 Restrições Funcionais (ou de Engenharia)

São restrições baseadas em requisitos de desempenho, não apenas em relações espaciais. Conectam a geometria com a física do produto.

| Tipo | Exemplo |
|------|---------|
| **Resistência** | Tensão máxima ≤ 200 MPa |
| **Rigidez** | Deflexão máxima ≤ 0.05 mm |
| **Peso** | Massa total ≤ 5 kg |
| **Fluídica** | Vazão mínima ≥ 10 L/min |
| **Térmica** | Temperatura máxima ≤ 120°C |
| **Frequência** | Primeira frequência natural ≥ 50 Hz |

**Por que são mais complexas:**
- Exigem integração com modelos de análise (FEA, CFD)
- Dependem de propriedades de material (módulo de elasticidade, densidade)
- A avaliação pode exigir simulação numérica, não apenas álgebra
- O vínculo entre geometria e desempenho é indireto

Exemplo: "a área da seção transversal deve ser ≥ X para que a tensão não exceda Y." Para verificar isso, o sistema precisa calcular a tensão (o que pode exigir FEA) e comparar com o limite. Não é uma equação puramente geométrica.

### 4.3 Restrições Variacionais

Permitem **intervalos** (desigualdades) em vez de valores fixos. Definem um **espaço de soluções viáveis**.

| Igualdade (=) | Desigualdade (restrição variacional) |
|---------------|--------------------------------------|
| L = 100 | 50 ≤ L ≤ 100 |
| θ = 45° | θ ≥ 30° |
| D = 10 | D ≤ 12 |

**Utilidade:**
- **Projeto preliminar:** quando os valores exatos ainda não estão decididos, mas os limites são conhecidos
- **Otimização:** definir o espaço de busca para algoritmos de otimização
- **Design robusto:** garantir que o produto funcione dentro de uma faixa de variação

---

## 5. Conexão com o Mortenson

O Capítulo 10 do Mortenson fornece a fundação matemática e conceitual para modelagem paramétrica:

| Conceito no Mortenson (Cap. 10) | Evolução para a modelagem moderna |
|--------------------------------|-----------------------------------|
| **Parametric solid** (Eq. 10.1): x = x(u,v,w), y = y(u,v,w), z = z(u,v,w) | Funções paramétricas como base matemática de qualquer modelo variável |
| **Instance** de primitiva: transformação linear de uma primitiva existente (p. 298) | Instâncias paramétricas com mais graus de liberdade |
| **Group technology** e **generic primitives** (p. 298-301) | Famílias de peças (Family of Parts) |
| **Key dimensions** como variáveis independentes (p. 301) | Parâmetros de usuário (user parameters) |
| **Parameterized shapes** com topologia fixa (p. 301) | Modelos paramétricos com topologia variável (suppress features) |
| Limitação: "the number of useful generic primitives... is limited" (p. 301) | Motivação para modelagem paramétrica de geometria arbitrária |
| **Sweep solids** (translational, rotational, general) — Cap. 10.6 | Operações paramétricas de sweep/extrude/revolve |
| **Controlled deformation solids** (Cap. 10.7) | Operações de deformação paramétrica (bend, twist, stretch) |

---

## 6. Autoavaliação do Dia 2

Responda sem consultar:

1. Quais são os três domínios de um modelo de produto? Dê um exemplo de informação em cada um.
2. O que é STEP-NC e como ele difere do código G tradicional?
3. Por que a geometria sozinha não é suficiente para um modelo de produto completo?
4. O que é Design Intent? Dê um exemplo concreto em uma peça mecânica.
5. Como o conceito de "group technology" do Mortenson se relaciona com "family of parts"?
6. Qual a definição de "generic primitive" e "primitive instance" segundo Mortenson?
7. Explique a diferença entre modelagem paramétrica e variacional com um exemplo.
8. O que é uma restrição geométrica? E uma restrição funcional? Dê um exemplo de cada.
9. O que caracteriza uma restrição variacional? Em que situação ela é útil?
10. Qual a principal limitação dos sistemas puramente baseados em primitivas parametrizadas, segundo Mortenson?
