# Roteiro de estudos para 5 dias

Este cronograma foi montado a partir dos PDFs da pasta e do arquivo `roteiro-estudo-prova.md`.

Objetivo:

- cobrir os assuntos mais provaveis da prova em 5 dias
- revisar teoria e tambem treinar explicacao e comparacao entre conceitos
- deixar o ultimo dia mais focado em consolidacao e revisao ativa

Sugestao de ritmo diario:

- Bloco 1: 1h30 a 2h de teoria
- Bloco 2: 1h a 1h30 de resumo e mapa mental
- Bloco 3: 45min a 1h de exercicios, autoexplicacao ou revisao ativa

Se tiver menos tempo por dia, priorize sempre nesta ordem:

1. entender os conceitos centrais
2. saber comparar os metodos
3. memorizar formulas e propriedades

## Dia 1: base matematica e fundamentos de modelagem

### Objetivo do dia

Construir a base para o restante da materia. Sem isso, curvas, superficies, CSG e B-rep ficam mais dificeis.

### Estudar

- `00a - Revisao da Matematica - matrizes_V2.pdf`
- `00b - fundamentosMath__4_1_1.pdf`
- `05 - Revisao da Matematica - vetores e sistemas de coordenadas.pdf`
- `01 - O que eh um Modelo v3_6.pdf`

### Foco principal

- matrizes: soma, multiplicacao, dimensoes e composicao
- transformacoes 2D e 3D
- coordenadas homogeneas
- vetores: norma, normalizacao, produto escalar e vetorial
- reta e plano em forma parametrica
- ideia de modelo: abstracao, representacao, implementacao
- capacidades de criar, representar e analisar/simular

### O que voce precisa sair sabendo

- montar e reconhecer matrizes de translacao, rotacao e escala
- explicar por que a ordem das transformacoes altera o resultado
- usar produto escalar para angulo e perpendicularidade
- usar produto vetorial para normal
- explicar os niveis de abstracao de um modelo
- diferenciar sintaxe e semantica na representacao

### Revisao ativa do dia

Responda sem consultar:

- por que coordenadas homogeneas sao usadas?
- qual a diferenca entre produto escalar e vetorial?
- como representar uma reta parametrica?
- qual o papel de um modelo em computacao grafica/modelagem geometrica?

### Entrega do dia

Escreva uma folha-resumo com:

- formulas principais de vetores e matrizes
- tipos de transformacao
- definicao curta de modelo geometrico

## Dia 2: 2D, wireframe, solidos e metodos de criacao

### Objetivo do dia

Entender a evolucao dos modelos e por que modelagem solida foi necessaria.

### Estudar

- `03 - 2 e meio D wireframe.pdf`
- `04 - Def Sólidos e Nao Solidos v3_1_1.pdf`
- `06 - Modelagem de Solidos- Criacao Inst-Param-Sweep v6_3.pdf`

### Foco principal

- limitacoes do 2D e do pseudo-3D
- wireframe: vantagens e desvantagens
- diferenca entre solidos, superficies e nao solidos
- propriedades desejadas de uma representacao valida
- instanciacao
- parametrizacao
- sweeping: extrusao, revolucao, lofting

### O que voce precisa sair sabendo

- explicar por que wireframe e ambiguo
- justificar por que superfícies nao equivalem a solidos
- definir `closure`, validade, unicidade, nao ambiguidade, concisao e eficiencia
- comparar instanciacao, parametrizacao e sweeping
- explicar geratriz e diretriz
- citar problemas de sweeping, como auto-intersecao e degeneracao

### Revisao ativa do dia

Responda sem consultar:

- por que wireframe nao e suficiente para varias analises?
- quando modelagem solida se torna necessaria?
- qual a diferenca entre instanciacao e parametrizacao?
- o que e um sweeping translacional e um rotacional?

### Entrega do dia

Monte uma tabela comparando:

- wireframe x superficie x modelagem solida
- instanciacao x parametrizacao x sweeping

## Dia 3: topologia, poliedros, booleanas e CSG

### Objetivo do dia

Cobrir a parte mais estrutural da modelagem solida e um dos blocos mais fortes para prova conceitual.

### Estudar

- `08 - Modelagem de Solidos - Criacao Topológica v7_2_1.pdf`
- `09 - Modelagem de Solidos  - Criacao Booleana v9_2.pdf`
- `12 - Representa Solidos CSG v5_2.pdf`

### Foco principal

- geometria x topologia
- conectividade e continuidade
- manifold e orientabilidade
- poliedros simples
- formula de Euler
- formula de Euler-Poincare
- validacao de poliedros
- operacoes booleanas regularizadas
- estrutura de arvore CSG

### O que voce precisa sair sabendo

- explicar diferenca entre propriedade geometrica e topologica
- aplicar `V - E + F = 2`
- entender `V - E + F - H = 2(C - G)`
- explicar por que a formula de Euler sozinha nao valida tudo
- explicar por que booleanas comuns podem falhar
- definir booleana regularizada
- descrever como CSG armazena historia de construcao e intencao de projeto

### Revisao ativa do dia

Responda sem consultar:

- o que e um objeto `2-manifold`?
- por que a regularizacao e necessaria nas booleanas?
- o que representa uma arvore CSG?
- uniao, interseccao e diferenca sao comutativas?

### Entrega do dia

Escreva mini-respostas de 4 a 6 linhas para:

- Boleana comum x boleana regularizada
- Topologia x geometria
- Formula de Euler x validacao completa
- CSG x outros esquemas de criacao

## Dia 4: B-rep, curvas suaves e superfícies

### Objetivo do dia

Cobrir a outra metade mais forte da prova: representacao de solidos, curvas e superficies.

### Estudar

- `11 - Modelagem de Solidos - representa Brep v7_4_4.pdf`
- `15 - Curvas Suaves v6_2_1_8.pdf`
- `15_1-Curvas_Suaves_Hermite_V7_1_4.pdf`
- `16 - Superfícies v3_2.pdf`

### Foco principal

- definicao de B-rep
- B-rep poliedrico x generalizado
- adjacencias e estruturas de dados
- Winged-Edge e Half-Edge
- curvas interpoladoras x aproximadoras
- continuidade `C0`, `C1`, `C2`
- Hermite, Bezier, B-spline e NURBS
- patches de Bezier e B-spline
- rendering de patches

### O que voce precisa sair sabendo

- comparar B-rep e CSG
- explicar por que adjacencias sao importantes em B-rep
- saber a intuicao de Winged-Edge e Half-Edge
- diferenciar Hermite, Bezier, B-spline e NURBS
- diferenciar controle global e local
- explicar continuidade `C0`, `C1` e `C2`
- explicar como patches geram superficies suaves
- explicar renderizacao por discretizacao em triangulos

### Revisao ativa do dia

Responda sem consultar:

- qual a diferenca central entre B-rep e CSG?
- por que Bezier tem controle global?
- por que B-spline costuma ser mais flexivel que Bezier?
- o que NURBS adiciona sobre B-spline?
- como calcular normal de uma superficie parametrica?

### Entrega do dia

Monte duas tabelas:

- B-rep x CSG
- Hermite x Bezier x B-spline x NURBS

## Dia 5: consolidacao, objetos naturais e simulado final

### Objetivo do dia

Consolidar tudo, revisar pontos fracos e treinar resposta de prova.

### Estudar

- `02 - Objetos Naturais v3_2.pdf`
- revisao dos resumos dos dias 1 a 4
- `roteiro-estudo-prova.md`

### Foco principal

- objetos naturais: agua, fogo, fumaca, nuvens, plantas
- L-systems, particulas, fractais, metaballs
- modelagem implicita e isosuperficies
- grandes comparacoes da disciplina
- formulas e definicoes-chave

### Revisao final obrigatoria

Voce precisa revisar de novo:

- produto escalar e vetorial
- transformacoes e coordenadas homogeneas
- wireframe x superficie x solido
- instanciacao x parametrizacao x sweeping x booleanas x topologica
- B-rep x CSG
- Euler e Euler-Poincare
- Hermite x Bezier x B-spline x NURBS
- `C0`, `C1`, `C2`
- booleanas regularizadas

### Simulado oral/escrito

Tente responder em voz alta ou por escrito:

1. O que torna uma representacao de solido valida?
2. Por que wireframe e ambiguo?
3. Qual a diferenca entre B-rep e CSG?
4. O que e uma operacao booleana regularizada?
5. O que a formula de Euler valida e o que ela nao valida sozinha?
6. Diferencie Hermite, Bezier, B-spline e NURBS.
7. Explique continuidade `C0`, `C1` e `C2`.
8. Como superficies parametrizadas sao renderizadas?

### Fechamento do dia

Separe os topicos em 3 grupos:

- sei bem
- sei mais ou menos
- preciso revisar antes da prova

Releia apenas o terceiro grupo no fim do dia.

## Prioridade se o tempo apertar

Se nao conseguir estudar tudo com profundidade, foque primeiro em:

1. vetores, matrizes, transformacoes e coordenadas homogeneas
2. wireframe x superficies x solidos
3. propriedades de representacoes validas
4. booleanas regularizadas
5. B-rep x CSG
6. Euler e topologia basica
7. Bezier, B-spline, NURBS e continuidade
8. superficies por patches

## Estrategia pratica para memorizar melhor

Todo dia, no final, faca 3 coisas:

1. escreva 10 perguntas curtas sobre o que estudou
2. responda sem olhar o material
3. marque em vermelho o que travou

No dia seguinte, revise primeiro os itens em vermelho antes de continuar.
