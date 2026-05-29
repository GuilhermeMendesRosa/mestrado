# Relatorio Curto

## 1. Linguagem e bibliotecas

- Linguagem: Python 3
- Bibliotecas: `numpy` para calculo numerico e `matplotlib` para janela, desenho e eventos do mouse

## 2. Insercao e edicao dos pontos

O programa abre um canvas 2D com duas curvas B-spline de grau 4. A curva ativa recebe novos pontos por clique esquerdo do mouse. Pontos ja existentes podem ser selecionados clicando sobre eles e movidos com arraste, com redesenho imediato da curva e do poligono de controle.

## 3. Implementacao da curva B-spline grau 4

A curva foi implementada manualmente pela formulacao de Cox-de Boor. Para cada parametro `t`, o ponto da curva e calculado pela soma ponderada das funcoes base `N(i, p)(t)` pelos pontos de controle. Nenhuma funcao pronta de spline foi utilizada.

## 4. Vetor de nos nao uniforme

Cada curva usa um vetor de nos aberto e nao uniforme. Os primeiros `p + 1` nos sao iguais a `0`, os ultimos `p + 1` nos sao iguais a `1` e os nos internos sao estritamente crescentes, gerados por uma distribuicao nao linear. Isso garante a nao uniformidade exigida no trabalho.

## 5. Derivadas

As derivadas de primeira e segunda ordem sao calculadas por meio dos pontos de controle derivados da B-spline, sem aproximacao numerica por diferencas finitas. Isso permite verificar e ajustar as continuidades C1 e C2 com base matematica direta.

## 6. Continuidade entre duas curvas

- C0: a Curva 2 e transladada para que seu ponto inicial coincida com o ponto final da Curva 1.
- C1: apos C0, o segundo ponto de controle da Curva 2 e ajustado para igualar a primeira derivada na junta.
- C2: apos C1, o terceiro ponto de controle da Curva 2 e ajustado para igualar a segunda derivada na junta.

## 7. Dificuldades encontradas

Os pontos mais delicados foram o tratamento do parametro no extremo final do intervalo e o ajuste exato das derivadas na juncao entre curvas com knots nao uniformes.

## 8. Uso de IA

A IA foi usada para apoiar a estruturacao da implementacao, revisar a arquitetura do codigo e acelerar a redacao da documentacao.
