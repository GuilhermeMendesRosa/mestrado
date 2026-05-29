# Plano de Implementacao - B-spline Grau 4 (Nao uniforme)

## 1. Objetivo

Implementar um trabalho de Computacao Grafica para a curva **B-spline de grau 4** (ordem 5), em um plano 2D com `z = 0`, atendendo ao enunciado:

- insercao de pontos de controle com o mouse
- edicao dos pontos de controle com atualizacao imediata da curva
- implementacao manual da curva
- suporte a **duas curvas no mesmo espaco grafico**
- uniao das curvas com continuidade **C0**, **C1** e **C2**
- entrega de um relatorio curto ao final

Observacao: bibliotecas graficas podem ser usadas apenas para janela, desenho e interacao. A implementacao da curva e das continuidades deve ser propria.

## 2. Linguagem e stack recomendadas

Recomendacao: **Python** com:

- `numpy` para calculos numericos
- `matplotlib` para interface simples com mouse e desenho da curva

Justificativa:

- menor tempo de implementacao
- facil separacao entre parte matematica e interface
- suficiente para inserir, arrastar e redesenhar pontos em tempo real

Se houver necessidade de uma interface mais sofisticada depois, migrar a interface para `PyQt` ou `pygame` e manter o nucleo matematico separado.

## 3. Escopo funcional minimo

O sistema final deve permitir:

1. criar a primeira curva B-spline grau 4
2. criar a segunda curva B-spline grau 4 no mesmo canvas
3. inserir pontos de controle com clique do mouse
4. selecionar e arrastar pontos de controle
5. redesenhar a curva sempre que um ponto for alterado
6. usar vetor de nos **nao uniforme**
7. unir as curvas com C0
8. ajustar as curvas para C1
9. ajustar as curvas para C2
10. exibir informacoes basicas para demonstracao e relatorio

## 4. Requisitos matematicos

### 4.1 Curva B-spline

Usar a formulacao por funcoes base de **Cox-de Boor**.

Curva:

```text
C(t) = soma de i=0 ate n de N(i,p)(t) * P(i)
```

Onde:

- `P(i)` sao os pontos de controle
- `p = 4`
- `N(i,p)(t)` sao as funcoes base B-spline
- `U = [u0, u1, ..., um]` e o vetor de nos

### 4.2 Grau e quantidade minima de pontos

Para grau `p = 4`, e necessario no minimo:

```text
n + 1 >= p + 1
=> minimo de 5 pontos de controle
```

### 4.3 Vetor de nos nao uniforme

Nao usar vetor interno uniformemente espac ado.

Exemplo valido de vetor de nos aberto e nao uniforme:

```text
[0, 0, 0, 0, 0, 0.12, 0.31, 0.58, 0.83, 1, 1, 1, 1, 1]
```

Condicoes desejadas:

- primeiros `p + 1` nos iguais a `0`
- ultimos `p + 1` nos iguais a `1`
- nos internos estritamente crescentes
- espacamentos internos diferentes entre si

### 4.4 Derivadas

Para verificar continuidade, sera util calcular:

- primeira derivada da curva na extremidade
- segunda derivada da curva na extremidade

Pode ser feito de duas formas:

1. por formulas de derivadas de B-spline
2. por derivadas das funcoes base

Recomendacao: implementar funcao separada para avaliar derivadas da curva, em vez de estimar numericamente por diferencas finitas.

## 5. Arquitetura sugerida

Estrutura recomendada:

```text
MOG/
  app.py
  bspline.py
  continuidade.py
  README.md
  relatorio.md
```

### 5.1 `bspline.py`

Responsavel por:

- representar pontos de controle
- gerar vetor de nos nao uniforme
- avaliar funcoes base de Cox-de Boor
- avaliar a curva em varios pontos
- avaliar derivadas de ordem 1 e 2

Funcoes sugeridas:

```python
base_bspline(i, p, t, knots)
gerar_knots_nao_uniformes(n, p)
avaliar_bspline(control_points, degree, knots, num_samples=200)
avaliar_derivada_bspline(control_points, degree, knots, t, ordem=1)
```

### 5.2 `continuidade.py`

Responsavel por:

- unir duas curvas em C0
- ajustar a segunda curva para C1
- ajustar a segunda curva para C2
- verificar se a continuidade foi atingida

Funcoes sugeridas:

```python
aplicar_c0(curva_a, curva_b)
aplicar_c1(curva_a, curva_b)
aplicar_c2(curva_a, curva_b)
verificar_c0(curva_a, curva_b, tolerancia=1e-6)
verificar_c1(curva_a, curva_b, tolerancia=1e-6)
verificar_c2(curva_a, curva_b, tolerancia=1e-6)
```

### 5.3 `app.py`

Responsavel por:

- abrir a janela grafica
- capturar clique do mouse
- inserir pontos de controle
- selecionar e arrastar pontos
- alternar entre curva 1 e curva 2
- desenhar poligonos de controle e curvas
- acionar comandos de C0, C1 e C2 por teclado ou botoes

## 6. Modelo de dados simples

Uma forma minima e suficiente:

```python
class CurvaBSpline:
    degree: int
    control_points: list[np.ndarray]
    knots: np.ndarray
    color: str
```

Estados da interface:

- curva ativa: 1 ou 2
- indice do ponto selecionado para arraste
- modo de insercao ou edicao
- status atual de continuidade

## 7. Roadmap de implementacao

## Etapa 1 - Base matematica

Implementar em `bspline.py`:

1. funcao base de Cox-de Boor
2. geracao do vetor de nos nao uniforme
3. avaliacao da curva
4. avaliacao da primeira derivada
5. avaliacao da segunda derivada

Checklist:

- testar com pelo menos 5 pontos
- validar que a curva muda ao alterar os pontos
- imprimir o vetor de nos no terminal

## Etapa 2 - Primeira curva interativa

Implementar em `app.py`:

1. clique esquerdo para adicionar ponto de controle
2. desenho do poligono de controle
3. desenho da B-spline grau 4
4. atualizacao automatica ao inserir ponto

Checklist:

- impedir avaliacao com menos de 5 pontos
- mostrar texto de ajuda na tela
- manter aspecto do plano coerente

## Etapa 3 - Edicao por arraste

Adicionar:

1. selecao de um ponto clicando proximo a ele
2. arraste com o mouse
3. redesenho em tempo real

Checklist:

- o ponto arrastado acompanha o cursor
- a curva e o poligono de controle atualizam imediatamente
- nao gerar travamentos durante o arraste

## Etapa 4 - Segunda curva no mesmo canvas

Adicionar suporte para duas curvas:

1. tecla para alternar curva ativa
2. cores diferentes para cada curva
3. controle de pontos independente
4. exibicao simultanea das duas curvas

Checklist:

- cada curva mantem seus proprios pontos e knots
- as duas aparecem no mesmo sistema de coordenadas

## Etapa 5 - Continuidade C0

Objetivo:

- fazer o fim da curva A coincidir com o inicio da curva B

Abordagem pratica:

1. encontrar o ponto final da curva A
2. encontrar o ponto inicial da curva B
3. aplicar translacao na curva B para que os dois coincidam

Opcao mais simples:

- deslocar todos os pontos de controle da curva B pelo vetor:

```text
delta = C_A(final) - C_B(inicio)
```

Checklist:

- ponto final de A igual ao ponto inicial de B
- verificacao numerica dentro de tolerancia

## Etapa 6 - Continuidade C1

Objetivo:

- manter C0 e igualar a primeira derivada na junta

Abordagem pratica:

1. garantir C0 primeiro
2. calcular `C'_A(final)`
3. calcular `C'_B(inicio)`
4. ajustar pontos de controle proximos da junta na curva B
5. reavaliar ate atingir a tolerancia

Implementacao minima recomendada:

- fixar a curva A
- ajustar apenas a curva B
- mover um pequeno conjunto dos primeiros pontos de controle de B

Se nao for possivel atingir C1 exata na primeira tentativa, implementar primeiro a verificacao e depois o ajuste.

Checklist:

- C0 preservada
- vetores tangentes iguais dentro de tolerancia
- exibir status na interface

## Etapa 7 - Continuidade C2

Objetivo:

- manter C1 e igualar a segunda derivada na junta

Abordagem pratica:

1. garantir C0 e C1
2. calcular `C''_A(final)`
3. calcular `C''_B(inicio)`
4. ajustar mais pontos de controle de B, ou ajustar A e B de forma controlada
5. verificar a segunda derivada novamente

Checklist:

- C0 preservada
- C1 preservada
- segundas derivadas iguais dentro de tolerancia

## 8. Estrategia de continuidade recomendada

Para entrega mais segura, seguir esta ordem:

1. implementar verificacao de C0, C1 e C2
2. implementar ajuste automatico de C0
3. implementar ajuste automatico de C1
4. implementar ajuste automatico de C2

Motivo:

- e mais facil depurar quando ja existe uma funcao de verificacao independente

## 9. Interacao recomendada na interface

Mapa simples de comandos:

- clique esquerdo: adicionar ponto
- clique e arraste: mover ponto existente
- tecla `1`: ativar curva 1
- tecla `2`: ativar curva 2
- tecla `c`: aplicar C0
- tecla `v`: aplicar C1
- tecla `b`: aplicar C2
- tecla `r`: resetar curva ativa
- tecla `t`: imprimir dados no terminal
- tecla `esc`: sair

Informacoes uteis na tela:

- curva ativa
- numero de pontos da curva ativa
- grau da curva
- tipo do vetor de nos
- status de continuidade atual

## 10. Criterios de aceitacao

O trabalho pode ser considerado pronto quando:

1. a B-spline grau 4 for desenhada a partir dos pontos de controle
2. os pontos puderem ser inseridos com mouse
3. os pontos puderem ser arrastados com mouse
4. duas curvas coexistirem no mesmo canvas
5. C0 puder ser aplicada e demonstrada
6. C1 puder ser aplicada e demonstrada
7. C2 puder ser aplicada e demonstrada
8. o vetor de nos usado for de fato nao uniforme
9. a implementacao da curva nao depender de funcao pronta da biblioteca

## 11. Validacoes e testes manuais

Casos de teste sugeridos:

### Caso 1 - Minimo de pontos

- criar uma curva com 5 pontos
- confirmar que ela e desenhada corretamente

### Caso 2 - Edicao interativa

- arrastar um ponto central
- verificar atualizacao imediata da curva

### Caso 3 - Nao uniformidade

- alterar os nos internos
- verificar que a forma da curva muda sem mudar os pontos de controle

### Caso 4 - C0

- criar duas curvas separadas
- aplicar C0
- conferir coincidencia na junta

### Caso 5 - C1

- aplicar C1 depois de C0
- conferir tangencia na junta

### Caso 6 - C2

- aplicar C2 depois de C1
- conferir suavidade de curvatura na junta

## 12. Riscos tecnicos

1. `matplotlib` pode exigir tratamento cuidadoso de eventos de arraste.
2. Implementar C2 corretamente pode ser a parte mais delicada do trabalho.
3. B-spline nao uniforme exige cuidado com indices do vetor de nos.
4. Erros na fronteira `t = 1` podem aparecer se a avaliacao nao tratar bem o ultimo intervalo.

## 13. Ordem recomendada para a sessao de implementacao

Se a implementacao for feita em outra sessao, usar esta ordem:

1. criar `bspline.py` com Cox-de Boor e avaliacao da curva
2. criar um exemplo simples sem interface para validar a curva
3. criar `app.py` com insercao de pontos por mouse
4. adicionar arraste de pontos
5. adicionar segunda curva
6. adicionar verificacao de C0, C1 e C2
7. adicionar ajuste automatico de C0
8. adicionar ajuste automatico de C1
9. adicionar ajuste automatico de C2
10. preparar `README.md` e `relatorio.md`

## 14. Estrutura minima do relatorio

O relatorio final pode ser curto, mas deve conter:

1. linguagem utilizada
2. bibliotecas utilizadas
3. como os pontos de controle sao inseridos e editados
4. como a curva B-spline grau 4 foi implementada
5. como o vetor de nos nao uniforme foi definido
6. como foram obtidas as continuidades C0, C1 e C2
7. dificuldades encontradas
8. se houve uso de IA, em que etapa e com qual finalidade

## 15. Resultado esperado da implementacao

Ao final, o programa deve demonstrar visualmente:

- duas curvas B-spline grau 4 no mesmo plano
- pontos de controle manipulaveis com mouse
- vetor de nos nao uniforme
- uniao com C0
- uniao com C1
- uniao com C2

Esse e o objetivo minimo para uma entrega forte e alinhada ao enunciado.
