#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Trabalho de Computacao Grafica - Partes 2 e 3
Main: Tkinter + mouse + renderizacao
Curvas: B-spline Grau 4 (nao uniforme) e Bezier Grau 5
"""

import tkinter as tk
from bspline import BSpline
from bezier import Bezier


class AplicativoCurvas:
    """Janela principal. Gerencia as duas curvas via composicao (POO)."""

    def __init__(self, raiz):
        self.raiz = raiz
        self.raiz.title("B-spline Grau 4 + Bezier Grau 5")
        self.raiz.geometry("800x600")

        # --- Composicao: Main TEM uma BSpline e TEM uma Bezier ---
        self.bspline = BSpline()
        self.bezier  = Bezier()

        self.modo_ativo = "bspline"

        self.arrastando = None
        self.lista_arrastando = None
        self.raio_ponto = 6

        # --- Widgets Tkinter ---
        self.frame_controle = tk.Frame(raiz)
        self.frame_controle.pack(side=tk.BOTTOM, fill=tk.X, pady=5)

        self.botao_modo = tk.Button(
            self.frame_controle, text="Modo: B-spline",
            command=self.alternar_modo, font=("Arial", 12, "bold"),
            bg="#d0d0ff", width=22
        )
        self.botao_modo.pack()

        self.canvas = tk.Canvas(raiz, width=800, height=600, bg="white")
        self.canvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        self.canvas.bind("<Button-1>", self.clique_esquerdo)
        self.canvas.bind("<B1-Motion>", self.arrastar)
        self.canvas.bind("<ButtonRelease-1>", self.soltar)

        self.redesenhar()

    # ---------- Modo ----------

    def _curva_ativa(self):
        """Retorna o objeto da curva que esta ativa no momento."""
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

    # ---------- Mouse ----------

    def clique_esquerdo(self, evento):
        x, y = evento.x, evento.y
        curva = self._curva_ativa()

        for i, ponto in enumerate(curva.pontos):
            distancia = ((ponto["x"] - x) ** 2 + (ponto["y"] - y) ** 2) ** 0.5
            if distancia <= self.raio_ponto + 5:
                self.arrastando = i
                self.lista_arrastando = self.modo_ativo
                return

        if curva.pode_adicionar():
            curva.adicionar_ponto(x, y)
        self.redesenhar()

    def arrastar(self, evento):
        if self.arrastando is not None and self.lista_arrastando == self.modo_ativo:
            curva = self._curva_ativa()
            curva.pontos[self.arrastando]["x"] = evento.x
            curva.pontos[self.arrastando]["y"] = evento.y
            self.redesenhar()

    def soltar(self, evento):
        self.arrastando = None
        self.lista_arrastando = None

    # ---------- Instrucoes ----------

    def desenhar_instrucoes(self):
        self.canvas.create_text(
            400, 12,
            text="Clique no canvas para adicionar pontos. Arraste para move-los.",
            font=("Arial", 11), fill="gray50"
        )
        self.canvas.create_text(
            400, 32,
            text="Modo atual: " + self._curva_ativa().nome,
            font=("Arial", 12, "bold"),
            fill=self._curva_ativa().cor_borda,
            tags="modo_texto"
        )
        faltando = self._curva_ativa().min_pontos - len(self._curva_ativa().pontos)
        if faltando > 0:
            self.canvas.create_text(
                400, 52,
                text="Adicione mais %d ponto(s) para ver a curva %s!" % (faltando, self._curva_ativa().nome),
                font=("Arial", 10), fill="orange",
                tags="aviso"
            )
        elif self.modo_ativo == "bezier" and not self.bezier.pode_adicionar() and len(self.bezier.pontos) > self.bezier.max_pontos:
            self.canvas.create_text(
                400, 52,
                text="Curva Bezier grau 5 usa exatamente 6 pontos!",
                font=("Arial", 10), fill="red",
                tags="aviso"
            )

    # ---------- Helpers de desenho (genericamente tipados) ----------

    def desenhar_pontos(self, curva):
        """Desenha pontos de controle e labels de qualquer curva."""
        for i, p in enumerate(curva.pontos):
            r = self.raio_ponto
            self.canvas.create_oval(
                p["x"] - r, p["y"] - r, p["x"] + r, p["y"] + r,
                fill=curva.cor_ponto, outline=curva.cor_borda, width=2
            )
            self.canvas.create_text(
                p["x"] + 12, p["y"] - 12,
                text=curva.prefixo_label + str(i),
                font=("Arial", 10, "bold"), fill=curva.cor_borda
            )

    def desenhar_poligonal(self, curva):
        """Desenha a poligonal de controle (linha tracejada) de qualquer curva."""
        if len(curva.pontos) > 1:
            c = []
            for p in curva.pontos:
                c.extend([p["x"], p["y"]])
            self.canvas.create_line(c, fill=curva.cor_poligonal, dash=(4, 4), width=1)

    # ---------- Desenho especifico de cada curva (EXPLICITO) ----------

    def desenhar_curva_bspline(self):
        """Desenha a curva B-spline usando o algoritmo de Cox-de Boor."""
        if not self.bspline.pronto():
            return

        t_final = len(self.bspline.pontos) - self.bspline.GRAU
        num_amostras = 100
        passo_t = t_final / num_amostras

        pontos_curva = []
        for i in range(num_amostras + 1):
            t = i * passo_t
            x, y = self.bspline.calcular_ponto(t)
            pontos_curva.extend([x, y])

        if len(pontos_curva) >= 4:
            self.canvas.create_line(pontos_curva, fill=self.bspline.cor_curva, width=2, smooth=True)

    def desenhar_curva_bezier(self):
        """Desenha a curva Bezier usando o algoritmo de De Casteljau."""
        if not self.bezier.pronto():
            return

        num_amostras = 100
        passo_t = 1.0 / num_amostras
        pontos_curva = []
        for i in range(num_amostras + 1):
            t = i * passo_t
            x, y = self.bezier.calcular_ponto(t)
            pontos_curva.extend([x, y])

        if len(pontos_curva) >= 4:
            self.canvas.create_line(pontos_curva, fill=self.bezier.cor_curva, width=2, smooth=True)

    # ---------- Redesenho geral (ordem: fundo -> poligonal -> pontos -> curva) ----------

    def redesenhar(self):
        self.canvas.delete("all")
        self.desenhar_instrucoes()

        # --- B-spline ---
        self.desenhar_poligonal(self.bspline)
        self.desenhar_pontos(self.bspline)
        self.desenhar_curva_bspline()

        # --- Bezier ---
        self.desenhar_poligonal(self.bezier)
        self.desenhar_pontos(self.bezier)
        self.desenhar_curva_bezier()


if __name__ == "__main__":
    janela = tk.Tk()
    app = AplicativoCurvas(janela)
    janela.mainloop()
