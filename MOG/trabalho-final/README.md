# Editor de Curvas Paramétricas

Editor interativo de curvas B-spline (grau 4) e Bézier (grau 5) com suporte a continuidade C0, C1 e C2.

## Requisitos

- Python 3

## Como executar

```bash
python3 main.py
```

## Arquivos

- `main.py` — ponto de entrada
- `src/aplicativo.py` — interface gráfica (Tkinter)
- `src/bspline.py` — curva B-spline
- `src/bezier.py` — curva Bézier
- `src/continuidade.py` — continuidade C0, C1, C2
- `src/renderizador.py` — desenho na tela
- `src/painel.py` — painel de coordenadas
