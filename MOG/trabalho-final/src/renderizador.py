#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Renderizador - Responsavel por todo desenho no canvas Tkinter.
"""

import math
import tkinter as tk


class Renderizador:
    """Desenha curvas, pontos, poligonais, setas e instrucoes no canvas."""

    def __init__(self, canvas, bspline, bezier, continuidade):
        self.canvas = canvas
        self.bspline = bspline
        self.bezier = bezier
        self.continuidade = continuidade
        self.raio_ponto = 6
        self.mostrar_setas = True

    def _curva_ativa(self, modo_ativo):
        return self.bspline if modo_ativo == "bspline" else self.bezier

    # ---------- Redesenho geral ----------

    def redesenhar(self, modo_ativo):
        self.canvas.delete("all")
        self.desenhar_instrucoes(modo_ativo)

        self.desenhar_poligonal(self.bspline)
        self.desenhar_pontos(self.bspline)
        self.desenhar_curva_bspline()

        self.desenhar_poligonal(self.bezier)
        self.desenhar_pontos(self.bezier)
        self.desenhar_curva_bezier()

        self.desenhar_juncao()
        self.desenhar_tangentes()
        self.desenhar_curvaturas()

    # ---------- Instrucoes ----------

    def desenhar_instrucoes(self, modo_ativo):
        w = self.canvas.winfo_width()
        cx = w // 2 if w > 10 else 400
        curva = self._curva_ativa(modo_ativo)

        self.canvas.create_text(
            cx, 12,
            text="Clique no canvas para adicionar pontos. Arraste para move-los.",
            font=("Arial", 11), fill="gray50"
        )
        self.canvas.create_text(
            cx, 32,
            text="Modo atual: " + curva.nome,
            font=("Arial", 12, "bold"),
            fill=curva.cor_borda,
            tags="modo_texto"
        )
        faltando = curva.min_pontos - len(curva.pontos)
        if faltando > 0:
            self.canvas.create_text(
                cx, 52,
                text="Adicione mais %d ponto(s) para ver a curva %s!" % (faltando, curva.nome),
                font=("Arial", 10), fill="orange",
                tags="aviso"
            )
        elif modo_ativo == "bezier" and not self.bezier.pode_adicionar() and len(self.bezier.pontos) > self.bezier.max_pontos:
            self.canvas.create_text(
                cx, 52,
                text="Curva Bezier grau 5 usa exatamente 6 pontos!",
                font=("Arial", 10), fill="red",
                tags="aviso"
            )

        if self.continuidade.c0:
            y_base = 52 if faltando <= 0 else 72
            self.canvas.create_text(
                cx, y_base,
                text="Continuidade C0 ativa — curvas unidas por translacao",
                font=("Arial", 10), fill="green",
                tags="c0_status"
            )

            if self.continuidade.c1:
                self.canvas.create_text(
                    cx, y_base + 20,
                    text="Continuidade C1 ativa — tangentes iguais (derivadas identicas)",
                    font=("Arial", 10, "bold"), fill="darkred",
                    tags="c1_status"
                )

            if self.continuidade.c2:
                self.canvas.create_text(
                    cx, y_base + 40,
                    text="Continuidade C2 ativa — curvaturas iguais (2as derivadas identicas)",
                    font=("Arial", 10, "bold"), fill="#9933cc",
                    tags="c2_status"
                )

    # ---------- Pontos e poligonal ----------

    def desenhar_pontos(self, curva):
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
        if len(curva.pontos) > 1:
            c = []
            for p in curva.pontos:
                c.extend([p["x"], p["y"]])
            self.canvas.create_line(c, fill=curva.cor_poligonal, dash=(4, 4), width=1)

    # ---------- Curvas ----------

    def desenhar_curva_bspline(self):
        if not self.bspline.pronto():
            return

        nos = self.bspline._gerar_vetor_nos(len(self.bspline.pontos))
        t_ini = nos[self.bspline.GRAU]
        t_fim = nos[len(self.bspline.pontos)]
        passos = 100
        dt = (t_fim - t_ini) / passos

        coords = []
        t = t_ini
        while t <= t_fim:
            x, y, z = self.bspline.calcular_ponto(t)
            coords.extend([x, y])
            t += dt

        if len(coords) >= 4:
            self.canvas.create_line(coords, fill=self.bspline.cor_curva, width=2)

    def desenhar_curva_bezier(self):
        if not self.bezier.pronto():
            return

        passos = 100
        dt = 1.0 / passos
        coords = []
        t = 0.0
        while t <= 1.0:
            x, y, z = self.bezier.calcular_ponto(t)
            coords.extend([x, y])
            t += dt

        if len(coords) >= 4:
            self.canvas.create_line(coords, fill=self.bezier.cor_curva, width=2)

    # ---------- Juncao ----------

    def desenhar_juncao(self):
        if self.continuidade.c0 and len(self.bspline.pontos) > 0:
            p = self.bspline.pontos[-1]
            r = 8
            self.canvas.create_oval(
                p["x"] - r, p["y"] - r, p["x"] + r, p["y"] + r,
                outline="gold", width=3, tags="juncao"
            )
            self.canvas.create_text(
                p["x"], p["y"] - r - 10,
                text="Juncao C0", font=("Arial", 9, "bold"),
                fill="gold", tags="juncao"
            )

    # ---------- Tangentes ----------

    def desenhar_tangentes(self):
        if not self.mostrar_setas:
            return
        if not self.continuidade.c0:
            return
        if not self.continuidade.pode_aplicar_c1(self.bspline, self.bezier):
            return

        jx = self.bspline.pontos[-1]["x"]
        jy = self.bspline.pontos[-1]["y"]

        dx_bs, dy_bs, _ = self.bspline.derivada_no_fim()
        dx_bz, dy_bz, _ = self.bezier.derivada_no_inicio()

        mag_bs = math.sqrt(dx_bs**2 + dy_bs**2)
        mag_bz = math.sqrt(dx_bz**2 + dy_bz**2)

        max_mag = max(mag_bs, mag_bz, 1e-9)
        scale = min(60.0, 150.0 / max_mag)

        ex1 = jx + dx_bs * scale
        ey1 = jy + dy_bs * scale
        self.canvas.create_line(jx, jy, ex1, ey1,
                                fill="#cc0000", width=2.5, arrow=tk.LAST,
                                tags="tangente")

        ex2 = jx + dx_bz * scale
        ey2 = jy + dy_bz * scale
        self.canvas.create_line(jx, jy, ex2, ey2,
                                fill="#006600", width=2.5, arrow=tk.LAST,
                                tags="tangente")

    # ---------- Curvaturas ----------

    def desenhar_curvaturas(self):
        if not self.mostrar_setas:
            return
        if not self.continuidade.c0:
            return
        if not self.continuidade.pode_aplicar_c2(self.bspline, self.bezier):
            return

        jx = self.bspline.pontos[-1]["x"]
        jy = self.bspline.pontos[-1]["y"]

        dx_bs2, dy_bs2, _ = self.bspline.derivada_segunda_no_fim()
        dx_bz2, dy_bz2, _ = self.bezier.derivada_segunda_no_inicio()

        mag_bs2 = math.sqrt(dx_bs2**2 + dy_bs2**2)
        mag_bz2 = math.sqrt(dx_bz2**2 + dy_bz2**2)

        max_mag = max(mag_bs2, mag_bz2, 1e-9)
        scale = min(30.0, 80.0 / max_mag)

        ex1 = jx + dx_bs2 * scale
        ey1 = jy + dy_bs2 * scale
        self.canvas.create_line(jx, jy, ex1, ey1,
                                fill="#cc6600", width=2.5, arrow=tk.LAST,
                                tags="curvatura")

        ex2 = jx + dx_bz2 * scale
        ey2 = jy + dy_bz2 * scale
        self.canvas.create_line(jx, jy, ex2, ey2,
                                fill="#6600cc", width=2.5, arrow=tk.LAST,
                                tags="curvatura")
