# Simulado teórico com 50 questões — P2

Este simulado foi montado com foco teórico, seguindo os tópicos da P2 e o roteiro de estudo.

Como usar:
1. Tente responder as 50 questões sem olhar as respostas.
2. Marque as que você não souber ou responder com insegurança.
3. Corrija pelo gabarito e revise os temas em que mais errou.

---

## Questões com respostas

### Bloco A: Interoperabilidade e Padrões de Troca de Dados (Questões 1–18)

1. Qual o problema fundamental que os padrões de troca de dados CAD tentam resolver?
Resposta: Permitir que diferentes softwares CAD/CAM/CAE troquem informações de produto sem perda de significado, já que cada sistema tem seu formato interno proprietário.

2. Compare a abordagem de tradutor direto (point-to-point) com a de arquivo neutro. Qual a principal vantagem do arquivo neutro?
Resposta: No tradutor direto, cada par de sistemas precisa de um conversor próprio (N*(N-1) tradutores para N sistemas). No arquivo neutro, cada sistema só precisa exportar/importar de um formato comum (2N conversores). A principal vantagem é a escalabilidade e facilidade de manutenção.

3. Por que um arquivo neutro geralmente é maior que um formato nativo de CAD?
Resposta: Porque o formato neutro precisa ser abrangente o suficiente para representar dados de qualquer sistema, incluindo informações que um sistema específico pode não usar. Ele carrega redundâncias e metadados extras para garantir que nenhum dado se perca na tradução.

4. O que foi o programa ICAM e qual sua importância histórica para troca de dados CAD?
Resposta: O Integrated Computer-Aided Manufacturing foi um programa da Força Aérea dos EUA nos anos 1970 visando integrar design e manufatura computacionalmente. Sua importância foi ter impulsionado a criação dos primeiros padrões de troca de dados (como o IGES) ao evidenciar a necessidade de interoperabilidade.

5. O que é o padrão IGES e qual sua principal limitação?
Resposta: IGES (Initial Graphics Exchange Specification) é um padrão ANSI de 1980 para troca de dados CAD. Sua principal limitação é trocar apenas informação geométrica (curvas, superfícies, wireframe), sem capturar a semântica do produto — materiais, tolerâncias, estrutura de montagem, intenção de projeto.

6. O que é o padrão VDA-FS e em que contexto industrial ele surgiu?
Resposta: VDA-FS (Verband der Automobilindustrie — Flächenschnittstelle) é um padrão da indústria automotiva alemã focado na troca de dados de superfícies de forma livre. Surgiu da necessidade das montadoras alemãs trocarem dados de carroceria com fornecedores.

7. Qual a diferença fundamental entre STEP e IGES? Por que isso é relevante?
Resposta: IGES troca apenas geometria (é um "desenho" matemático). STEP (ISO 10303) troca informação completa de produto: geometria + estrutura + materiais + tolerâncias + ciclo de vida + manufatura. É relevante porque um modelo STEP é computacionalmente interpretável por sistemas de manufatura, análise e gestão, enquanto um arquivo IGES precisa de interpretação humana para ter significado.

8. Descreva a arquitetura de três camadas do STEP.
Resposta: (1) Description Methods: linguagem EXPRESS e esquemas de modelagem para definir estruturas de dados. (2) Integrated Resources: bibliotecas reutilizáveis de definições (geometria, topologia, materiais, tolerâncias). (3) Application Protocols (APs): definem o subconjunto do modelo STEP necessário para um domínio específico (ex: AP203 para design mecânico, AP214 para automotivo).

9. O que é um Application Protocol (AP) no STEP? Cite três exemplos e seus domínios.
Resposta: Um AP define quais partes do modelo STEP são relevantes para um domínio de aplicação específico. Exemplos: AP203 (design 3D com controle de configuração), AP214 (design automotivo), AP242 (engenharia 3D baseada em modelo — unificou AP203 e AP214), AP224 (planejamento baseado em features).

10. O que é a linguagem EXPRESS e para que ela serve no contexto do STEP?
Resposta: EXPRESS (ISO 10303-11) é uma linguagem de modelagem de dados para especificar a estrutura e as restrições dos modelos de produto. Não é uma linguagem de programação — é uma linguagem de especificação que define entidades, atributos, relações e regras (WHERE). Sua notação gráfica é a EXPRESS-G.

11. Qual o papel do SDAI (Standard Data Access Interface) na arquitetura STEP?
Resposta: O SDAI (ISO 10303-22) é uma API padronizada que permite a aplicações acessar e manipular dados STEP programaticamente (ler, escrever, consultar), sem precisar conhecer o formato físico do arquivo. É a camada de acesso que torna os dados STEP consumíveis por software.

12. Quais os três domínios de um modelo de produto (Product Model)? Explique cada um.
Resposta: (1) Domínio Estrutural: estrutura de montagem, BOM (lista de materiais), relações entre componentes, versões. (2) Domínio Geométrico: forma, dimensões, posição, representações CSG ou B-rep. (3) Domínio de Conhecimento: regras de projeto, restrições, intenções de design, tolerâncias. Um Integrated Product Model combina os três.

13. Por que armazenar apenas geometria não é suficiente para ter um modelo de produto completo?
Resposta: Porque geometria sozinha não informa materiais, tolerâncias, processos de fabricação, relações funcionais entre peças, ou a razão de ser de cada elemento. Sem isso, análise, simulação e manufatura automatizada ficam inviáveis ou propensas a erro.

14. O que significa verificação de conformidade no contexto do STEP?
Resposta: É a capacidade de validar automaticamente se um arquivo STEP está em conformidade com o schema definido (EXPRESS), verificando se todas as entidades, atributos e restrições obrigatórias estão presentes e corretas. Isso reduz erros de interpretação humana na troca de dados.

15. O que é STEP-NC e como ele difere do código G tradicional?
Resposta: STEP-NC (ISO 14649) é uma extensão do STEP para comando numérico. Enquanto o código G tradicional envia instruções de baixo nível (movimentos de eixo, coordenadas), o STEP-NC envia informação de alto nível (features, operações, tolerâncias), permitindo que a máquina CNC "entenda" o que está usinando e possa otimizar o processo.

16. O que é o padrão SET e como ele se relaciona com o STEP?
Resposta: SET (Standard d'Échange et de Transfert) foi um padrão francês de troca de dados, competidor e precursor do STEP. Assim como o IGES, era focado principalmente em geometria, e o STEP foi desenvolvido como evolução para superar as limitações tanto do IGES quanto do SET.

17. Por que a indústria automotiva alemã desenvolveu seu próprio padrão (VDA-FS) em vez de usar o IGES?
Resposta: Porque o IGES, sendo um padrão geral, não atendia bem às necessidades específicas da indústria automotiva para troca de superfícies de forma livre (curvas e superfícies complexas de carroceria). O VDA-FS foi otimizado para esse tipo de geometria.

18. Qual a importância da integração CAD-CAM via STEP para a manufatura moderna?
Resposta: Permite que o modelo de design (CAD) alimente diretamente o planejamento e a execução da manufatura (CAM/CNC) sem perda de informação ou necessidade de reprogramação manual. Isso reduz erros, tempo de setup e permite manufatura adaptativa baseada no modelo de produto completo.

---

### Bloco B: Modelagem Paramétrica, Variacional e Restrições (Questões 19–35)

19. O que é Design Intent (intenção de projeto) e por que ele é crucial na modelagem paramétrica?
Resposta: Design Intent é o conjunto de regras, relações e restrições que capturam o raciocínio do projetista embutido no modelo. É crucial porque permite que o modelo se comporte de forma previsível quando modificado — as alterações respeitam automaticamente as regras de projeto, em vez de "quebrar" a geometria.

20. Dê um exemplo concreto de Design Intent em uma peça mecânica.
Resposta: Em um flange com furos, o Design Intent pode incluir: "os furos devem estar igualmente espaçados em um círculo concêntrico ao flange" e "o diâmetro dos furos deve ser 1/3 do diâmetro do flange". Se o diâmetro do flange mudar, os furos se reposicionam e redimensionam automaticamente.

21. O que é uma família de peças (Family of Parts)? Relacione com o conceito de instancing do Mortenson.
Resposta: Uma família de peças é um modelo paramétrico que gera múltiplas variantes alterando parâmetros (ex: parafusos M6, M8, M10 a partir do mesmo modelo base). Relaciona-se com instancing (Mortenson Cap. 10) porque em ambos os casos uma definição base é reutilizada com parâmetros diferentes, evitando recriar a geometria do zero.

22. Qual a diferença fundamental entre modelagem paramétrica e modelagem variacional?
Resposta: Na modelagem paramétrica, as dependências têm direção definida e seguem uma ordem de avaliação (ex: L2 = L1 + 10 — L1 determina L2, não o contrário). Na modelagem variacional, todas as equações são resolvidas simultaneamente, sem direção preferencial — o solver encontra solução que satisfaça todas as restrições juntas.

23. Dê um exemplo que ilustre a diferença entre paramétrico e variacional.
Resposta: Paramétrico: "Largura = 100, Altura = Largura/2" — se mudar Largura, Altura atualiza; se mudar Altura, Largura não muda. Variacional: "Largura + Altura = 300 e Largura = 2*Altura" — o sistema resolve ambas juntas; não importa qual você tenta mudar, o solver garante que ambas as equações sejam satisfeitas.

24. O que é uma restrição geométrica? Dê três exemplos.
Resposta: É uma restrição que define uma relação espacial entre entidades geométricas. Exemplos: paralelismo entre duas linhas, tangência entre um arco e uma reta, distância fixa entre dois pontos, concentricidade entre dois círculos, perpendicularidade.

25. O que é uma restrição funcional (ou de engenharia)? Como ela difere de uma restrição geométrica?
Resposta: É uma restrição baseada em requisitos de desempenho do produto (física, engenharia), não apenas em relações espaciais. Exemplos: tensão máxima ≤ σ_adm, deflexão ≤ 1 mm, peso total ≤ 5 kg. Difere da geométrica porque conecta a geometria com análise de engenharia, exigindo avaliação de propriedades físicas.

26. O que caracteriza uma restrição variacional? Em que situação ela é útil?
Resposta: Restrições variacionais usam desigualdades (intervalos) em vez de igualdades, definindo um espaço de soluções viáveis. Exemplo: "comprimento entre 50 e 100 mm". São úteis em projeto preliminar e otimização, quando os valores exatos ainda não estão definidos, mas os limites aceitáveis sim.

27. Por que restrições funcionais são mais complexas de implementar que restrições geométricas?
Resposta: Porque exigem integração com modelos de análise (FEM, CFD, etc.) e propriedades de material, não apenas relações geométricas. Enquanto uma restrição geométrica é puramente matemática (equações algébricas), uma restrição funcional pode exigir simulação numérica para ser avaliada.

28. Qual a diferença entre uma abordagem procedural e uma abordagem baseada em restrições (constraint-based) para modelagem?
Resposta: Na procedural, define-se uma sequência de operações para construir a geometria (como programação imperativa). Na baseada em restrições, declara-se o que se deseja (relações e condições) e o sistema resolve automaticamente (como programação declarativa). A procedural tem ordem fixa; a constraint-based é flexível mas exige um solver.

29. Como um grafo de restrições representa um problema de modelagem?
Resposta: Os elementos geométricos são representados como nós do grafo. As restrições entre eles são representadas como arestas. Por exemplo: linha L1 (nó) —[paralelo]— linha L2 (nó) —[distância=50]— linha L3 (nó). O grafo permite analisar dependências, detectar redundâncias e planejar a ordem de resolução.

30. O que é um predicado no contexto de restrições geométricas?
Resposta: Um predicado é uma condição lógica que deve ser verdadeira para que o modelo seja válido. Exemplo: "a distância entre os pontos P1 e P2 é igual a d" é um predicado que a geometria deve satisfazer.

31. O que caracteriza um sistema sub-restrito (under-constrained)? Qual a consequência prática?
Resposta: Um sistema tem mais graus de liberdade (variáveis) que equações (restrições), ou seja, há infinitas soluções que satisfazem as restrições. A consequência prática é que a geometria não fica completamente determinada — o modelo pode "flutuar" e se comportar de forma imprevisível quando editado.

32. O que caracteriza um sistema sobre-restrito (over-constrained)? Qual a consequência prática?
Resposta: Um sistema tem mais restrições que graus de liberdade, podendo ter equações contraditórias. A consequência prática é que o solver pode falhar ou gerar resultados incorretos, e o software pode alertar sobre restrições redundantes ou conflitantes.

33. O que é uma função implícita e quando ela é usada na modelagem?
Resposta: É uma função na forma F(x, y, z, ...) = 0 que define uma relação sem isolar uma variável. Exemplo: x² + y² - R² = 0 (círculo). É útil quando não é possível ou conveniente isolar uma variável (ex: superfícies complexas, curvas de interseção), mas é mais difícil de avaliar computacionalmente que a forma explícita.

34. Por que a resolução de sistemas de equações simultâneas é um desafio computacional na modelagem variacional?
Resposta: Porque (1) os sistemas podem ser não-lineares, exigindo métodos numéricos iterativos (Newton-Raphson); (2) pode haver múltiplas soluções, sendo necessário escolher a correta; (3) restrições redundantes ou inconsistentes precisam ser detectadas e tratadas; (4) o sistema pode ser grande (centenas de restrições) e precisa ser resolvido em tempo interativo.

35. Como os conceitos de instancing e primitivas paramétricas do Mortenson (Cap. 10) se relacionam com modelagem paramétrica moderna?
Resposta: O instancing paramétrico do Mortenson — criar variações de primitivas alterando parâmetros (dimensões, posição, orientação) — é a ideia fundamental que evoluiu para a modelagem paramétrica moderna. A diferença é que o instancing do Mortenson é limitado a primitivas predefinidas, enquanto a modelagem paramétrica moderna estende o conceito para geometria arbitrária com restrições complexas.

---

### Bloco C: Features e Modelagem Baseada em Feições (Questões 36–50)

36. O que significa a crítica de que o CAD tradicional usa "dados microscópicos"?
Resposta: Significa que o CAD tradicional opera com entidades geométricas de baixo nível (pontos, linhas, arestas, faces) que não carregam significado de engenharia. Um furo, por exemplo, é apenas um conjunto de faces cilíndricas, e não um "furo passante M8 para fixação".

37. O que é sub-especificação geométrica no CAD tradicional?
Resposta: É a situação em que a geometria está matematicamente correta, mas a informação não é suficiente para manufatura ou análise. Por exemplo: um cilindro pode estar modelado, mas sem informação de que se trata de um furo roscado, qual o material, ou qual a tolerância de usinagem.

38. Por que a falta de intenção de projeto na estrutura de dados do CAD tradicional é um problema?
Resposta: Porque sistemas posteriores (manufatura, análise, montagem) não conseguem extrair automaticamente o significado da geometria. Um engenheiro de manufatura olhando um furo não sabe, só pela geometria, se é para parafuso, pino, passagem de fluido ou alívio de peso. Isso impede automação e aumenta o risco de erros de interpretação.

39. O que significa dizer que a estrutura de dados do CAD tradicional é de um único nível (flat structure)?
Resposta: Significa que não há hierarquia, agrupamentos ou relações entre elementos geométricos. Cada aresta e face está no mesmo plano, sem organização por função, sem agrupamento em features, sem relações pai-filho. Isso torna o modelo difícil de navegar, modificar e reutilizar.

40. Liste e explique brevemente as quatro deficiências do CAD tradicional.
Resposta: (1) Dados microscópicos: opera com entidades de baixo nível sem significado de engenharia. (2) Sub-especificação geométrica: geometria existe, mas faltam informações para manufatura e análise. (3) Construção tediosa: cada elemento precisa ser definido manualmente; modificações exigem reconstrução. (4) Estrutura de dados plana: sem hierarquia ou agrupamento, dificultando navegação e reuso.

41. O que é uma feature (feição) em CAD?
Resposta: É um elemento geométrico que carrega significado de engenharia — agrega geometria + semântica + comportamento. Exemplo: um "furo passante" é geometria (cilindro) + semântica ("passante", "para fixação M8") + comportamento (atravessa toda a peça, atualiza-se parametricamente).

42. Qual a diferença entre uma feature física e uma feature abstrata? Dê exemplos de cada.
Resposta: Features físicas correspondem a geometria real na peça (ex: furo, cavidade, rasgo, ressalto, chanfro). Features abstratas não têm representação geométrica direta — são informações anexadas ao modelo (ex: tolerância dimensional, acabamento superficial, especificação de material, tratamento térmico).

43. O que são Form Features e como elas diferem de Manufacturing Features?
Resposta: Form Features são orientadas ao design — descrevem a forma funcional da peça como o projetista a concebe (ex: ressalto, nervura). Manufacturing Features são orientadas ao processo de fabricação — a mesma geometria pode ser uma feature diferente (ex: o que é um "ressalto" no design pode ser "material a remover ao redor" na manufatura).

44. Por que o mapeamento entre features de design e features de manufatura não é trivial (nem sempre 1:1)?
Resposta: Porque uma feature de design pode corresponder a múltiplas operações de manufatura, e vice-versa. Além disso, o que é "material" no design é "vazio a remover" na manufatura. Por exemplo: um ressalto no design é uma ilha de material; para usinagem, o que interessa é o volume a ser removido ao redor dele.

45. O que caracteriza uma feature rotacional? Dê exemplos.
Resposta: Features rotacionais são associadas a peças torneadas, com simetria axial e geradas por revolução de um perfil 2D. Exemplos: cilindro externo, cone, ressalto torneado, canal para anel de retenção (groove), faceamento. Usinagem típica: torno.

46. O que caracteriza uma feature prismática? Dê exemplos.
Resposta: Features prismáticas são associadas a peças fresadas, definidas por faces planas ortogonais ou inclinadas, sem exigir simetria rotacional. Exemplos: cavidade retangular (pocket), rasgo (slot), face rebaixada (step), furo (hole). Usinagem típica: fresadora, centro de usinagem.

47. Como saber se uma peça é predominantemente rotacional ou prismática?
Resposta: Uma peça é rotacional se sua geometria principal é gerada por revolução em torno de um eixo (simetria axial) e sua usinagem principal é torneamento. É prismática se sua geometria é baseada em faces planas e a usinagem principal é fresamento. Uma peça pode ser híbrida (ex: eixo com rasgo de chaveta = rotacional + prismática isolada).

48. Qual a diferença entre Feature Recognition e Feature-Based Design (Design by Features)?
Resposta: Feature Recognition parte de um modelo geométrico pronto (B-rep) e tenta identificar features automaticamente por análise da geometria. Feature-Based Design constrói o modelo desde o início usando operações de feature com significado. O segundo captura naturalmente a intenção de projeto; o primeiro tenta recuperá-la depois.

49. Por que Feature Recognition é um problema difícil?
Resposta: Porque features podem se intersectar, sobrepor ou ser parcialmente destruídas por operações posteriores, tornando difícil identificá-las apenas pela geometria final. Além disso, a mesma geometria pode ser interpretada como diferentes features dependendo do contexto de manufatura, gerando ambiguidade.

50. Como a modelagem por features resolve as deficiências do CAD tradicional?
Resposta: (1) Substitui "dados microscópicos" por entidades com significado (features). (2) Elimina a sub-especificação ao associar semântica e parâmetros de manufatura a cada feature. (3) Reduz a construção tediosa com operações de alto nível (ex: "criar furo passante" em vez de modelar cada face). (4) Cria estrutura hierárquica (árvore de features) substituindo a estrutura plana.
