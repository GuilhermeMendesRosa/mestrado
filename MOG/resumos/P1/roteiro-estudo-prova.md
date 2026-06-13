# Roteiro de estudo para a prova

Baseado nos PDFs encontrados nesta pasta. O foco abaixo e revisar os assuntos que aparecem de forma recorrente e que tem mais cara de conteudo de prova.

Arquivos usados como base:

- `00a - Revisao da Matematica - matrizes_V2.pdf`
- `00b - fundamentosMath__4_1_1.pdf`
- `01 - O que eh um Modelo v3_6.pdf`
- `02 - Objetos Naturais v3_2.pdf`
- `03 - 2 e meio D wireframe.pdf`
- `04 - Def Solidos e Nao Solidos v3_1_1.pdf`
- `05 - Revisao da Matematica - vetores e sistemas de coordenadas.pdf`
- `06 - Modelagem de Solidos- Criacao Inst-Param-Sweep v6_3.pdf`
- `08 - Modelagem de Solidos - Criacao Topologica v7_2_1.pdf`
- `09 - Modelagem de Solidos  - Criacao Booleana v9_2.pdf`
- `11 - Modelagem de Solidos - representa Brep v7_4_4.pdf`
- `12 - Representa Solidos CSG v5_2.pdf`
- `15 - Curvas Suaves v6_2_1_8.pdf`
- `15_1-Curvas_Suaves_Hermite_V7_1_4.pdf`
- `16 - Superficies v3_2.pdf`

Observacao:

- `16-Superficies_Marina_Rosso_2022.pdf` nao retornou texto util na extracao automatica, entao o roteiro de superficies foi montado principalmente a partir do arquivo `16 - Superficies v3_2.pdf`.

## 1. Prioridade alta: matematica base

### Matrizes e transformacoes

Estudar:

- dimensao de matrizes
- soma, multiplicacao por escalar e multiplicacao matricial
- compatibilidade de dimensoes
- por que `AB != BA` em geral
- uso de matrizes em computacao grafica
- composicao de transformacoes
- coordenadas homogeneas em 2D e 3D

Saber fazer:

- montar matriz de translacao, rotacao e escala em 2D
- montar matriz de translacao e rotacoes `Rx`, `Ry`, `Rz` em 3D
- combinar varias transformacoes em uma unica matriz
- explicar por que a ordem das transformacoes importa
- rotacionar em torno de um ponto pivor usando `T * R * T^-1`
- entender a ideia de pre-multiplicacao para reduzir custo computacional

### Vetores e sistemas de coordenadas

Estudar:

- definicao de vetor, magnitude, direcao e vetor unitario
- soma, subtracao e multiplicacao por escalar
- projecoes vetoriais
- produto escalar
- produto vetorial
- regra da mao direita
- bases vetoriais e sistemas de coordenadas
- espaco vetorial, combinacao linear, dependencia e independencia linear

Saber fazer:

- normalizar vetor
- calcular angulo entre vetores via produto escalar
- identificar perpendicularidade com produto escalar igual a zero
- calcular normal de um plano com produto vetorial
- obter equacao parametrica de reta a partir de ponto e vetor diretor
- obter equacao de plano por ponto e vetores, por tres pontos, ou por ponto e normal
- entender interseccao entre reta e plano

## 2. Prioridade alta: fundamentos de modelagem geometrica

### O que e um modelo

Estudar:

- niveis de abstracao: mundo fisico, modelo matematico, representacao e implementacao
- sintaxe x semantica na representacao
- proposito de um modelo
- tres capacidades do modelo:
- criar
- representar
- analisar/simular

Saber explicar:

- por que um modelo nao serve apenas para desenhar
- por que representacao precisa equilibrar significado, estrutura de dados e uso posterior
- diferenca entre armazenar geometria e permitir analise do objeto

### Classificacao dos sistemas graficos

Estudar:

- 2D raster
- 2D vetorial
- 2,5D
- 3D
- objetos rigidos x flexiveis
- objetos naturais x manufaturados
- modelagem algoritmica/procedural x geometrica

## 3. Prioridade alta: limitacoes de 2D e wireframe

### Modelos 2D, pseudo-3D e wireframe

Estudar:

- por que sistemas 2D sao ambiguos para representar profundidade e interior/exterior
- conceito de modelo 2,5D e wireframe
- primitivas analiticas e sinteticas em wireframe
- vantagens do wireframe
- desvantagens do wireframe

Pontos que costumam cair bem em prova:

- wireframe e simples, rapido e barato, mas ambiguo
- depende de interpretacao humana
- nao permite, em geral, calculos robustos de volume, centro de massa, interferencia e validacao
- e util como visualizacao, mas fraco como representacao completa de solidos

## 4. Prioridade alta: solidos, nao solidos e propriedades de uma representacao valida

### Diferenca entre solidos, superficies e nao solidos

Estudar:

- solido como objeto 3D integro
- superficie como entidade sem volume/espessura
- por que uma colecao de superficies nao garante um volume fechado
- quando modelagem solida e necessaria

### Propriedades desejadas em esquemas de representacao de solidos

Estudar:

- nao ambiguidade
- fechamento (`closure`)
- unicidade
- validade
- homogeneidade dimensional
- concisao
- eficiencia
- precisao/fidelidade

Saber explicar:

- por que uma representacao ambigua e catastrofica
- por que o modelo precisa continuar valido apos transformacoes e operacoes
- por que arestas, faces e vertices precisam obedecer restricoes topologicas

## 5. Prioridade alta: metodos de criacao de solidos

### Instanciacao

Estudar:

- copia modificada de primitivas padrao
- primitivas comuns: cubo, cilindro, esfera, toro, cone, cunha
- parametros proprios da primitiva
- sistema de coordenadas local
- transformacoes de tamanho, posicao e orientacao

Saber explicar:

- vantagem: compacto, preciso, rapido
- limitacao: dominio muito restrito
- transformacoes mudam geometria, nao topologia

### Parametrizacao

Estudar:

- generalizacao da instanciacao
- familia de objetos definida por parametros de alto nivel
- uso em automacao e tecnologia de grupos

Saber explicar:

- diferenca entre parametrizacao e simples instanciacao
- vantagens e limites do metodo

### Sweeping / varredura

Estudar:

- ideia de varrer uma geratriz ao longo de uma diretriz
- extrusao translacional
- revolucao rotacional
- sweeping generalizado
- lofting
- reconstrucao 3D por secoes planares

Saber explicar:

- o que sao geratriz, diretriz e sistema de coordenadas local
- exemplos: ponto gera curva, curva gera superficie, face gera solido
- problemas classicos: auto-intersecao, falta de `closure`, degeneracoes, dificuldade de validacao

## 6. Prioridade alta: topologia de poliedros

### Conceitos topologicos

Estudar:

- diferenca entre geometria e topologia
- conectividade e continuidade
- propriedades topologicas nao metricas
- objetos equivalentes topologicamente
- variedade-2 (`2-manifold`)
- orientabilidade

### Poliedros e validacao

Estudar:

- definicao de poliedro
- vertices, arestas e faces
- poliedros simples e poliedros platonicos
- formula de Euler: `V - E + F = 2`
- extensao de Euler-Poincare: `V - E + F - H = 2(C - G)`

Saber fazer/explicar:

- usar a formula de Euler para checagem basica
- explicar por que a formula sozinha nao valida tudo
- lembrar restricoes extras:
- cada aresta liga 2 vertices
- cada aresta pertence a 2 faces
- pelo menos 3 arestas por vertice
- faces nao podem se interpenetrar

### Operadores de Euler

Estudar:

- ideia geral de operadores que constroem e destroem mantendo validade topologica
- nomes citados nos slides: `MEV`, `MEF`, `MEFS`, `MEKR`, `MFKRH` e inversos

Nao parece necessario decorar implementacao detalhada, mas vale saber a funcao deles no contexto de modelagem topologica.

## 7. Prioridade muito alta: operacoes booleanas regularizadas

### Booleanas em modelagem solida

Estudar:

- uniao, interseccao e diferenca
- comutatividade de uniao e interseccao
- nao comutatividade da diferenca
- diferenca entre operacao booleana canonica e regularizada

### Regularizacao

Estudar:

- por que booleanas comuns podem gerar resultados invalidos
- ideia de `closure(interior(A op B))`
- dangling parts / heterogeneidade dimensional
- papel de interior e contorno na definicao de solido

Saber explicar:

- por que operacoes booleanas regularizadas garantem `closure`
- por que isso e crucial em modelagem de solidos validos
- relacao entre diferenca regularizada e complemento

## 8. Prioridade muito alta: representacao de solidos

### B-rep

Estudar:

- definicao de Boundary Representation
- representacao do solido por suas superficies limitantes
- superficies fechadas, orientaveis, nao auto-intersectantes e conectadas
- B-rep poliedrico x B-rep generalizado
- faces, arestas, vertices e adjacencias
- validacao topologica e geometrica

Saber comparar:

- B-rep poliedrico: mais simples, eficiente e aproximado
- B-rep generalizado: mais flexivel, exato e complexo

### Estruturas de dados de B-rep

Estudar:

- codificacao explicita
- lista de vertices
- lista de arestas
- Winged-Edge
- Half-Edge
- ideia de Radial-Edge para non-manifold

Saber explicar:

- problema da redundancia em codificacao explicita
- por que adjacencia e importante
- vantagem de estruturas como Winged-Edge e Half-Edge
- limitacoes do Half-Edge para certos casos non-manifold

### CSG

Estudar:

- Constructive Solid Geometry
- representacao por arvore binaria
- folhas com primitivas
- nos internos com operacoes booleanas regularizadas e transformacoes
- armazenamento da historia de construcao e da intencao de projeto

Saber comparar B-rep x CSG:

- CSG e mais compacto e intuitivo para criacao
- CSG nao armazena diretamente os resultados intermediarios/finais
- B-rep facilita exibir a superficie explicitamente
- CSG preserva melhor a historia de construcao
- B-rep complica booleanas; CSG complica visualizacao direta

## 9. Prioridade muito alta: curvas suaves

### Formas de representacao de curvas

Estudar:

- arrays de coordenadas
- formulacoes implicitas
- formulacoes explicitas
- formulacoes parametrizadas
- formulacoes polinomiais, blending e matriciais
- curvas racionais x nao racionais

### Caracteristicas gerais das curvas

Estudar:

- interpoladoras x aproximadoras
- grau da curva
- controle local x global
- continuidade `C0`, `C1`, `C2`
- convex hull
- curvas abertas x fechadas
- curvas uniformes x nao uniformes

Saber explicar:

- o que muda quando aumenta o grau da curva
- por que `C1` e `C2` sao importantes em trajetorias suaves
- diferenca entre curva que passa pelos pontos e curva guiada pelos pontos

### Curvas de Hermite

Estudar:

- definicao por dois pontos e duas tangentes
- caracter interpolador
- forma matricial
- funcoes de ponderacao de Hermite

Saber fazer:

- identificar os dados de entrada: `P1`, `P2`, `T1`, `T2`
- entender que a tangente controla direcao e intensidade da curvatura
- reconhecer a formulacao `P(t) = T * H^-1 * G`

### Curvas de Bezier

Estudar:

- pontos de controle
- funcoes de Bernstein
- casos quadratico e cubico
- forma matricial
- convex hull
- controle global
- interpolacao apenas dos pontos extremos

Saber explicar:

- por que Bezier passa pelo primeiro e ultimo ponto, mas nao necessariamente pelos internos
- como as tangentes nas extremidades dependem dos pontos vizinhos
- problema de usar grau alto demais
- por que composicao de varias Bezier cubicas melhora controle local
- condicoes de continuidade entre segmentos

### B-splines

Estudar:

- generalizacao de Bezier
- curvas aproximadoras
- grau independente da quantidade de pontos de controle
- controle local
- funcoes de De Boor
- vetor de nos
- B-spline uniforme x nao uniforme
- continuidade associada aos nos

Saber explicar:

- vantagem principal sobre Bezier: controle local
- por que a curva normalmente nao passa pelos pontos de controle
- como nos nao uniformes permitem alterar continuidade e interpolar extremos

### NURBS

Estudar:

- Non-Uniform Rational B-Splines
- pesos nos pontos de controle
- forma racional
- coordenadas homogeneas
- representacao exata de conicas

Saber explicar:

- por que NURBS sao tao usadas em CAD
- diferenca entre B-spline comum e NURBS
- papel dos pesos na aproximacao da curva aos pontos de controle

### Catmull-Rom

Estudar pelo menos o basico:

- interpola os pontos de controle
- continuidade `C1`
- nao tem `C2`
- nao respeita convex hull

## 10. Prioridade alta: superficies

### Conceitos gerais

Estudar:

- por que superficies sao importantes para estetica, suavidade e formas organicas
- patches parametricos
- criacao de superficies por equacao analitica, nuvem de pontos/scanning e patches
- triangularizacao de superficies

### Patches de Bezier

Estudar:

- extensao bidimensional da Bezier
- superficie `C(u,v)`
- malha de controle `4x4` no caso cubico
- influencia da malha de pontos de controle
- controle global
- uniao de patches e continuidade entre eles

Saber explicar:

- por que a superficie interpola os cantos
- analogia entre curva Bezier e patch Bezier
- condicoes de continuidade `C0` e `C1` entre patches

### Patches B-spline

Estudar:

- semelhanca com patches de Bezier
- possibilidade de qualquer numero de pontos de controle em `u` e `v`
- continuidade melhor em curvas cubicas

### Rendering de patches

Estudar:

- renderizacao direta a partir da descricao parametrica
- aproximacao por malha de triangulos
- subdivisao uniforme
- subdivisao adaptativa
- calculo de normais por tangentes em `u` e `v` e produto vetorial

## 11. Prioridade media: objetos naturais e modelagem implicita

### Objetos naturais

Estudar:

- por que agua, fogo, fumaca, nuvens e plantas sao dificeis de modelar
- aproximacoes comuns em CG
- sistemas de particulas
- fractais
- L-systems para plantas
- simulacao de terrenos e canais

### Metaballs e representacao implicita

Estudar:

- equacoes implicitas
- isosuperficie
- ideia de blobby objects
- uso em animacoes com mudanca de forma

Esse bloco parece mais conceitual do que algoritimico nos slides.

## 12. Comparacoes que valem revisao final

Se eu fosse revisar na vespera, eu garantiria que consigo comparar:

- 2D raster x 2D vetorial x 2,5D x 3D
- wireframe x superficie x modelagem solida
- solido x nao solido x superficie
- instanciacao x parametrizacao x sweeping x modelagem topologica x booleanas
- B-rep x CSG
- Bezier x Hermite
- Bezier x B-spline
- B-spline x NURBS
- curva interpoladora x aproximadora
- controle global x controle local
- continuidade `C0`, `C1`, `C2`
- booleana comum x booleana regularizada

## 13. Perguntas que tem cara de prova

Treine responder, sem consultar material:

- O que caracteriza um modelo geometrico?
- Qual a diferenca entre geometria e topologia?
- Por que wireframe e ambiguo?
- O que faz uma representacao de solido ser valida?
- O que significa `closure` em modelagem solida?
- Para que servem coordenadas homogeneas?
- Qual a diferenca entre B-rep e CSG?
- O que sao operacoes booleanas regularizadas e por que elas sao necessarias?
- Qual a diferenca entre curvas interpoladoras e aproximadoras?
- Qual a diferenca entre Bezier, Hermite, B-spline e NURBS?
- O que significam `C0`, `C1` e `C2`?
- O que representa a formula de Euler e quais seus limites como validacao?
- O que sao objetos manifold e non-manifold?
- Como uma superficie parametrica pode ser renderizada?

## 14. Ordem sugerida de estudo

1. Matrizes, vetores e coordenadas homogeneas.
2. Conceitos de modelo, representacao e classificacao dos sistemas.
3. Wireframe, superficies e modelagem solida.
4. Propriedades de representacoes validas de solidos.
5. Metodos de criacao: instanciacao, parametrizacao, sweeping, topologica, booleanas.
6. Representacao de solidos: B-rep e CSG.
7. Topologia de poliedros e formula de Euler.
8. Curvas: Hermite, Bezier, B-spline, NURBS.
9. Superficies e patches.
10. Objetos naturais e modelagem implicita.

## 15. Resumo do que mais merece decoracao tecnica

Vale memorizar ou pelo menos reconhecer rapidamente:

- matrizes de translacao, rotacao e escala em 2D/3D
- conceito de coordenadas homogeneas
- produto escalar e produto vetorial
- formula de Euler e Euler-Poincare
- estrutura geral de arvore CSG
- ideia geral das estruturas Winged-Edge e Half-Edge
- definicao de Hermite, Bezier, B-spline e NURBS
- significados de `C0`, `C1` e `C2`
- definicao de booleana regularizada
