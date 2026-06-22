# 📋 Plano de Ação - Trabalho de Curvas e Continuidade

**Linguagem escolhida:** Python  
**Biblioteca gráfica:** Tkinter  
**Curva 1 (Parte 2):** B-spline Grau 4 (Não uniforme) ✅  
**Curva 2 (Parte 3):** Bézier Grau 5  
**Prazo final:** 25/06/2026

---

## ✅ FASE 1 — Definir Linguagem de Programação
**Status:** CONCLUÍDO ✅  
**Data:** Prévio ao início da implementação

- [x] Escolher Python como linguagem de programação.
- [x] Aprovado pelo professor/segundo as regras do trabalho.

---

## ✅ FASE 2 — Implementar B-spline Grau 4 (Não uniforme)
**Status:** CONCLUÍDO ✅  
**Arquivo:** `bspline_curva.py`

### O que foi feito:
- [x] Criar a janela gráfica com Tkinter.
- [x] Capturar cliques do mouse para adicionar pontos de controle.
- [x] Permitir arrastar os pontos de controle e atualizar a curva em tempo real.
- [x] Implementar o **vetor de nós não uniforme** (clamped) com repetições nas extremidades.
- [x] Implementar o **algoritmo de Cox-de Boor** para calcular as funções base.
- [x] Calcular os pontos da curva B-spline a partir dos pontos de controle.
- [x] Desenhar a curva B-spline na tela (linha vermelha).
- [x] Desenhar a poligonal de controle (linhas tracejadas cinzas).

### Como testar:
1. Execute: `python3 bspline_curva.py`
2. Clique na tela branca para adicionar pontos de controle.
3. Adicione pelo menos **5 pontos** para a curva aparecer.
4. Arraste os pontos azuis para ver a curva se atualizar.

### Observações importantes:
- **O grau é fixo em 4** (definido pelo professor).
- A quantidade de pontos de controle define o **número de segmentos** da curva:
  - 5 pontos = 1 segmento (mínimo)
  - 6 pontos = 2 segmentos
  - 7 pontos = 3 segmentos
  - e assim por diante...
- O vetor de nós não uniforme é gerado com repetições nas extremidades para forçar a curva a passar pelo **primeiro e último ponto**.

---

## ✅ FASE 3 — Implementar Bézier Grau 5
**Status:** CONCLUÍDO ✅
**Arquivo:** `bezier.py`

### O que foi feito:
- [x] Adicionar uma nova curva (Bézier Grau 5) no mesmo canvas.
- [x] Permitir inserir e mover os pontos de controle da Bézier separadamente.
- [x] Implementar o **algoritmo de De Casteljau** para calcular os pontos da curva.
- [x] Diferenciar visualmente os pontos de controle da B-spline (azul) e da Bézier (verde).
- [x] Desenhar a curva Bézier na tela (cor verde).

### Como testar:
1. Execute: `python3 curvas.py`
2. Use o botão "Modo: B-spline" / "Modo: Bézier" para alternar entre as curvas.
3. No modo Bézier, clique para adicionar pontos de controle (mínimo 6).
4. Arraste os pontos verdes para ver a curva se atualizar em tempo real.

---

## ✅ FASE 4 — Unir as curvas com Continuidade C0
**Status:** CONCLUÍDO ✅
**Descrição:** Utilizar transformações geométricas para unir as duas curvas de forma que elas se toquem (posição igual no ponto de junção).

### O que foi feito:
- [x] Identificar o ponto final da B-spline (último ponto de controle) e o ponto inicial da Bézier (primeiro ponto de controle).
- [x] Aplicar uma **translação** nos pontos de controle da Bézier para que esses pontos coincidam.
- [x] Adicionar botão "Unir curvas (C0)" na interface.
- [x] Indicador visual dourado no ponto de junção das curvas.
- [x] Mensagem de status "Continuidade C0 ativa" exibida no canvas.

### Como testar:
1. Execute: `python3 curvas.py`
2. Adicione pontos para ambas as curvas (B-spline: mínimo 5, Bézier: exatamente 6).
3. Clique no botão "Unir curvas (C0)".
4. Observe a Bézier ser transladada para encontrar a B-spline e o marcador dourado na junção.

---

## ✅ FASE 5 — Unir as curvas com Continuidade C1
**Status:** CONCLUÍDO ✅
**Descrição:** Além de C0 (posição igual), garantir que as **tangentes** (derivadas de primeira ordem) das duas curvas sejam iguais no ponto de junção.

### O que precisa ser feito:
- [x] Ajustar os pontos de controle internos próximos à junção para que as tangentes coincidam.
- [x] Ou usar uma transformação geométrica (ex: escala/rotação) para alinhar as direções das curvas.
- [x] Caso não consiga C1, aceitável entregar **G1** (direções iguais, magnitudes podem diferir), com nota reduzida.

---

## ✅ FASE 6 — Unir as curvas com Continuidade C2
**Status:** CONCLUÍDO ✅
**Data:** 22/06/2026
**Descrição:** Além de C0 e C1, garantir que as **curvaturas** (derivadas de segunda ordem) também sejam iguais no ponto de junção.

### O que foi feito:
- [x] Implementar `derivada_segunda_no_fim()` na B-spline: fórmula analítica `p*(p-1)*(B_n - 2*B_{n-1} + B_{n-2})` com p=4 → `12*(B_n - 2*B_{n-1} + B_{n-2})`.
- [x] Implementar `derivada_segunda_no_inicio()` na Bézier: fórmula analítica `n*(n-1)*(Z_2 - 2*Z_1 + Z_0)` com n=5 → `20*(Z_2 - 2*Z_1 + Z_0)`.
- [x] Deduzir fórmula para ajustar Z_2 preservando C0 e C1: `Z_2 = (16/5)·B_n - (14/5)·B_{n-1} + (3/5)·B_{n-2}`.
- [x] Adicionar botão "Unir curvas (C2)" na interface.
- [x] Implementar `aplicar_c2()` que ajusta Z_2 para igualar curvaturas.
- [x] Implementar `aplicar_g2()` como fallback (alinha direção da curvatura, preserva magnitude original).
- [x] Visualização de vetores de curvatura (B'' em laranja, Z'' em roxo) no ponto de junção.
- [x] Indicador de status C2/G2 no canvas.
- [x] Invalidação de C2/G2 ao reaplicar C1 ou G1.

### Como testar:
1. Execute: `python3 curvas.py`
2. Adicione pontos para ambas as curvas (B-spline: mínimo 5, Bézier: exatamente 6).
3. Clique em "Unir curvas (C0)", depois "Unir curvas (C1)", depois "Unir curvas (C2)".
4. Observe os vetores de curvatura laranja (B'') e roxo (Z'') coincidirem.
5. Alternativa: use "Unir curvas (G2)" para alinhar apenas a direção da curvatura.

---

## ⏳ FASE 7 — Relatório Final
**Status:** PENDENTE ⏳
**Descrição:** Escrever um relatório resumido sobre como o trabalho foi realizado.

### O que precisa conter:
- [ ] Descrição das ferramentas utilizadas (Python, Tkinter, VS Code, etc.).
- [ ] Explicação de como o algoritmo de Cox-de Boor foi implementado.
- [ ] Explicação de como a curva Bézier foi implementada.
- [ ] Descrição do processo para alcançar C0, C1 e C2.
- [ ] Printscreens ou descrição dos resultados visuais.
- [ ] Se usar IA generativa, descrever como e para quais fins (conforme regras do trabalho).

---

## 📁 Estrutura de Arquivos

```
MOG/
├── bspline_curva.py          # Código principal (Parte 2 em andamento)
├── DESCRIÇÃO TRABALHO.md     # Descrição original do trabalho
└── PLANO_DE_AÇÃO.md         # Este arquivo (checklist de progresso)
```

---

## 🎯 Resumo do Progresso

| Fase | Descrição | Status |
|------|-----------|--------|
| 1 | Definir linguagem | ✅ Concluído |
| 2 | B-spline Grau 4 | ✅ Concluído |
| 3 | Bézier Grau 5 | ✅ Concluído |
| 4 | Continuidade C0 | ✅ Concluído |
| 5 | Continuidade C1 | ✅ Concluído |
| 6 | Continuidade C2 | ✅ Concluído |
| 7 | Relatório | ⏳ Pendente |

**Última atualização:** 22/06/2026
