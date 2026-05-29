# B-spline Grau 4 Nao Uniforme

Implementacao manual de curvas B-spline de grau 4 (ordem 5) com:

- duas curvas no mesmo canvas
- insercao de pontos de controle com mouse
- edicao por arraste com atualizacao imediata
- vetor de nos aberto e nao uniforme
- uniao entre as curvas com C0, C1 e C2

## Arquivos

- `app.py`: interface interativa com `matplotlib`
- `bspline.py`: base de Cox-de Boor, avaliacao da curva e derivadas
- `continuidade.py`: ajuste e verificacao de C0, C1 e C2
- `relatorio.md`: relatorio curto da entrega
- `bspline_grau4.py`: ponto de entrada alternativo

## Dependencias

```bash
pip install numpy matplotlib
```

## Como executar

```bash
python3 app.py
```

ou

```bash
python3 bspline_grau4.py
```

## Comandos da interface

- clique esquerdo: adiciona ponto na curva ativa
- clique e arraste: move um ponto existente
- `1` / `2`: ativa curva 1 ou curva 2
- `c`: aplica C0 do fim da Curva 1 para o inicio da Curva 2
- `v`: aplica C1 do fim da Curva 1 para o inicio da Curva 2
- `b`: aplica C2 do fim da Curva 1 para o inicio da Curva 2
- `r`: reseta a curva ativa
- `k`: regenera os knots nao uniformes da curva ativa
- `t`: imprime pontos, knots e derivadas no terminal
- `esc`: fecha a aplicacao

## Observacoes de implementacao

- A curva e avaliada manualmente pelas funcoes base de Cox-de Boor.
- O vetor de nos e aberto e nao uniforme; os nos internos seguem uma progressao nao linear.
- As derivadas de ordem 1 e 2 sao calculadas a partir dos pontos de controle derivados, sem diferencas finitas.
- O ajuste de continuidade altera a Curva 2 para coincidir com o final da Curva 1.

## Fluxo sugerido para demonstracao

1. Insira pelo menos 5 pontos na Curva 1.
2. Pressione `2` e insira pelo menos 5 pontos na Curva 2.
3. Arraste alguns pontos para mostrar a atualizacao em tempo real.
4. Pressione `c`, depois `v` e depois `b` para demonstrar C0, C1 e C2.
5. Pressione `t` para imprimir os knots e as derivadas no terminal.
