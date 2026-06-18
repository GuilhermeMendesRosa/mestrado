#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Trabalho de Computacao Grafica - Partes 2 e 3
Main: Tkinter + matplotlib + mouse + renderizacao 3D (Z=0)
Curvas: B-spline Grau 4 (nao uniforme) e Bezier Grau 5
"""

import tkinter as tk

import matplotlib
matplotlib.use("TkAgg")

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from bspline import BSpline
from bezier import Bezier


class AplicativoCurvas:
    """Janela principal. Gerencia as duas curvas via composicao (POO)."""

    LARGURA = 800
    ALTURA = 600

    def __init__(self, raiz):
        self.raiz = raiz
        self.raiz.title("B-spline Grau 4 + Bezier Grau 5")
        self.raiz.geometry(f"{self.LARGURA}x{self.ALTURA}")

        self.bspline = BSpline()
        self.bezier = Bezier()

        self.modo_ativo = "bspline"

        self.arrastando = None
        self.lista_arrastando = None
        self.raio_ponto = 6

        self.pan_mode = False
        self.pan_start_x = None
        self.pan_start_y = None
        self.pan_xlim = None
        self.pan_ylim = None

        # ---- Matplotlib Figure ----
        self.fig = Figure(figsize=(self.LARGURA / 100, self.ALTURA / 100), dpi=100)
        self.ax = self.fig.add_subplot(111)
        self.ax.set_xlim(0, self.LARGURA)
        self.ax.set_ylim(0, self.ALTURA)
        self.ax.set_aspect("equal")
        self.ax.grid(True, alpha=0.3)

        # ---- Layout ----
        self.frame_top = tk.Frame(raiz)
        self.frame_top.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        self.label_info = tk.Label(
            self.frame_top,
            text="Clique no canvas para adicionar pontos. Arraste para move-los.",
            font=("Arial", 10), fg="gray50", anchor="w",
        )
        self.label_info.pack(side=tk.TOP, fill=tk.X, padx=10, pady=(4, 0))

        self.label_modo = tk.Label(
            self.frame_top, text="", font=("Arial", 11, "bold"), anchor="w",
        )
        self.label_modo.pack(side=tk.TOP, fill=tk.X, padx=10)

        self.canvas = FigureCanvasTkAgg(self.fig, master=self.frame_top)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        # ---- Controles (rodapé) ----
        self.frame_controle = tk.Frame(raiz)
        self.frame_controle.pack(side=tk.BOTTOM, fill=tk.X, pady=5)

        self.botao_modo = tk.Button(
            self.frame_controle, text="Modo: B-spline",
            command=self.alternar_modo, font=("Arial", 12, "bold"),
            bg="#d0d0ff", width=14,
        )
        self.botao_modo.pack(side=tk.LEFT, padx=(5, 2))

        self.botao_reset = tk.Button(
            self.frame_controle, text="Reset Zoom",
            command=self.reset_zoom, font=("Arial", 10),
            width=10,
        )
        self.botao_reset.pack(side=tk.LEFT, padx=2)

        self.botao_limpar = tk.Button(
            self.frame_controle, text="Limpar Tudo",
            command=self.limpar_tudo, font=("Arial", 10),
            width=10,
        )
        self.botao_limpar.pack(side=tk.LEFT, padx=2)

        # ---- Eventos matplotlib ----
        self.fig.canvas.mpl_connect("button_press_event", self.clique)
        self.fig.canvas.mpl_connect("motion_notify_event", self.arrastar)
        self.fig.canvas.mpl_connect("button_release_event", self.soltar)
        self.fig.canvas.mpl_connect("scroll_event", self.zoom_scroll)

        self.redesenhar()

    # ---------- Modo ----------

    def _curva_ativa(self):
        return self.bspline if self.modo_ativo == "bspline" else self.bezier

    def alternar_modo(self):
        self.arrastando = None
        self.lista_arrastando = None
        if self.modo_ativo == "bspline":
            self.modo_ativo = "bezier"
            self.botao_modo.config(text="Modo: Bezier", bg="#d0ffd0")
        else:
            self.modo_ativo = "bspline"
            self.botao_modo.config(text="Modo: B-spline", bg="#d0d0ff")
        self.redesenhar()

    # ---------- Zoom / Pan / Limpar ----------

    def reset_zoom(self):
        self.ax.set_xlim(0, self.LARGURA)
        self.ax.set_ylim(0, self.ALTURA)
        self.ax.set_aspect("equal")
        self.canvas.draw()

    def limpar_tudo(self):
        self.bspline.pontos = []
        self.bezier.pontos = []
        self.arrastando = None
        self.lista_arrastando = None
        self.pan_mode = False
        self.redesenhar()

    def zoom_scroll(self, event):
        if event.inaxes != self.ax:
            return
        scale = 0.85 if event.button == "up" else 1.15
        xlim = self.ax.get_xlim()
        ylim = self.ax.get_ylim()
        cx, cy = event.xdata, event.ydata
        self.ax.set_xlim(
            cx - (cx - xlim[0]) * scale,
            cx - (cx - xlim[1]) * scale,
        )
        self.ax.set_ylim(
            cy - (cy - ylim[0]) * scale,
            cy - (cy - ylim[1]) * scale,
        )
        self.canvas.draw()

    # ---------- Mouse ----------

    def clique(self, event):
        if event.inaxes != self.ax:
            return
        if event.button == 3:
            self.pan_mode = True
            self.pan_start_x = event.xdata
            self.pan_start_y = event.ydata
            self.pan_xlim = self.ax.get_xlim()
            self.pan_ylim = self.ax.get_ylim()
            return
        if event.button != 1:
            return

        x, y = event.xdata, event.ydata
        curva = self._curva_ativa()

        for i, ponto in enumerate(curva.pontos):
            dist = ((ponto["x"] - x) ** 2 + (ponto["y"] - y) ** 2) ** 0.5
            if dist <= self.raio_ponto + 5:
                self.arrastando = i
                self.lista_arrastando = self.modo_ativo
                return

        if curva.pode_adicionar():
            curva.adicionar_ponto(x, y)
        self.redesenhar()

    def arrastar(self, event):
        if event.inaxes != self.ax or event.xdata is None:
            if self.pan_mode:
                self.pan_mode = False
            return

        if self.pan_mode:
            dx = event.xdata - self.pan_start_x
            dy = event.ydata - self.pan_start_y
            self.ax.set_xlim(
                self.pan_xlim[0] - dx,
                self.pan_xlim[1] - dx,
            )
            self.ax.set_ylim(
                self.pan_ylim[0] - dy,
                self.pan_ylim[1] - dy,
            )
            self.canvas.draw()
            return

        if self.arrastando is not None and self.lista_arrastando == self.modo_ativo:
            curva = self._curva_ativa()
            curva.pontos[self.arrastando]["x"] = event.xdata
            curva.pontos[self.arrastando]["y"] = event.ydata
            self.redesenhar()

    def soltar(self, event):
        if event.button == 3:
            self.pan_mode = False
            return
        self.arrastando = None
        self.lista_arrastando = None

    # ---------- Labels ----------

    def _atualizar_labels(self):
        curva = self._curva_ativa()
        self.label_modo.config(text=f"Modo atual: {curva.nome}", fg=curva.cor_borda)

        faltando = curva.min_pontos - len(curva.pontos)
        if faltando > 0:
            self.label_info.config(
                text=(
                    f"Clique para adicionar pontos. "
                    f"Adicione mais {faltando} ponto(s) para ver a curva {curva.nome}!"
                ),
                fg="orange",
            )
        elif (
            self.modo_ativo == "bezier"
            and not self.bezier.pode_adicionar()
            and len(self.bezier.pontos) > self.bezier.max_pontos
        ):
            self.label_info.config(
                text="Curva Bezier grau 5 usa exatamente 6 pontos!",
                fg="red",
            )
        else:
            self.label_info.config(
                text="Scroll para zoom | Botao direito para arrastar | Clique para pontos",
                fg="gray50",
            )

    # ---------- Desenho ----------

    def desenhar_pontos(self, curva):
        if not curva.pontos:
            return
        xs = [p["x"] for p in curva.pontos]
        ys = [p["y"] for p in curva.pontos]
        self.ax.scatter(
            xs, ys, s=200, color=curva.cor_ponto,
            edgecolors=curva.cor_borda, linewidths=2, zorder=4,
        )
        for i, p in enumerate(curva.pontos):
            self.ax.annotate(
                f"{curva.prefixo_label}{i}",
                (p["x"], p["y"]),
                xytext=(10, -10), textcoords="offset points",
                fontsize=10, fontweight="bold", color=curva.cor_borda, zorder=5,
            )

    def desenhar_poligonal(self, curva):
        if len(curva.pontos) > 1:
            xs = [p["x"] for p in curva.pontos]
            ys = [p["y"] for p in curva.pontos]
            self.ax.plot(xs, ys, "--", color=curva.cor_poligonal, linewidth=1, zorder=1)

    def desenhar_curva_bspline(self):
        if not self.bspline.pronto():
            return
        nos = self.bspline._gerar_vetor_nos(len(self.bspline.pontos))
        t_ini = nos[self.bspline.GRAU]
        t_fim = nos[len(self.bspline.pontos)]
        passos = 100
        dt = (t_fim - t_ini) / passos

        xs, ys = [], []
        t = t_ini
        while t <= t_fim:
            x, y, _ = self.bspline.calcular_ponto(t)
            xs.append(x)
            ys.append(y)
            t += dt
        if xs:
            self.ax.plot(xs, ys, "-", color=self.bspline.cor_curva, linewidth=2, zorder=2)

    def desenhar_curva_bezier(self):
        if not self.bezier.pronto():
            return
        passos = 100
        dt = 1.0 / passos
        xs, ys = [], []
        t = 0.0
        while t <= 1.0:
            x, y, _ = self.bezier.calcular_ponto(t)
            xs.append(x)
            ys.append(y)
            t += dt
        if xs:
            self.ax.plot(xs, ys, "-", color=self.bezier.cor_curva, linewidth=2, zorder=2)

    def redesenhar(self):
        self.ax.clear()
        self.ax.set_xlim(0, self.LARGURA)
        self.ax.set_ylim(0, self.ALTURA)
        self.ax.set_aspect("equal")
        self.ax.grid(True, alpha=0.3)

        self.desenhar_poligonal(self.bspline)
        self.desenhar_pontos(self.bspline)
        self.desenhar_curva_bspline()

        self.desenhar_poligonal(self.bezier)
        self.desenhar_pontos(self.bezier)
        self.desenhar_curva_bezier()

        self._atualizar_labels()
        self.canvas.draw()


if __name__ == "__main__":
    janela = tk.Tk()
    app = AplicativoCurvas(janela)
    janela.mainloop()
