#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Trabalho de Computacao Grafica - Partes 2 e 3
Aplicativo: Tkinter + mouse + renderizacao
Curvas: B-spline Grau 4 (nao uniforme) e Bezier Grau 5
"""

import tkinter as tk
from .bspline import BSpline
from .bezier import Bezier
from .continuidade import GerenciadorContinuidade
from .renderizador import Renderizador
from .painel import PainelPontos


class AplicativoCurvas:
    """Janela principal. Gerencia as duas curvas via composicao (POO)."""

    RAIO_PONTO = 6

    def __init__(self, raiz):
        self.raiz = raiz
        self.raiz.title("B-spline Grau 4 + Bezier Grau 5")
        self.raiz.geometry("1060x620")

        # --- Composicao ---
        self.bspline = BSpline()
        self.bezier = Bezier()
        self.continuidade = GerenciadorContinuidade()

        self.modo_ativo = "bspline"
        self.arrastando = None
        self.lista_arrastando = None

        # -------------------------------------------------------
        # Frame de controle (barra inferior com botoes)
        # -------------------------------------------------------
        self.frame_controle = tk.Frame(raiz, pady=4)
        self.frame_controle.pack(side=tk.BOTTOM, fill=tk.X)

        self.botao_modo = tk.Button(
            self.frame_controle, text="Modo: B-spline",
            command=self.alternar_modo, font=("Arial", 11, "bold"),
            bg="#d0d0ff", width=20
        )
        self.botao_modo.pack(side=tk.LEFT, padx=4)

        self.botao_c0 = tk.Button(
            self.frame_controle, text="Unir curvas (C0)",
            command=self.aplicar_c0, font=("Arial", 11, "bold"),
            bg="#ffffcc", width=18
        )
        self.botao_c0.pack(side=tk.LEFT, padx=4)

        self.botao_c1 = tk.Button(
            self.frame_controle, text="Unir curvas (C1)",
            command=self.aplicar_c1, font=("Arial", 11, "bold"),
            bg="#ffcccc", width=18
        )
        self.botao_c1.pack(side=tk.LEFT, padx=4)

        self.botao_c2 = tk.Button(
            self.frame_controle, text="Unir curvas (C2)",
            command=self.aplicar_c2, font=("Arial", 11, "bold"),
            bg="#ddccff", width=18
        )
        self.botao_c2.pack(side=tk.LEFT, padx=4)

        self.botao_reset = tk.Button(
            self.frame_controle, text="Resetar curvas",
            command=self.resetar_curvas, font=("Arial", 11, "bold"),
            bg="#ffccaa", width=16
        )
        self.botao_reset.pack(side=tk.LEFT, padx=4)

        # -------------------------------------------------------
        # Frame principal: canvas (esq.) + separador + painel (dir.)
        # -------------------------------------------------------
        self.frame_principal = tk.Frame(raiz)
        self.frame_principal.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        self.canvas = tk.Canvas(self.frame_principal, bg="white")
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        sep = tk.Frame(self.frame_principal, width=2, bg="#cccccc")
        sep.pack(side=tk.LEFT, fill=tk.Y)

        # -------------------------------------------------------
        # Painel lateral (construido via PainelPontos)
        # -------------------------------------------------------
        self.frame_pontos = tk.Frame(self.frame_principal, width=220, bg="#f8f8f8")
        self.frame_pontos.pack(side=tk.LEFT, fill=tk.Y)
        self.frame_pontos.pack_propagate(False)
        self.painel = PainelPontos(self.frame_pontos)

        # -------------------------------------------------------
        # Renderizador
        # -------------------------------------------------------
        self.renderizador = Renderizador(
            self.canvas, self.bspline, self.bezier, self.continuidade
        )

        # -------------------------------------------------------
        # Bindings de mouse
        # -------------------------------------------------------
        self.canvas.bind("<Button-1>",       self.clique_esquerdo)
        self.canvas.bind("<B1-Motion>",      self.arrastar)
        self.canvas.bind("<ButtonRelease-1>", self.soltar)

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

    def resetar_curvas(self):
        self.bspline.pontos = []
        self.bezier.pontos = []
        self.arrastando = None
        self.lista_arrastando = None
        self.modo_ativo = "bspline"
        self.botao_modo.config(text="Modo: B-spline", bg="#d0d0ff")
        self._invalidar_continuidades()
        self.redesenhar()

    def _invalidar_continuidades(self):
        self.continuidade.invalidar()
        self.botao_c0.config(text="Unir curvas (C0)", bg="#ffffcc")
        self.botao_c1.config(text="Unir curvas (C1)", bg="#ffcccc")
        self.botao_c2.config(text="Unir curvas (C2)", bg="#ddccff")

    # ---------- Continuidade (thin wrappers) ----------

    def aplicar_c0(self):
        if self.continuidade.aplicar_c0(self.bspline, self.bezier):
            self.botao_c0.config(text="Reaplicar C0", bg="#ccffcc")
            self.redesenhar()

    def aplicar_c1(self):
        if self.continuidade.aplicar_c1(self.bspline, self.bezier):
            self.botao_c1.config(text="Reaplicar C1", bg="#ff6666")
            self.botao_c2.config(text="Unir curvas (C2)", bg="#ddccff")
            self.redesenhar()

    def aplicar_c2(self):
        if self.continuidade.aplicar_c2(self.bspline, self.bezier):
            self.botao_c2.config(text="Reaplicar C2", bg="#9966ff")
            self.redesenhar()

    # ---------- Mouse ----------

    def clique_esquerdo(self, evento):
        x, y = evento.x, evento.y
        curva = self._curva_ativa()

        for i, ponto in enumerate(curva.pontos):
            distancia = ((ponto["x"] - x) ** 2 + (ponto["y"] - y) ** 2) ** 0.5
            if distancia <= self.RAIO_PONTO + 5:
                self.arrastando = i
                self.lista_arrastando = self.modo_ativo
                return

        if curva.pode_adicionar():
            curva.adicionar_ponto(x, y)
            self._invalidar_continuidades()
        self.redesenhar()

    def arrastar(self, evento):
        if self.arrastando is not None and self.lista_arrastando == self.modo_ativo:
            curva = self._curva_ativa()
            curva.pontos[self.arrastando]["x"] = evento.x
            curva.pontos[self.arrastando]["y"] = evento.y
            self._invalidar_continuidades()
            self.redesenhar()

    def soltar(self, evento):
        self.arrastando = None
        self.lista_arrastando = None

    # ---------- Redesenho geral ----------

    def redesenhar(self):
        self.renderizador.redesenhar(self.modo_ativo)
        self.painel.atualizar(self.bspline, self.bezier, self.continuidade)
