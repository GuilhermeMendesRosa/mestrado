# Simulado teorico com 100 questoes

Este simulado foi montado com foco teorico, seguindo os PDFs da pasta e os roteiros ja criados.

Como usar:

1. Tente responder as 100 questoes sem olhar as respostas.
2. Marque as que voce nao souber ou responder com inseguranca.
3. Corrija pelo gabarito e revise os temas em que mais errou.


## Questoes com respostas

### Bloco A: fundamentos, matematica e representacao

1. O que e um modelo em modelagem geometrica?
Resposta: E uma representacao abstrata de um objeto real ou matematico, feita para permitir criacao, representacao, analise e simulacao.

2. Quais sao os niveis de abstracao apresentados nos slides sobre modelos?
Resposta: Mundo fisico, modelo matematico, representacao e implementacao.

3. Qual a diferenca entre sintaxe e semantica na representacao de um objeto?
Resposta: Sintaxe e a forma de descrever os elementos; semantica e o significado desses elementos.

4. Quais sao as tres capacidades centrais de um modelo segundo os slides?
Resposta: Criar, representar e analisar/simular.

5. Por que um modelo nao deve servir apenas para desenhar um objeto?
Resposta: Porque o modelo tambem deve permitir armazenamento significativo, alteracao, simulacao, analise e uso computacional posterior.

6. Qual a diferenca entre dominio raster e dominio vetorial em sistemas graficos 2D?
Resposta: Raster representa por pixels/imagem; vetorial representa por entidades geometricas descritas matematicamente.

7. O que caracteriza um sistema 2,5D?
Resposta: E uma extensao do 2D que sugere informacao 3D, mas sem representar plenamente um solido 3D integro.

8. Por que modelos 2D e pseudo-3D podem gerar ambiguidades de interpretacao?
Resposta: Porque faltam informacoes completas de profundidade, interior/exterior e estrutura espacial, exigindo interpretacao humana.

9. O que e um vetor e quais sao suas propriedades geometricas basicas?
Resposta: E um ente matematico que representa direcao e magnitude, sem posicao fixa quando tratado como vetor livre.

10. O que significa normalizar um vetor?
Resposta: Tornar o vetor unitario, dividindo-o por sua magnitude.

11. Para que serve o produto escalar em computacao grafica?
Resposta: Para medir alinhamento angular, calcular angulos, projecoes e testar perpendicularidade.

12. O que indica um produto escalar igual a zero entre dois vetores?
Resposta: Que os vetores sao perpendiculares.

13. Para que serve o produto vetorial em computacao grafica e modelagem?
Resposta: Para obter um vetor perpendicular a dois outros, muito usado no calculo de normais.

14. O que a regra da mao direita define no produto vetorial?
Resposta: Define o sentido do vetor resultante do produto vetorial.

15. O que e uma base vetorial?
Resposta: E um conjunto de vetores linearmente independentes capaz de gerar um espaco por combinacoes lineares.

16. O que significa dizer que um conjunto de vetores e linearmente independente?
Resposta: Que nenhum vetor do conjunto pode ser escrito como combinacao linear dos outros.

17. Como a equacao parametrica de uma reta e interpretada geometricamente?
Resposta: Como o conjunto de pontos obtidos a partir de um ponto inicial e um vetor diretor variando um parametro.

18. Como um plano pode ser definido a partir de um ponto e um vetor normal?
Resposta: Um ponto pertence ao plano se o vetor ate ele for perpendicular ao vetor normal, isto e, satisfizer a equacao com produto escalar zero.

19. Por que matrizes sao importantes em computacao grafica?
Resposta: Porque permitem representar e compor transformacoes geometricas de forma compacta e eficiente.

20. Por que a ordem das multiplicacoes de matrizes importa em sequencias de transformacao?
Resposta: Porque multiplicacao matricial nao e comutativa; mudar a ordem muda o resultado final.

### Bloco B: transformacoes, wireframe, solidos e propriedades das representacoes

21. O que sao coordenadas homogeneas e por que elas sao usadas?
Resposta: Sao coordenadas com um componente extra que permitem representar translacoes e compor transformacoes lineares e afins numa unica forma matricial.

22. Qual a vantagem de representar varias transformacoes por uma unica matriz composta?
Resposta: Reduz custo computacional e simplifica a aplicacao repetida das mesmas transformacoes a muitos pontos.

23. Como se faz conceitualmente uma rotacao em torno de um ponto pivor?
Resposta: Traduzir o objeto ate o pivor ir para a origem, rotacionar e depois traduzir de volta.

24. O que e um modelador wireframe?
Resposta: E um modelador que representa objetos por pontos, arestas, arcos e curvas no espaco, sem descrever completamente o interior do solido.

25. Quais sao as principais vantagens do wireframe?
Resposta: Simplicidade, rapidez de visualizacao, baixo custo computacional e pouca memoria.

26. Quais sao as principais desvantagens do wireframe?
Resposta: Ambiguidade, dependencia de interpretacao humana, baixa capacidade de analise e falta de validacao consistente.

27. Por que wireframe e considerado ambiguo?
Resposta: Porque a mesma estrutura de arames pode sugerir mais de um objeto 3D.

28. Qual a diferenca entre solido, superficie e nao solido?
Resposta: Solido tem interior, fronteira e volume; superficie nao tem volume; nao solido inclui casos nao integrais ou non-manifold.

29. Por que uma colecao de superficies nao garante necessariamente um solido valido?
Resposta: Porque elas podem nao fechar um volume, nao ser orientaveis corretamente ou nao delimitar interior e exterior de modo consistente.

30. Em que situacoes a modelagem solida se torna necessaria ou suficiente?
Resposta: Quando e importante distinguir interior e exterior, validar integridade e calcular propriedades como volume, massa e interferencias.

31. O que significa dizer que uma representacao de solidos deve ser nao ambigua?
Resposta: Que cada representacao deve corresponder a um unico solido, sem duvidas sobre o objeto representado.

32. O que significa `closure` em modelagem solida?
Resposta: Que as operacoes sobre o esquema devem produzir novamente objetos validos do mesmo dominio.

33. O que significa unicidade de representacao?
Resposta: Que um mesmo objeto tenha uma unica representacao dentro do esquema, ou ao menos nao gere ambiguidades de representacao.

34. O que significa validade em um esquema de representacao de solidos?
Resposta: Que o modelo respeita as regras geometricas e topologicas necessarias para representar um solido coerente.

35. O que significa homogeneidade dimensional em um modelo solido?
Resposta: Que o objeto nao mistura elementos de dimensoes inadequadas, como partes pendentes sem interior correspondente.

36. O que significa concisao em um esquema de representacao?
Resposta: Capacidade de representar com poucos dados relevantes, economizando armazenamento.

37. O que significa eficiencia em um esquema de representacao?
Resposta: Facilidade e rapidez para visualizar, analisar e processar o modelo computacionalmente.

38. O que significa precisao ou fidelidade em um esquema de representacao?
Resposta: Capacidade de representar o objeto sem aproximacoes indevidas ou com alta fidelidade ao real.

39. Por que uma representacao ambigua e considerada catastrofica em CAD/CAM?
Resposta: Porque inviabiliza fabricacao automatica, simulacao confiavel e tomada de decisoes corretas pelo sistema.

40. Qual a diferenca entre propriedade geometrica e propriedade topologica?
Resposta: Geometria trata de medidas, formas, angulos e distancias; topologia trata de conectividade e continuidade.

### Bloco C: metodos de criacao de solidos

41. O que e instanciacao na criacao de solidos?
Resposta: E a criacao de copias modificadas de primitivas padrao por transformacoes de tamanho, posicao e orientacao.

42. Quais sao as primitivas mais comuns citadas nos slides de instanciacao?
Resposta: Cubo, cilindro, esfera, toro, cone e cunha/calco.

43. Quais informacoes uma instancia precisa guardar sobre o objeto?
Resposta: O que o objeto e, onde esta e como esta orientado, alem dos parametros proprios da primitiva.

44. Por que se diz que instanciacao altera a geometria, mas nao a topologia?
Resposta: Porque muda forma, tamanho, posicao ou orientacao, mas nao altera a estrutura de conectividade do objeto.

45. Qual a principal vantagem da instanciacao?
Resposta: Compacidade, precisao e bom desempenho.

46. Qual a principal limitacao da instanciacao?
Resposta: Dominio muito restrito, pois depende de primitivas predefinidas.

47. O que e parametrizacao na criacao de solidos?
Resposta: E a geracao de objetos a partir de parametros de alto nivel que descrevem uma familia de formas.

48. Como a parametrizacao generaliza a instanciacao?
Resposta: Porque nao fica limitada apenas a TGLR e pode descrever objetos mais complexos e variacoes topologicas.

49. Por que a parametrizacao e util para familias de objetos?
Resposta: Porque o mesmo esquema parametrico pode gerar varias variantes de um mesmo tipo de objeto.

50. Qual a principal limitacao compartilhada por instanciacao e parametrizacao?
Resposta: Nao definem bem como combinar objetos livremente para criar outros mais complexos e exigem solucoes especificas de visualizacao/analise.

51. O que e sweeping ou varredura?
Resposta: E a criacao de um objeto varrendo uma geratriz ao longo de uma diretriz no espaco.

52. O que sao geratriz e diretriz em sweeping?
Resposta: Geratriz e o elemento base que sera varrido; diretriz e a trajetoria ou regra do movimento dessa geratriz.

53. O que e uma extrusao translacional?
Resposta: E varrer uma forma ao longo de uma translacao, produzindo por exemplo um solido extrudado.

54. O que e uma varredura rotacional?
Resposta: E girar uma geratriz em torno de um eixo, criando um objeto de revolucao.

55. O que e lofting?
Resposta: E a construcao de uma superficie ou solido interpolando secoes transversais ao longo de um eixo.

56. Como o sweeping pode ser usado em reconstrucao 3D por secoes planares?
Resposta: Interpolando varias curvas de secoes planas medidas para reconstruir um volume ou superficie 3D.

57. Cite dois problemas classicos de sweeping generalizado.
Resposta: Auto-intersecao e geracao de objetos degenerados ou sem homogeneidade dimensional.

58. Por que se diz que sweeping nao e necessariamente fechado sob operacoes booleanas?
Resposta: Porque a uniao de dois objetos gerados por sweeping nao precisa resultar em outro objeto que possa ser descrito pelo mesmo esquema de sweeping.

59. O que e modelagem topologica poliedrica?
Resposta: E a criacao de solidos polihedricos a partir de seus constituintes topologicos, como faces, arestas e vertices.

60. Qual a ideia geral dos operadores de Euler nesse contexto?
Resposta: Construir e destruir elementos mantendo a validade topologica do solido polihedrico.

### Bloco D: topologia, poliedros, booleanas, CSG e B-rep

61. O que a topologia estuda, em contraste com a geometria?
Resposta: Estuda conectividade e continuidade preservadas sob deformacoes sem rasgo ou auto-intersecao, e nao medidas metricas.

62. O que e um poliedro, segundo a definicao apresentada nos slides?
Resposta: E um solido composto por poligonos planares organizados de modo consistente, com compartilhamento adequado de arestas.

63. O que caracteriza um objeto `2-manifold`?
Resposta: Que toda vizinhanca suficientemente pequena de seus pontos se comporta topologicamente como um disco.

64. O que significa orientabilidade de uma superficie?
Resposta: Que e possivel definir consistentemente um lado frontal e um traseiro ao longo da superficie.

65. O que diz a formula de Euler para poliedros simples?
Resposta: Que para poliedros simples vale `V - E + F = 2`.

66. Quais elementos aparecem na formula de Euler-Poincare apresentada nos slides?
Resposta: Vertices `V`, arestas `E`, faces `F`, buracos em faces `H`, conjuntos/cascas `C` e genus `G`.

67. O que representa `H` na formula de Euler-Poincare?
Resposta: Numero de holes, isto e, buracos em faces ou aneis.

68. O que representa `G` na formula de Euler-Poincare?
Resposta: Numero de furos que atravessam o objeto, o genus.

69. O que representa `C` na formula de Euler-Poincare?
Resposta: Numero de componentes ou cascas disjuntas consideradas no objeto.

70. Por que a formula de Euler, sozinha, nao basta para validar um poliedro?
Resposta: Porque um objeto pode satisfazer a formula e ainda violar restricoes geometricas ou topologicas locais.

71. Cite restricoes extras de validacao de poliedros alem da formula de Euler.
Resposta: Cada aresta deve ligar dois vertices, ser compartilhada por duas faces, pelo menos tres arestas devem chegar a um vertice e faces nao podem se interpenetrar.

72. O que sao operacoes booleanas em modelagem solida?
Resposta: Sao operacoes de uniao, interseccao e diferenca entre objetos para formar novas formas.

73. Quais operacoes booleanas sao comutativas e qual nao e?
Resposta: Uniao e interseccao sao comutativas; diferenca nao e.

74. Qual o problema das operacoes booleanas canonicas em solidos?
Resposta: Elas podem gerar resultados invalidos, com partes pendentes ou heterogeneidade dimensional.

75. O que sao operacoes booleanas regularizadas?
Resposta: Sao booleanas definidas para solidos validos que produzem sempre outro solido valido, garantindo `closure`.

76. O que significa a expressao `closure(interior(A op B))`?
Resposta: Significa tomar a operacao booleana, considerar apenas o interior valido do resultado e depois fechar esse interior com sua fronteira apropriada.

77. O que sao dangling parts ou heterogeneidade dimensional?
Resposta: Partes de fronteira sem interior adjacente, como arestas ou faces pendentes, que quebram a integridade dimensional do objeto.

78. Por que a regularizacao e importante para manter solidos validos?
Resposta: Porque remove resultados degenerados e garante que o resultado continue sendo um solido coerente.

79. Como a operacao de diferenca regularizada se relaciona com o complemento?
Resposta: A diferenca regularizada pode ser vista como interseccao com o complemento regularizado do outro objeto.

80. O que e CSG?
Resposta: E a Geometria Solida Construtiva, um esquema que representa objetos pela composicao hierarquica de primitivas com transformacoes e booleanas.

81. Como um modelo CSG e normalmente estruturado?
Resposta: Como uma arvore binaria ou, em extensoes, um grafo aciclico dirigido.

82. O que fica nos nos internos e nas folhas de uma arvore CSG?
Resposta: Nos internos guardam operacoes booleanas regularizadas e transformacoes; folhas guardam primitivas.

83. O que significa dizer que CSG armazena a historia de construcao do objeto?
Resposta: Que o modelo registra como o objeto foi montado passo a passo, e nao apenas a forma final explicitada.

84. Qual a principal vantagem conceitual de CSG?
Resposta: Compacidade e preservacao das intencoes de projeto.

85. Qual a principal dificuldade de CSG em relacao a visualizacao?
Resposta: A forma final nao esta explicitamente armazenada como malha ou fronteira pronta, tornando visualizacao e colorizacao mais custosas.

86. O que e B-rep?
Resposta: E a representacao por fronteira do solido, descrevendo-o por suas superficies limitantes organizadas.

87. O que diferencia B-rep poliedrico de B-rep generalizado?
Resposta: O poliedrico usa faces planas e arestas retas; o generalizado admite patches suaves e arestas curvas.

88. Que condicoes as superficies limitantes devem satisfazer em uma B-rep valida?
Resposta: Devem ser fechadas, orientaveis, nao auto-intersectantes, conectadas e realmente limitantes do objeto.

89. Por que adjacencia e uma informacao importante em B-rep?
Resposta: Porque muitas operacoes dependem de saber quais faces, arestas e vertices incidem uns nos outros.

90. Qual o principal problema da codificacao explicita de faces por coordenadas?
Resposta: Redundancia de dados e dificuldade de manter consistencia, pois vertices compartilhados podem ser duplicados.

### Bloco E: curvas, superficies e objetos naturais

91. Qual a diferenca entre curva interpoladora e curva aproximadora?
Resposta: Interpoladora passa pelos pontos de descricao; aproximadora usa os pontos para guiar a forma, sem necessariamente passar por eles.

92. O que significam continuidade `C0`, `C1` e `C2`?
Resposta: `C0` garante conexao de pontos; `C1` garante continuidade de tangente; `C2` garante continuidade de curvatura.

93. O que e convex hull e qual sua importancia para curvas como Bezier?
Resposta: E o menor conjunto convexo que contem os pontos de controle; em Bezier ajuda a prever a regiao onde a curva ficara.

94. Qual a diferenca entre controle local e controle global de uma curva?
Resposta: Controle global significa que mover um ponto afeta grande parte da curva; controle local afeta apenas uma regiao limitada.

95. Qual e a ideia central da curva de Hermite?
Resposta: Definir uma curva interpoladora a partir de pontos extremos e tangentes nas extremidades.

96. Qual a principal diferenca conceitual entre Hermite e Bezier?
Resposta: Hermite usa pontos extremos e tangentes; Bezier usa pontos de controle.

97. Quais sao as caracteristicas principais das curvas de Bezier?
Resposta: Passam pelo primeiro e ultimo ponto, usam funcoes de Bernstein, ficam no convex hull e possuem controle global.

98. O que caracteriza uma B-spline?
Resposta: E uma curva aproximadora baseada em funcoes de De Boor, com grau independente do numero de pontos de controle e controle local.

99. O que sao NURBS e por que sao muito usadas em CAD?
Resposta: Sao Non-Uniform Rational B-Splines; sao muito usadas em CAD por unirem controle local, flexibilidade, pesos e representacao exata de conicas.

100. Quais sao as duas formas gerais de renderizar patches citadas nos slides?
Resposta: Renderizacao direta da descricao parametrica ou aproximacao por malha de triangulos.

