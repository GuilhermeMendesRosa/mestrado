# Material de Estudo — Dia 1: Interoperabilidade e Padrões de Troca de Dados CAD

**Fonte:** Conhecimento complementar de padrões ISO e literatura de CAD/CAM. Este conteúdo não está no Mortenson.

---

## 1. O Problema da Comunicação entre Sistemas CAD

### 1.1 Por que precisamos trocar dados?

Em um ambiente industrial típico, diferentes departamentos usam diferentes softwares:
- **Projeto (CAD):** CATIA, SolidWorks, NX, Creo, Inventor
- **Análise (CAE):** ANSYS, Abaqus, Nastran
- **Manufatura (CAM):** Mastercam, NX CAM, CATIA Machining
- **Inspeção:** software de medição 3D, CMM
- **Gestão (PDM/PLM):** Teamcenter, Windchill, Enovia

Cada software tem seu **formato interno proprietário** de armazenamento. Sem um padrão de troca, um arquivo do CATIA não abre no NX, e um modelo do SolidWorks é ilegível no ANSYS.

Este é o problema fundamental que os padrões de troca de dados CAD tentam resolver: **permitir que informação de produto transite entre sistemas heterogêneos sem perda de significado.**

### 1.2 Duas estratégias de comunicação

#### Estratégia A: Tradutor Direto (Point-to-Point)

Cada par de sistemas tem um conversor dedicado.

```
CATIA ────tradutor───→ NX
CATIA ────tradutor───→ ANSYS
CATIA ────tradutor───→ Mastercam
NX    ────tradutor───→ CATIA
NX    ────tradutor───→ ANSYS
... e assim por diante
```

Para **N sistemas**, são necessários **N × (N − 1)** tradutores. Com 10 sistemas: 90 tradutores.

| Vantagens | Desvantagens |
|-----------|-------------|
| Tradução otimizada para cada par | Explosão combinatória (cresce com N²) |
| Potencialmente mais rápido e preciso | Manutenção insustentável quando softwares evoluem |
| Menor tamanho de arquivo | Cada tradutor é um projeto de software complexo |

#### Estratégia B: Arquivo Neutro (Neutral File)

Cada sistema exporta e importa de um formato comum padronizado.

```
CATIA ───→ export .step ──→ NX
                             ANSYS
                             Mastercam
                             ...
```

Para **N sistemas**, são necessários apenas **2N** conversores (N exportadores + N importadores). Com 10 sistemas: 20 conversores.

| Vantagens | Desvantagens |
|-----------|-------------|
| Escalável — cresce linearmente com N | Arquivo maior (precisa ser abrangente) |
| Fácil de manter — muda o exportador de 1 sistema, não N−1 tradutores | Possível perda de informação específica do sistema |
| Permite adicionar novo sistema com apenas 2 conversores | Tradução de ida e volta pode degradar dados |
| Independência de fornecedor | Pode não cobrir 100% das funcionalidades de cada sistema |

#### O Trade-off

O arquivo neutro é maior porque precisa ser "generoso": inclui redundâncias e metadados para que qualquer sistema consiga interpretar a informação, mesmo que parte dela seja irrelevante para aquele sistema. O tradutor direto pode ser "enxuto" porque sabe exatamente o que o sistema de destino precisa. Porém, o custo de manter N² tradutores supera em muito a desvantagem do tamanho de arquivo.

**A indústria escolheu a estratégia do arquivo neutro.**

---

## 2. Padrões Clássicos e Histórico

### 2.1 O Programa ICAM (anos 1970)

O **Integrated Computer-Aided Manufacturing** foi um programa da Força Aérea dos EUA (US Air Force) nos anos 1970 com o objetivo de integrar computacionalmente o design e a manufatura de componentes aeroespaciais.

O ICAM evidenciou que, sem um formato padronizado, cada contratante e subcontratante precisaria de tradutores diferentes, inviabilizando a integração. Deste programa nasceu a necessidade que levou ao IGES.

**Legado do ICAM:** a percepção de que interoperabilidade não é um luxo — é um requisito de sobrevivência para cadeias de suprimento complexas.

### 2.2 IGES (Initial Graphics Exchange Specification)

- **Ano:** 1980 (padrão ANSI Y14.26M, depois US PRO/IPO-100)
- **Significado do nome:** Especificação Inicial de Troca Gráfica
- **O que é:** O primeiro grande padrão neutro de troca de dados CAD adotado internacionalmente
- **Escopo principal:** Geometria — curvas, superfícies, wireframe, anotações 2D

#### O que o IGES troca (e o que não troca)

| Inclui | Não inclui |
|--------|-----------|
| Curvas (linhas, arcos, cônicas, splines) | Materiais |
| Superfícies (planos, cilindros, NURBS) | Tolerâncias dimensionais e geométricas |
| Estrutura wireframe | Estrutura de montagem (assembly) |
| Anotações e dimensões 2D | Histórico de construção |
| Entidades de desenho (vistas, cortes) | Intenção de projeto |
| | Informação de manufatura |
| | Ciclo de vida do produto |

#### Limitações do IGES (questão de prova)

1. **Só geometria, sem semântica:** Um furo é trocado como um conjunto de superfícies cilíndricas, não como "furo passante M8"
2. **Sem informação de produto:** Não há como saber material, processo de fabricação, tolerância
3. **Arquivos muito grandes:** Representação verbosa, sem compressão eficiente
4. **Interpretação ambígua:** Sistemas diferentes podem interpretar as mesmas entidades de forma diferente
5. **Foco gráfico, não funcional:** Feito para "desenhar", não para "simular" ou "fabricar"

> **Analogia para prova:** IGES é como enviar uma foto de uma peça — você vê a forma, mas não sabe de que material é feita, qual a tolerância, nem como foi projetada para ser fabricada.

### 2.3 SET (Standard d'Échange et de Transfert)

- Padrão francês (norma AFNOR Z68-300), concorrente e precursor do STEP
- Escopo similar ao IGES: foco em geometria de curvas e superfícies
- Adotado principalmente na indústria aeroespacial francesa (Airbus, Dassault)
- Perdeu relevância quando o STEP foi padronizado internacionalmente

### 2.4 VDA-FS (Verband der Automobilindustrie — Flächenschnittstelle)

- Padrão da indústria automotiva alemã (VDA = associação da indústria automobilística)
- **Foco muito específico:** troca de dados de superfícies de forma livre (freeform surfaces)
- Contexto: montadoras alemãs (BMW, Mercedes, VW, Audi) trocando dados de carroceria e superfícies de classe A com fornecedores
- Otimizado para curvas e superfícies complexas (Bézier, B-spline)
- Limitado a geometria de superfície — não cobre sólidos, montagens ou informação de produto

#### Por que tantos padrões?

Cada indústria e cada país desenvolveu seu padrão porque:
- O IGES era genérico demais para necessidades específicas
- A indústria automotiva alemã precisava de alta precisão em superfícies (VDA-FS)
- A indústria aeroespacial francesa precisava de algo mais estruturado (SET)
- Todos convergiram para a necessidade de algo mais completo (STEP)

---

## 3. O Padrão STEP (ISO 10303)

### 3.1 O que é STEP

**STEP** = **ST**andard for the **E**xchange of **P**roduct model data.

É a norma **ISO 10303**, desenvolvida a partir dos anos 1980 e publicada a partir de 1994, como evolução que resolve as limitações de IGES, SET e VDA-FS.

> **Resumo para prova:** O STEP não é apenas mais um formato de arquivo — é uma infraestrutura completa para representação e troca de dados de produto ao longo de todo o seu ciclo de vida.

### 3.2 A diferença crucial: STEP vs. IGES (questão certa de prova)

| Critério | IGES | STEP (ISO 10303) |
|----------|------|-------------------|
| **O que troca** | Geometria (entidades gráficas) | Informação completa de produto |
| **Semântica** | Pobre — apenas forma | Rica — forma + material + processo + tolerância |
| **Ciclo de vida** | Cobre só o desenho | Cobre design → análise → manufatura → inspeção → suporte |
| **Estrutura** | Lista plana de entidades | Modelo de dados em camadas com schema formal |
| **Validação** | Sintática apenas | Sintática + semântica (via EXPRESS) |
| **Manufatura** | Não cobre | Cobre (STEP-NC, ISO 14649) |
| **Modelo de dados** | Implícito, não documentado | Explícito, documentado em EXPRESS |
| **Extensibilidade** | Difícil (formatos fixos) | Modular (Application Protocols) |

> **A diferença em uma frase:** IGES é um formato de desenho eletrônico; STEP é um modelo de produto computável.

### 3.3 Arquitetura do STEP (três camadas)

O STEP é organizado em três camadas, das mais abstratas/fundacionais às mais concretas/específicas:

```
┌─────────────────────────────────────────────────────┐
│  3. APPLICATION PROTOCOLS (APs)                     │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐            │
│  │  AP203   │ │  AP214   │ │  AP242   │  ...       │
│  │ Design   │ │Automotivo│ │  MBE     │            │
│  └──────────┘ └──────────┘ └──────────┘            │
├─────────────────────────────────────────────────────┤
│  2. INTEGRATED RESOURCES (IRs)                      │
│  Geometria │ Topologia │ Materiais │ Tolerâncias... │
├─────────────────────────────────────────────────────┤
│  1. DESCRIPTION METHODS                             │
│  EXPRESS │ EXPRESS-G │ Schemas de modelagem        │
└─────────────────────────────────────────────────────┘
```

#### Camada 1: Description Methods (Métodos de Descrição)

Define **como** descrever os dados, não o que descrever. É a "linguagem" do STEP.

- **EXPRESS (ISO 10303-11):** Linguagem formal de modelagem de dados, orientada a objetos, schema-based. Define entidades, atributos, relações e restrições (WHERE rules).
- **EXPRESS-G:** Notação gráfica da EXPRESS — diagramas para visualizar schemas
- **EXPRESS-X:** Extensão para mapeamento entre schemas

> **Ponto de prova:** EXPRESS **não é** uma linguagem de programação. É uma linguagem de **especificação de dados** — você descreve a estrutura que os dados devem ter, não como processá-los.

Exemplo de uma entidade em EXPRESS:

```
ENTITY Circle;
  center  : Point;
  radius  : REAL;
  WHERE
    radius > 0.0;
END_ENTITY;
```

#### Camada 2: Integrated Resources (Recursos Integrados)

Bibliotecas reutilizáveis de definições — os "blocos de construção" do STEP. Estes recursos são usados pelos Application Protocols.

Principais IRs:
- **Part 42:** Geometric and topological representation (geometria e topologia)
- **Part 43:** Representation structures (estruturas de representação)
- **Part 44:** Product structure configuration (estrutura de produto)
- **Part 45:** Materials (materiais)
- **Part 46:** Visual presentation (apresentação visual)
- **Part 47:** Tolerances (tolerâncias)
- **Part 49:** Process structure and properties (processos)

Os recursos integrados evitam duplicação — cada conceito é definido uma vez e reutilizado pelos APs.

#### Camada 3: Application Protocols (APs)

Definem quais partes do modelo STEP são necessárias para um domínio específico. Cada AP é uma "fatia" do modelo STEP completo.

Principais APs:

| AP | Nome | Domínio |
|----|------|---------|
| **AP203** | Configuration Controlled 3D Design | Design mecânico 3D com controle de configuração (versões, approval) |
| **AP214** | Core Data for Automotive Mechanical Design | Dados de design automotivo |
| **AP224** | Feature-Based Process Planning | Planejamento de processo baseado em features (usinagem) |
| **AP238** | STEP-NC (Application Interpreted Model for CNC) | Integração CAD-CAM-CNC |
| **AP242** | Managed Model-Based 3D Engineering | Sucessor que unifica AP203 + AP214 (MBE) |
| **AP239** | Product Life Cycle Support (PLCS) | Suporte ao ciclo de vida |

> **Ponto de prova:** Um AP é como um "contrato" entre sistemas: define exatamente o que será trocado para um determinado propósito, evitando ambiguidade.

### 3.4 EXPRESS — A linguagem do STEP

**EXPRESS (ISO 10303-11)** é uma linguagem de modelagem de dados, não de programação. Suas características:

- **Schema:** agrupamento lógico de definições relacionadas
- **ENTITY:** define um tipo de objeto com atributos
- **TYPE:** define tipos de dados (simples ou enumerados)
- **SUBTYPE/SUPERTYPE:** herança entre entidades
- **WHERE:** regras de validação (restrições que os dados devem satisfazer)
- **UNIQUE:** restrições de unicidade
- **INVERSE:** relações inversas entre entidades

Por que EXPRESS em vez de UML ou SQL?
- Projetada especificamente para dados de produto de engenharia
- Suporta restrições complexas (WHERE rules) que vão além de chaves estrangeiras
- Independente de implementação — não dita como os dados serão armazenados

### 3.5 SDAI (Standard Data Access Interface)

**SDAI (ISO 10303-22)** é uma API padronizada para acesso programático a dados STEP.

**Problema que resolve:** Sem o SDAI, cada aplicação precisaria implementar seu próprio parser de arquivos STEP (formato físico ISO 10303-21), o que é complexo e propenso a erro.

**O que o SDAI provê:**
- Operações de consulta e navegação sobre modelos STEP
- Criação, leitura, atualização e deleção de entidades
- Gerenciamento de sessões e transações
- Independência do formato de armazenamento físico

```
Aplicação CAD
      │
      ▼
  SDAI (API padronizada)
      │
      ▼
  Base de dados STEP / Arquivo .step físico
```

> **Analogia para prova:** EXPRESS é o "dicionário" (define as palavras que existem) e SDAI é o "manual de conversação" (define como usar essas palavras em uma conversa entre sistemas).

### 3.6 Formatos físicos do STEP

O STEP define vários formatos de arquivo:

- **ISO 10303-21 (Clear Text Encoding):** formato texto, extensão `.step` ou `.stp` — o mais comum
- **ISO 10303-28 (XML Encoding):** formato XML para aplicações web
- **ISO 10303-26 (Binary Encoding):** formato binário para eficiência

Exemplo simplificado de um arquivo STEP (Clear Text):

```
ISO-10303-21;
HEADER;
  FILE_DESCRIPTION('Example part',';1');
  FILE_NAME('part.stp','2024-01-01','Author');
  FILE_SCHEMA(('CONFIG_CONTROL_DESIGN'));
ENDSEC;
DATA;
  #1 = CARTESIAN_POINT('',(0.0, 0.0, 0.0));
  #2 = CARTESIAN_POINT('',(100.0, 0.0, 0.0));
  #3 = CIRCLE('', #4, 10.0);
  ...
ENDSEC;
END-ISO-10303-21;
```

---

## 4. Resumo Visual para Revisão

### Linha do tempo dos padrões

```
1970 ── ICAM (US Air Force) ── necessidade de integração
  │
1980 ── IGES (ANSI) ── primeiro padrão neutro de geometria
  │
1980s ── SET (França), VDA-FS (Alemanha) ── padrões setoriais
  │
1994 ── STEP / ISO 10303 ── padrão internacional de produto
  │
2000s ── STEP-NC (ISO 14649), AP242 ── evolução contínua
```

### Mapa mental dos conceitos-chave

- **Problema:** sistemas diferentes, formatos proprietários, precisam trocar dados
  - **Solução A:** N×(N−1) tradutores diretos → não escala
  - **Solução B:** 2N conversores via arquivo neutro → escalável
- **IGES (1980):** só geometria, sem semântica, foco em "desenho"
- **STEP (ISO 10303):** informação completa de produto
  - **Arquitetura em 3 camadas**
    - Camada 1: EXPRESS (linguagem de especificação)
    - Camada 2: Integrated Resources (bibliotecas reutilizáveis)
    - Camada 3: Application Protocols (AP203, AP214, AP242...)
  - **EXPRESS:** define entidades, atributos, restrições (WHERE)
  - **SDAI:** API padronizada de acesso (não precisa de parser próprio)
  - **STEP-NC:** estende o STEP para comando numérico

---

## 5. Autoavaliação do Dia 1

Antes de dormir, responda sem consultar:

1. Por que N×(N−1) tradutores não escalam bem?
2. Qual a vantagem principal do arquivo neutro sobre o tradutor direto?
3. O que é o IGES e qual sua principal limitação?
4. Qual a diferença fundamental entre STEP e IGES?
5. Descreva as três camadas da arquitetura STEP.
6. O que é um Application Protocol? Dê dois exemplos.
7. Para que serve a linguagem EXPRESS? Por que ela não é uma linguagem de programação?
8. Qual o papel do SDAI na arquitetura STEP?
