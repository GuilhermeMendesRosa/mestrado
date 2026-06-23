#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Trabalho de Computacao Grafica - Partes 2 e 3
Main: Matplotlib + Tkinter + mouse + renderizacao
Curvas: B-spline Grau 4 (nao uniforme) e Bezier Grau 5
"""

import math
import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.patches import Circle

from bspline import BSpline
from bezier import Bezier

# --------------------------------------------------------------------------- #
# Mapeamento de cores Tkinter -> Matplotlib
# --------------------------------------------------------------------------- #
_MAPA_CORES = {
    "green2":     "#00ee00",
    "green3":     "#00cd00",
    "lightgray":  "#d3d3d3",
    "lightgreen": "#90ee90",
    "darkblue":   "#00008b",
    "darkgreen":  "#006400",
    "gold":       "#ffd700",
    "gray50":     "#808080",
}

def _cor(nome):
    """Retorna o codigo de cor aceito pelo matplotlib."""
    return _MAPA_CORES.get(nome, nome)


LARGURA = 800
ALTURA  = 600
PASSOS  = 200   # resolucao das curvas parametricas


class AplicativoCurvas:
    """Janela principal. Gerencia as duas curvas via composicao (POO)."""

    def __init__(self, raiz):
        self.raiz = raiz
        self.raiz.title("B-spline Grau 4 + Bezier Grau 5")
        self.raiz.geometry("960x740")

        # --- Composicao: Main TEM uma BSpline e TEM uma Bezier ---
        self.bspline = BSpline()
        self.bezier  = Bezier()

        self.modo_ativo = "bspline"

        self.continuidade_c0 = False
        self.continuidade_c1 = False
        self.continuidade_c2 = False

        self.arrastando       = None
        self.lista_arrastando = None
        self.raio_selecao     = 15   # em unidades de dados (espaco [0,800]x[0,600])

        # ------------------------------------------------------------------ #
        # Frame de controles — empacotado PRIMEIRO para garantir posicao base
        # ------------------------------------------------------------------ #
        self.frame_controle = tk.Frame(raiz, pady=5)
        self.frame_controle.pack(side=tk.BOTTOM, fill=tk.X)

        self.botao_modo = tk.Button(
            self.frame_controle, text="Modo: B-spline",
            command=self.alternar_modo, font=("Arial", 11, "bold"),
            bg="#d0d0ff", width=16
        )
        self.botao_modo.pack(side=tk.LEFT, padx=6)

        self.botao_limpar = tk.Button(
            self.frame_controle, text="Limpar",
            command=self.limpar, font=("Arial", 11, "bold"),
            bg="#ffdddd", width=10
        )
        self.botao_limpar.pack(side=tk.LEFT, padx=6)

        self.botao_c0 = tk.Button(
            self.frame_controle, text="Unir curvas (C0)",
            command=self.aplicar_c0, font=("Arial", 11, "bold"),
            bg="#ffffcc", width=16
        )
        self.botao_c0.pack(side=tk.LEFT, padx=6)

        self.botao_c1 = tk.Button(
            self.frame_controle, text="Unir curvas (C1)",
            command=self.aplicar_c1, font=("Arial", 11, "bold"),
            bg="#ffcccc", width=16
        )
        self.botao_c1.pack(side=tk.LEFT, padx=6)

        self.botao_c2 = tk.Button(
            self.frame_controle, text="Unir curvas (C2)",
            command=self.aplicar_c2, font=("Arial", 11, "bold"),
            bg="#ddccff", width=16
        )
        self.botao_c2.pack(side=tk.LEFT, padx=6)

        # ------------------------------------------------------------------ #
        # Frame da toolbar — empacotado ANTES do canvas para ficar abaixo dele
        # ------------------------------------------------------------------ #
        self.frame_toolbar = tk.Frame(raiz)
        self.frame_toolbar.pack(side=tk.BOTTOM, fill=tk.X)

        # ------------------------------------------------------------------ #
        # Figura Matplotlib
        # ------------------------------------------------------------------ #
        self.fig = Figure(dpi=100)
        self.ax  = self.fig.add_subplot(111)
        self._configurar_eixos()
        self.fig.tight_layout(pad=2.0)

        self.mpl_canvas = FigureCanvasTkAgg(self.fig, master=raiz)
        self.mpl_canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        # Toolbar nativa (zoom por caixa, pan, home/reset, salvar)
        self.toolbar = NavigationToolbar2Tk(
            self.mpl_canvas, self.frame_toolbar, pack_toolbar=False
        )
        self.toolbar.update()
        self.toolbar.pack(fill=tk.X)

        # Conecta eventos de mouse do matplotlib
        self.mpl_canvas.mpl_connect("button_press_event",   self._on_press)
        self.mpl_canvas.mpl_connect("motion_notify_event",  self._on_motion)
        self.mpl_canvas.mpl_connect("button_release_event", self._on_release)

        self.redesenhar()

    # ---------------------------------------------------------------------- #
    # Eixos
    # ---------------------------------------------------------------------- #

    def _configurar_eixos(self):
        self.ax.set_xlim(0, LARGURA)
        self.ax.set_ylim(0, ALTURA)
        self.ax.set_xlabel("X", fontsize=10)
        self.ax.set_ylabel("Y", fontsize=10)
        self.ax.grid(True, color="#e0e0e0", linestyle="-", linewidth=0.6)
        self.ax.set_facecolor("#f9f9f9")

    # ---------------------------------------------------------------------- #
    # Modo
    # ---------------------------------------------------------------------- #

    def _curva_ativa(self):
        """Retorna o objeto da curva que esta ativa no momento."""
        return self.bspline if self.modo_ativo == "bspline" else self.bezier

    def alternar_modo(self):
        self.arrastando       = None
        self.lista_arrastando = None
        if self.modo_ativo == "bspline":
            self.modo_ativo = "bezier"
            self.botao_modo.config(text="Modo: Bezier", bg="#d0ffd0")
        else:
            self.modo_ativo = "bspline"
            self.botao_modo.config(text="Modo: B-spline", bg="#d0d0ff")
        self.redesenhar()

    def _invalidar_continuidades(self):
        self.continuidade_c0 = False
        self.continuidade_c1 = False
        self.continuidade_c2 = False
        self.botao_c0.config(text="Unir curvas (C0)", bg="#ffffcc")
        self.botao_c1.config(text="Unir curvas (C1)", bg="#ffcccc")
        self.botao_c2.config(text="Unir curvas (C2)", bg="#ddccff")

    # ---------------------------------------------------------------------- #
    # Limpar
    # ---------------------------------------------------------------------- #

    def limpar(self):
        """Reseta ambas as curvas, continuidades e volta para a visao padrao."""
        self.bspline.pontos.clear()
        self.bezier.pontos.clear()
        self.arrastando       = None
        self.lista_arrastando = None
        self.modo_ativo       = "bspline"
        self.botao_modo.config(text="Modo: B-spline", bg="#d0d0ff")
        self._invalidar_continuidades()
        # Restaura limites de visao iniciais
        self.ax.set_xlim(0, LARGURA)
        self.ax.set_ylim(0, ALTURA)
        self.redesenhar()

    # ---------------------------------------------------------------------- #
    # C0 Continuidade
    # ---------------------------------------------------------------------- #

    def aplicar_c0(self):
        """Aplica translacao para unir as curvas com continuidade C0."""
        if not self.bspline.pronto() or not self.bezier.pronto():
            return

        ultimo_bsp   = self.bspline.pontos[-1]
        primeiro_bez = self.bezier.pontos[0]

        dx = ultimo_bsp["x"] - primeiro_bez["x"]
        dy = ultimo_bsp["y"] - primeiro_bez["y"]

        for p in self.bezier.pontos:
            p["x"] += dx
            p["y"] += dy

        self.continuidade_c0 = True
        self.botao_c0.config(text="Reaplicar C0", bg="#ccffcc")
        self.redesenhar()

    # ---------------------------------------------------------------------- #
    # C1 Continuidade
    # ---------------------------------------------------------------------- #

    def _pode_aplicar_c1(self):
        return (self.bspline.pronto() and self.bezier.pronto()
                and len(self.bspline.pontos) >= 2)

    def aplicar_c1(self):
        """Ajusta Z_1 para igualar tangentes: C1."""
        if not self._pode_aplicar_c1():
            return

        if not self.continuidade_c0:
            self.aplicar_c0()
            if not self.continuidade_c0:
                return

        jx = self.bspline.pontos[-1]["x"]
        jy = self.bspline.pontos[-1]["y"]

        dx_bs, dy_bs, _ = self.bspline.derivada_no_fim()

        # Para Bezier grau 5, Z'(0) = 5 * (Z1 - Z0).
        self.bezier.pontos[1]["x"] = jx + dx_bs / 5
        self.bezier.pontos[1]["y"] = jy + dy_bs / 5

        self.continuidade_c1 = True
        self.continuidade_c2 = False
        self.botao_c1.config(text="Reaplicar C1", bg="#ff6666")
        self.botao_c2.config(text="Unir curvas (C2)", bg="#ddccff")
        self.redesenhar()

    # ---------------------------------------------------------------------- #
    # C2 Continuidade
    # ---------------------------------------------------------------------- #

    def _pode_aplicar_c2(self):
        return (self.bspline.pronto() and self.bezier.pronto()
                and len(self.bspline.pontos) >= 3)

    def aplicar_c2(self):
        """Ajusta Z_2 para igualar curvaturas: C2."""
        if not self._pode_aplicar_c2():
            return

        if not self.continuidade_c0:
            self.aplicar_c0()
            if not self.continuidade_c0:
                return

        if not self.continuidade_c1:
            self.aplicar_c1()
            if not self.continuidade_c1:
                return

        dx_bs2, dy_bs2, _ = self.bspline.derivada_segunda_no_fim()

        z0 = self.bezier.pontos[0]
        z1 = self.bezier.pontos[1]

        # Para Bezier grau 5, Z''(0) = 20 * (Z2 - 2 * Z1 + Z0).
        self.bezier.pontos[2]["x"] = dx_bs2 / 20.0 + 2 * z1["x"] - z0["x"]
        self.bezier.pontos[2]["y"] = dy_bs2 / 20.0 + 2 * z1["y"] - z0["y"]

        self.continuidade_c2 = True
        self.botao_c2.config(text="Reaplicar C2", bg="#9966ff")
        self.redesenhar()

    # ---------------------------------------------------------------------- #
    # Helpers de vetores (tangente / curvatura)
    # ---------------------------------------------------------------------- #

    def _desenhar_vetor(self, jx, jy, ex, ey, cor, label, dx_label=0, dy_label=8):
        """Desenha uma seta de (jx,jy) ate (ex,ey) com texto label."""
        self.ax.annotate(
            "", xy=(ex, ey), xytext=(jx, jy),
            arrowprops=dict(arrowstyle="->", color=cor, lw=2.5),
            zorder=7
        )
        self.ax.text(
            ex + dx_label, ey + dy_label, label,
            color=cor, fontsize=8, fontweight="bold",
            ha="center", zorder=7
        )

    # ---------------------------------------------------------------------- #
    # Tangentes (visualizacao C1)
    # ---------------------------------------------------------------------- #

    def desenhar_tangentes(self):
        """Desenha vetores tangente na juncao para visualizar C1."""
        if not self.continuidade_c0:
            return
        if not self._pode_aplicar_c1():
            return

        jx = self.bspline.pontos[-1]["x"]
        jy = self.bspline.pontos[-1]["y"]

        dx_bs, dy_bs, _ = self.bspline.derivada_no_fim()
        dx_bz, dy_bz, _ = self.bezier.derivada_no_inicio()

        max_mag = max(math.hypot(dx_bs, dy_bs), math.hypot(dx_bz, dy_bz), 1e-9)
        scale   = min(60.0, 150.0 / max_mag)

        self._desenhar_vetor(
            jx, jy,
            jx + dx_bs * scale, jy + dy_bs * scale,
            "#cc0000", f"B'=({dx_bs:.1f},{dy_bs:.1f})"
        )
        self._desenhar_vetor(
            jx, jy,
            jx + dx_bz * scale, jy + dy_bz * scale,
            "#006600", f"Z'=({dx_bz:.1f},{dy_bz:.1f})"
        )

    # ---------------------------------------------------------------------- #
    # Curvaturas (visualizacao C2)
    # ---------------------------------------------------------------------- #

    def desenhar_curvaturas(self):
        """Desenha vetores de curvatura (2a derivada) na juncao."""
        if not self.continuidade_c0:
            return
        if not self._pode_aplicar_c2():
            return

        jx = self.bspline.pontos[-1]["x"]
        jy = self.bspline.pontos[-1]["y"]

        dx_bs2, dy_bs2, _ = self.bspline.derivada_segunda_no_fim()
        dx_bz2, dy_bz2, _ = self.bezier.derivada_segunda_no_inicio()

        max_mag = max(math.hypot(dx_bs2, dy_bs2), math.hypot(dx_bz2, dy_bz2), 1e-9)
        scale   = min(30.0, 80.0 / max_mag)

        self._desenhar_vetor(
            jx, jy,
            jx + dx_bs2 * scale, jy + dy_bs2 * scale,
            "#cc6600", f"B''=({dx_bs2:.1f},{dy_bs2:.1f})",
            dx_label=10, dy_label=0
        )
        self._desenhar_vetor(
            jx, jy,
            jx + dx_bz2 * scale, jy + dy_bz2 * scale,
            "#6600cc", f"Z''=({dx_bz2:.1f},{dy_bz2:.1f})",
            dx_label=10, dy_label=0
        )

    # ---------------------------------------------------------------------- #
    # Mouse
    # ---------------------------------------------------------------------- #

    def _toolbar_ativa(self):
        """True se a toolbar esta em modo zoom ou pan — nao adicionar pontos."""
        return bool(self.toolbar.mode)

    def _on_press(self, evento):
        if evento.button != 1:
            return
        if evento.inaxes is None or self._toolbar_ativa():
            return

        x, y  = evento.xdata, evento.ydata
        curva = self._curva_ativa()

        # Verifica se clicou perto de algum ponto para iniciar arraste
        for i, ponto in enumerate(curva.pontos):
            if math.hypot(ponto["x"] - x, ponto["y"] - y) <= self.raio_selecao:
                self.arrastando       = i
                self.lista_arrastando = self.modo_ativo
                return

        if curva.pode_adicionar():
            curva.adicionar_ponto(x, y)
            self._invalidar_continuidades()
        self.redesenhar()

    def _on_motion(self, evento):
        if self.arrastando is None:
            return
        if evento.button != 1:
            return
        if evento.inaxes is None:
            return
        if self.lista_arrastando != self.modo_ativo:
            return

        curva = self._curva_ativa()
        curva.pontos[self.arrastando]["x"] = evento.xdata
        curva.pontos[self.arrastando]["y"] = evento.ydata
        self._invalidar_continuidades()
        self.redesenhar()

    def _on_release(self, evento):
        self.arrastando       = None
        self.lista_arrastando = None

    # ---------------------------------------------------------------------- #
    # Helpers de desenho genericos
    # ---------------------------------------------------------------------- #

    def _desenhar_pontos(self, curva):
        """Desenha pontos de controle e labels de qualquer curva."""
        if not curva.pontos:
            return

        xs = [p["x"] for p in curva.pontos]
        ys = [p["y"] for p in curva.pontos]

        self.ax.scatter(
            xs, ys, s=55, zorder=5,
            color=_cor(curva.cor_ponto),
            edgecolors=_cor(curva.cor_borda),
            linewidths=1.8
        )
        for i, (px, py) in enumerate(zip(xs, ys)):
            self.ax.text(
                px + 7, py + 7,
                curva.prefixo_label + str(i),
                fontsize=9, fontweight="bold",
                color=_cor(curva.cor_borda), zorder=5
            )

    def _desenhar_poligonal(self, curva):
        """Desenha a poligonal de controle (linha tracejada) de qualquer curva."""
        if len(curva.pontos) < 2:
            return
        xs = [p["x"] for p in curva.pontos]
        ys = [p["y"] for p in curva.pontos]
        self.ax.plot(
            xs, ys,
            color=_cor(curva.cor_poligonal),
            linestyle="--", linewidth=1, zorder=2
        )

    # ---------------------------------------------------------------------- #
    # Desenho especifico de cada curva
    # ---------------------------------------------------------------------- #

    def _desenhar_curva_bspline(self):
        """Desenha a curva B-spline usando o algoritmo de Cox-de Boor."""
        if not self.bspline.pronto():
            return

        nos   = self.bspline._gerar_vetor_nos(len(self.bspline.pontos))
        t_ini = nos[self.bspline.GRAU]
        t_fim = nos[len(self.bspline.pontos)]
        dt    = (t_fim - t_ini) / PASSOS

        xs, ys = [], []
        t = t_ini
        while t <= t_fim + 1e-12:
            cx, cy, _ = self.bspline.calcular_ponto(min(t, t_fim))
            xs.append(cx)
            ys.append(cy)
            t += dt

        self.ax.plot(xs, ys, color=_cor(self.bspline.cor_curva), linewidth=2, zorder=3)

    def _desenhar_curva_bezier(self):
        """Desenha a curva Bezier usando o algoritmo de De Casteljau."""
        if not self.bezier.pronto():
            return

        xs, ys = [], []
        for i in range(PASSOS + 1):
            cx, cy, _ = self.bezier.calcular_ponto(i / PASSOS)
            xs.append(cx)
            ys.append(cy)

        self.ax.plot(xs, ys, color=_cor(self.bezier.cor_curva), linewidth=2, zorder=3)

    # ---------------------------------------------------------------------- #
    # Titulo / status
    # ---------------------------------------------------------------------- #

    def _atualizar_titulo(self):
        curva  = self._curva_ativa()
        partes = [f"Modo: {curva.nome}"]

        faltando = curva.min_pontos - len(curva.pontos)
        if faltando > 0:
            partes.append(f"adicione mais {faltando} ponto(s)")

        ativas = []
        if self.continuidade_c0:
            ativas.append("C0")
        if self.continuidade_c1:
            ativas.append("C1")
        if self.continuidade_c2:
            ativas.append("C2")
        if ativas:
            partes.append("Continuidade ativa: " + ", ".join(ativas))

        self.ax.set_title("   |   ".join(partes), fontsize=10, pad=6)

    # ---------------------------------------------------------------------- #
    # Redesenho geral
    # ---------------------------------------------------------------------- #

    def redesenhar(self):
        # Preserva o zoom/pan atual do usuario
        xlim = self.ax.get_xlim()
        ylim = self.ax.get_ylim()

        self.ax.cla()
        self._configurar_eixos()

        # Restaura a view do usuario apos cla()
        self.ax.set_xlim(xlim)
        self.ax.set_ylim(ylim)

        self._atualizar_titulo()

        # --- B-spline ---
        self._desenhar_poligonal(self.bspline)
        self._desenhar_curva_bspline()
        self._desenhar_pontos(self.bspline)

        # --- Bezier ---
        self._desenhar_poligonal(self.bezier)
        self._desenhar_curva_bezier()
        self._desenhar_pontos(self.bezier)

        # --- Marcador de juncao C0 ---
        if self.continuidade_c0 and self.bspline.pontos:
            p = self.bspline.pontos[-1]
            self.ax.add_patch(Circle(
                (p["x"], p["y"]), radius=8,
                fill=False, edgecolor="goldenrod", linewidth=3, zorder=6
            ))
            self.ax.text(
                p["x"], p["y"] + 15, "Juncao C0",
                fontsize=9, fontweight="bold",
                color="goldenrod", ha="center", zorder=6
            )

        # --- Vetores tangente e curvatura ---
        self.desenhar_tangentes()
        self.desenhar_curvaturas()

        self.mpl_canvas.draw()


if __name__ == "__main__":
    janela = tk.Tk()
    app = AplicativoCurvas(janela)
    janela.mainloop()
