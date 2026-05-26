"""
B-Spline Grau 4 (Ordem 5) - Interativa
========================================
Implementacao de curva B-spline de grau 4 com entrada interativa de pontos
de controle via cliques do mouse.

Instrucoes:
- Clique ESQUERDO: adiciona ponto de controle
- Clique DIREITO: finaliza a entrada de pontos
- Minimo de 5 pontos de controle necessarios para grau 4

Algoritmo: Funcoes base recursivas de Cox-de Boor
Vetor de nos: Clamped uniforme
"""

import numpy as np
import matplotlib.pyplot as plt


# =============================================================================
# Funcoes Base B-spline (Cox-de Boor)
# =============================================================================

def base_bspline(i, p, t, knots):
    """
    Calcula a funcao base B-spline N_{i,p}(t) usando a formula recursiva
    de Cox-de Boor.

    Parametros:
        i     : indice da funcao base
        p     : grau da B-spline
        t     : parametro (valor onde avaliar)
        knots : vetor de nos

    Retorna:
        Valor da funcao base N_{i,p}(t)
    """
    # Caso base: grau 0
    if p == 0:
        if knots[i] <= t < knots[i + 1]:
            return 1.0
        else:
            return 0.0

    # Recursao de Cox-de Boor
    # Primeiro termo
    denom1 = knots[i + p] - knots[i]
    if denom1 == 0.0:
        termo1 = 0.0
    else:
        termo1 = ((t - knots[i]) / denom1) * base_bspline(i, p - 1, t, knots)

    # Segundo termo
    denom2 = knots[i + p + 1] - knots[i + 1]
    if denom2 == 0.0:
        termo2 = 0.0
    else:
        termo2 = ((knots[i + p + 1] - t) / denom2) * base_bspline(i + 1, p - 1, t, knots)

    return termo1 + termo2


# =============================================================================
# Vetor de Nos (Knot Vector) - Clamped Uniforme
# =============================================================================

def gerar_knot_vector(n, p):
    """
    Gera um vetor de nos clamped (aberto) uniforme.

    Para n+1 pontos de controle e grau p, o vetor de nos tem m+1 elementos,
    onde m = n + p + 1.

    O vetor clamped tem os primeiros (p+1) nos iguais a 0 e os ultimos
    (p+1) nos iguais a 1, com nos internos uniformemente espacados.

    Parametros:
        n : indice maximo dos pontos de controle (n+1 pontos no total)
        p : grau da B-spline

    Retorna:
        Array numpy com o vetor de nos
    """
    m = n + p + 1  # indice maximo do vetor de nos
    knots = np.zeros(m + 1)

    for j in range(m + 1):
        if j <= p:
            knots[j] = 0.0
        elif j >= m - p:
            knots[j] = 1.0
        else:
            knots[j] = (j - p) / (n - p + 1)

    return knots


# =============================================================================
# Avaliacao da Curva B-spline
# =============================================================================

def avaliar_bspline(pontos_controle, grau, num_amostras=200):
    """
    Avalia a curva B-spline para um conjunto de pontos de controle.

    Parametros:
        pontos_controle : array (n+1, 2) com as coordenadas dos pontos de controle
        grau            : grau da B-spline
        num_amostras    : numero de pontos para amostrar a curva

    Retorna:
        curva : array (num_amostras, 2) com as coordenadas da curva
    """
    n = len(pontos_controle) - 1  # indice maximo

    if n < grau:
        return None  # pontos insuficientes

    knots = gerar_knot_vector(n, grau)

    # Parametro t varia de 0 a 1 (exclusive do ultimo valor para evitar
    # problemas na fronteira)
    t_values = np.linspace(0.0, 1.0, num_amostras, endpoint=False)
    # Adiciona o ultimo ponto exatamente em t = 1 - epsilon para capturar
    # o final da curva
    t_values = np.append(t_values, 1.0 - 1e-10)

    curva = np.zeros((len(t_values), 2))

    for idx, t in enumerate(t_values):
        ponto = np.zeros(2)
        for i in range(n + 1):
            N = base_bspline(i, grau, t, knots)
            ponto += N * pontos_controle[i]
        curva[idx] = ponto

    return curva


# =============================================================================
# Interface Interativa com Matplotlib
# =============================================================================

class BSplineInterativa:
    """
    Classe que gerencia a interface interativa para construcao da curva
    B-spline de grau 4.
    """

    def __init__(self, grau=4):
        self.grau = grau
        self.pontos_controle = []
        self.finalizado = False

        # Configuracao da figura
        self.fig, self.ax = plt.subplots(1, 1, figsize=(10, 7))
        self.ax.set_title(
            f"B-Spline Grau {self.grau} - Interativa\n"
            f"Clique ESQUERDO: adicionar ponto | "
            f"Clique DIREITO: finalizar\n"
            f"(Minimo {self.grau + 1} pontos de controle)",
            fontsize=11
        )
        self.ax.set_xlim(0, 10)
        self.ax.set_ylim(0, 10)
        self.ax.set_aspect('equal')
        self.ax.grid(True, alpha=0.3)
        self.ax.set_xlabel('X')
        self.ax.set_ylabel('Y')

        # Elementos graficos
        self.linha_poligono, = self.ax.plot([], [], 'b--o', markersize=8,
                                            linewidth=1, alpha=0.5,
                                            label='Poligono de controle')
        self.linha_curva, = self.ax.plot([], [], 'r-', linewidth=2.5,
                                         label='Curva B-spline')
        self.pontos_plot, = self.ax.plot([], [], 'ko', markersize=10,
                                         zorder=5,
                                         label='Pontos de controle')

        # Info de quantidade de pontos
        self.texto_info = self.ax.text(
            0.02, 0.02, f"Pontos: 0 / min {self.grau + 1}",
            transform=self.ax.transAxes, fontsize=10,
            verticalalignment='bottom',
            bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.7)
        )

        self.ax.legend(loc='upper right')

        # Conectar eventos
        self.cid_click = self.fig.canvas.mpl_connect('button_press_event',
                                                      self.on_click)
        self.cid_key = self.fig.canvas.mpl_connect('key_press_event',
                                                    self.on_key)

    def on_click(self, event):
        """Callback para cliques do mouse."""
        if event.inaxes != self.ax:
            return
        if self.finalizado:
            return

        if event.button == 1:  # Clique esquerdo - adiciona ponto
            self.pontos_controle.append([event.xdata, event.ydata])
            self.atualizar_plot()

        elif event.button == 3:  # Clique direito - finaliza
            self.finalizar()

    def on_key(self, event):
        """Callback para teclas do teclado."""
        if event.key == 'enter':
            self.finalizar()
        elif event.key == 'escape':
            plt.close(self.fig)

    def finalizar(self):
        """Finaliza a entrada de pontos."""
        self.finalizado = True
        n_pontos = len(self.pontos_controle)

        if n_pontos < self.grau + 1:
            self.ax.set_title(
                f"ERRO: {n_pontos} pontos inseridos, "
                f"minimo necessario: {self.grau + 1}\n"
                f"Feche a janela e execute novamente.",
                fontsize=11, color='red'
            )
        else:
            self.ax.set_title(
                f"B-Spline Grau {self.grau} - FINALIZADA\n"
                f"{n_pontos} pontos de controle",
                fontsize=11, color='green'
            )
            self.imprimir_info()

        self.fig.canvas.draw()

    def imprimir_info(self):
        """Imprime informacoes sobre a curva no terminal."""
        n = len(self.pontos_controle) - 1
        knots = gerar_knot_vector(n, self.grau)

        print("\n" + "=" * 60)
        print(f"  CURVA B-SPLINE GRAU {self.grau}")
        print("=" * 60)
        print(f"  Grau (p):              {self.grau}")
        print(f"  Ordem (k = p+1):       {self.grau + 1}")
        print(f"  Pontos de controle:    {n + 1}")
        print(f"  Nos no vetor (m+1):    {len(knots)}")
        print("-" * 60)
        print("  Pontos de controle:")
        for i, p in enumerate(self.pontos_controle):
            print(f"    P{i} = ({p[0]:.3f}, {p[1]:.3f})")
        print("-" * 60)
        print(f"  Vetor de nos (clamped uniforme):")
        print(f"    {np.array2string(knots, precision=4)}")
        print("=" * 60 + "\n")

    def atualizar_plot(self):
        """Atualiza o grafico com os pontos e a curva."""
        pontos = np.array(self.pontos_controle)
        n_pontos = len(self.pontos_controle)

        # Atualiza pontos de controle
        self.pontos_plot.set_data(pontos[:, 0], pontos[:, 1])

        # Atualiza poligono de controle
        self.linha_poligono.set_data(pontos[:, 0], pontos[:, 1])

        # Atualiza texto informativo
        self.texto_info.set_text(f"Pontos: {n_pontos} / min {self.grau + 1}")

        # Calcula e desenha a curva B-spline se houver pontos suficientes
        if n_pontos >= self.grau + 1:
            curva = avaliar_bspline(pontos, self.grau)
            if curva is not None:
                self.linha_curva.set_data(curva[:, 0], curva[:, 1])
                self.texto_info.set_text(
                    f"Pontos: {n_pontos} / min {self.grau + 1} "
                    f"[Curva ativa]"
                )
        else:
            self.linha_curva.set_data([], [])

        # Ajusta limites dos eixos se necessario
        if n_pontos > 0:
            margem = 1.0
            x_min = pontos[:, 0].min() - margem
            x_max = pontos[:, 0].max() + margem
            y_min = pontos[:, 1].min() - margem
            y_max = pontos[:, 1].max() + margem

            # Mantem aspecto razoavel
            self.ax.set_xlim(min(0, x_min), max(10, x_max))
            self.ax.set_ylim(min(0, y_min), max(10, y_max))

        self.fig.canvas.draw()


# =============================================================================
# Main
# =============================================================================

def main():
    print("\n" + "=" * 60)
    print("  B-SPLINE GRAU 4 (ORDEM 5) - MODO INTERATIVO")
    print("=" * 60)
    print("  Instrucoes:")
    print("    - Clique ESQUERDO: adicionar ponto de controle")
    print("    - Clique DIREITO ou ENTER: finalizar")
    print("    - ESC: fechar sem finalizar")
    print(f"    - Minimo de 5 pontos de controle (grau + 1)")
    print("=" * 60 + "\n")

    app = BSplineInterativa(grau=4)
    plt.show()


if __name__ == "__main__":
    main()
