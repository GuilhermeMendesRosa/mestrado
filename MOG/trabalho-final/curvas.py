#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Trabalho de Computacao Grafica - Partes 2 e 3
Main: Tkinter + mouse + renderizacao
Curvas: B-spline Grau 4 (nao uniforme) e Bezier Grau 5
"""

import math
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

        self.continuidade_c0 = False
        self.continuidade_c1 = False
        self.continuidade_g1 = False
        self.continuidade_c2 = False
        self.continuidade_g2 = False

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

        self.botao_c0 = tk.Button(
            self.frame_controle, text="Unir curvas (C0)",
            command=self.aplicar_c0, font=("Arial", 11, "bold"),
            bg="#ffffcc", width=22
        )
        self.botao_c0.pack()

        self.botao_c1 = tk.Button(
            self.frame_controle, text="Unir curvas (C1)",
            command=self.aplicar_c1, font=("Arial", 11, "bold"),
            bg="#ffcccc", width=22
        )
        self.botao_c1.pack()

        self.botao_g1 = tk.Button(
            self.frame_controle, text="Unir curvas (G1)",
            command=self.aplicar_g1, font=("Arial", 11, "bold"),
            bg="#ccddff", width=22
        )
        self.botao_g1.pack()

        self.botao_c2 = tk.Button(
            self.frame_controle, text="Unir curvas (C2)",
            command=self.aplicar_c2, font=("Arial", 11, "bold"),
            bg="#ddccff", width=22
        )
        self.botao_c2.pack()

        self.botao_g2 = tk.Button(
            self.frame_controle, text="Unir curvas (G2)",
            command=self.aplicar_g2, font=("Arial", 11, "bold"),
            bg="#ccddcc", width=22
        )
        self.botao_g2.pack()

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

    # ---------- C0 Continuity ----------

    def aplicar_c0(self):
        """Aplica translação para unir as curvas com continuidade C0."""
        if not self.bspline.pronto() or not self.bezier.pronto():
            return

        ultimo_bsp = self.bspline.pontos[-1]
        primeiro_bez = self.bezier.pontos[0]

        dx = ultimo_bsp["x"] - primeiro_bez["x"]
        dy = ultimo_bsp["y"] - primeiro_bez["y"]

        for p in self.bezier.pontos:
            p["x"] += dx
            p["y"] += dy

        self.continuidade_c0 = True
        self.botao_c0.config(text="Reaplicar C0", bg="#ccffcc")
        self.redesenhar()

    # ---------- C1 Continuity ----------

    def _pode_aplicar_c1(self):
        return self.bspline.pronto() and self.bezier.pronto() and len(self.bspline.pontos) >= 2

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

        mag_bs = math.sqrt(dx_bs**2 + dy_bs**2)
        if mag_bs < 1e-9:
            self.continuidade_c1 = False
            self.continuidade_g1 = False
            return

        # C1: 5*(Z_1 - Z_0) = 4*(B_last - B_n-1)
        # Z_1 = Z_0 + (4*(B_last - B_n-1)) / 5 = Z_0 + derivada_bs / 5
        self.bezier.pontos[1]["x"] = jx + dx_bs / 5
        self.bezier.pontos[1]["y"] = jy + dy_bs / 5

        self.continuidade_c1 = True
        self.continuidade_g1 = False
        self.continuidade_c2 = False
        self.continuidade_g2 = False
        self.botao_c1.config(text="Reaplicar C1", bg="#ff6666")
        self.botao_g1.config(text="Unir curvas (G1)", bg="#ccddff")
        self.botao_c2.config(text="Unir curvas (C2)", bg="#ddccff")
        self.botao_g2.config(text="Unir curvas (G2)", bg="#ccddcc")
        self.redesenhar()

    # ---------- G1 Continuity ----------

    def aplicar_g1(self):
        """Ajusta Z_1 para alinhar direcao com B-spline: G1."""
        if not self._pode_aplicar_c1():
            return

        if not self.continuidade_c0:
            self.aplicar_c0()
            if not self.continuidade_c0:
                return

        dx_bs, dy_bs, _ = self.bspline.derivada_no_fim()
        mag_bs = math.sqrt(dx_bs**2 + dy_bs**2)
        if mag_bs < 1e-9:
            self.continuidade_c1 = False
            self.continuidade_g1 = False
            return

        dir_x = dx_bs / mag_bs
        dir_y = dy_bs / mag_bs

        z0 = self.bezier.pontos[0]
        z1_orig = self.bezier.pontos[1]
        dx_z = z1_orig["x"] - z0["x"]
        dy_z = z1_orig["y"] - z0["y"]
        mag_z = math.sqrt(dx_z**2 + dy_z**2)

        if mag_z < 1e-9:
            mag_z = mag_bs * 0.5

        new_x = z0["x"] + dir_x * mag_z
        new_y = z0["y"] + dir_y * mag_z

        self.bezier.pontos[1]["x"] = new_x
        self.bezier.pontos[1]["y"] = new_y

        self.continuidade_c1 = False
        self.continuidade_g1 = True
        self.botao_c1.config(text="Unir curvas (C1)", bg="#ffcccc")
        self.botao_g1.config(text="Reaplicar G1", bg="#6688ff")
        self.continuidade_c2 = False
        self.continuidade_g2 = False
        self.botao_c2.config(text="Unir curvas (C2)", bg="#ddccff")
        self.botao_g2.config(text="Unir curvas (G2)", bg="#ccddcc")
        self.redesenhar()

    # ---------- C2 Continuity ----------

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

        Bn = self.bspline.pontos[-1]
        Bn1 = self.bspline.pontos[-2]
        Bn2 = self.bspline.pontos[-3]

        dx_bs2, dy_bs2, _ = self.bspline.derivada_segunda_no_fim()
        mag_bs2 = math.sqrt(dx_bs2**2 + dy_bs2**2)
        if mag_bs2 < 1e-9:
            self.continuidade_c2 = False
            self.continuidade_g2 = False
            return

        self.bezier.pontos[2]["x"] = (16.0 / 5.0) * Bn["x"] - (14.0 / 5.0) * Bn1["x"] + (3.0 / 5.0) * Bn2["x"]
        self.bezier.pontos[2]["y"] = (16.0 / 5.0) * Bn["y"] - (14.0 / 5.0) * Bn1["y"] + (3.0 / 5.0) * Bn2["y"]

        self.continuidade_c2 = True
        self.continuidade_g2 = False
        self.botao_c2.config(text="Reaplicar C2", bg="#9966ff")
        self.botao_g2.config(text="Unir curvas (G2)", bg="#ccddcc")
        self.redesenhar()

    # ---------- G2 Continuity ----------

    def aplicar_g2(self):
        """Ajusta Z_2 para alinhar direcao da curvatura com B-spline: G2."""
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
        mag_bs2 = math.sqrt(dx_bs2**2 + dy_bs2**2)
        if mag_bs2 < 1e-9:
            return

        dir_x = dx_bs2 / mag_bs2
        dir_y = dy_bs2 / mag_bs2

        dx_bz2_orig, dy_bz2_orig, _ = self.bezier.derivada_segunda_no_inicio()
        mag_bz2 = math.sqrt(dx_bz2_orig**2 + dy_bz2_orig**2)

        if mag_bz2 < 1e-9:
            mag_bz2 = mag_bs2 * 0.5

        target_dx = dir_x * mag_bz2
        target_dy = dir_y * mag_bz2

        jx = self.bspline.pontos[-1]["x"]
        jy = self.bspline.pontos[-1]["y"]
        z1 = self.bezier.pontos[1]

        self.bezier.pontos[2]["x"] = target_dx / 20.0 + 2 * z1["x"] - jx
        self.bezier.pontos[2]["y"] = target_dy / 20.0 + 2 * z1["y"] - jy

        self.continuidade_c2 = False
        self.continuidade_g2 = True
        self.botao_c2.config(text="Unir curvas (C2)", bg="#ddccff")
        self.botao_g2.config(text="Reaplicar G2", bg="#669966")
        self.redesenhar()

    # ---------- Tangent visualization ----------

    def desenhar_tangentes(self):
        """Desenha vetores tangente na juncao e info de C1/G1."""
        if not self.continuidade_c0:
            return
        if not self._pode_aplicar_c1():
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
        self.canvas.create_text(ex1, ey1 - 8,
                                text=f"B'=({dx_bs:.1f},{dy_bs:.1f})",
                                fill="#cc0000", font=("Arial", 8, "bold"),
                                tags="tangente")

        ex2 = jx + dx_bz * scale
        ey2 = jy + dy_bz * scale
        self.canvas.create_line(jx, jy, ex2, ey2,
                                fill="#006600", width=2.5, arrow=tk.LAST,
                                tags="tangente")
        self.canvas.create_text(ex2, ey2 - 8,
                                text=f"Z'=({dx_bz:.1f},{dy_bz:.1f})",
                                fill="#006600", font=("Arial", 8, "bold"),
                                tags="tangente")

    # ---------- Curvature visualization ----------

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

        mag_bs2 = math.sqrt(dx_bs2**2 + dy_bs2**2)
        mag_bz2 = math.sqrt(dx_bz2**2 + dy_bz2**2)

        max_mag = max(mag_bs2, mag_bz2, 1e-9)
        scale = min(30.0, 80.0 / max_mag)

        ex1 = jx + dx_bs2 * scale
        ey1 = jy + dy_bs2 * scale
        self.canvas.create_line(jx, jy, ex1, ey1,
                                fill="#cc6600", width=2.5, arrow=tk.LAST,
                                tags="curvatura")
        self.canvas.create_text(ex1 + 10, ey1,
                                text=f"B''=({dx_bs2:.1f},{dy_bs2:.1f})",
                                fill="#cc6600", font=("Arial", 8, "bold"),
                                tags="curvatura")

        ex2 = jx + dx_bz2 * scale
        ey2 = jy + dy_bz2 * scale
        self.canvas.create_line(jx, jy, ex2, ey2,
                                fill="#6600cc", width=2.5, arrow=tk.LAST,
                                tags="curvatura")
        self.canvas.create_text(ex2 + 10, ey2,
                                text=f"Z''=({dx_bz2:.1f},{dy_bz2:.1f})",
                                fill="#6600cc", font=("Arial", 8, "bold"),
                                tags="curvatura")

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

        if self.continuidade_c0:
            y_base = 52 if faltando <= 0 else 72
            self.canvas.create_text(
                400, y_base,
                text="Continuidade C0 ativa — curvas unidas por translacao",
                font=("Arial", 10), fill="green",
                tags="c0_status"
            )

            if self.continuidade_c1:
                self.canvas.create_text(
                    400, y_base + 20,
                    text="Continuidade C1 ativa — tangentes iguais (derivadas identicas)",
                    font=("Arial", 10, "bold"), fill="darkred",
                    tags="c1_status"
                )
            elif self.continuidade_g1:
                self.canvas.create_text(
                    400, y_base + 20,
                    text="Continuidade G1 ativa — direcoes iguais, magnitudes podem diferir",
                    font=("Arial", 10, "bold"), fill="#2244aa",
                    tags="g1_status"
                )

            if self.continuidade_c2:
                self.canvas.create_text(
                    400, y_base + 40,
                    text="Continuidade C2 ativa — curvaturas iguais (2as derivadas identicas)",
                    font=("Arial", 10, "bold"), fill="#9933cc",
                    tags="c2_status"
                )
            elif self.continuidade_g2:
                self.canvas.create_text(
                    400, y_base + 40,
                    text="Continuidade G2 ativa — direcoes de curvatura iguais, magnitudes podem diferir",
                    font=("Arial", 10, "bold"), fill="#336699",
                    tags="g2_status"
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
            self.canvas.create_line(coords, fill=self.bspline.cor_curva, width=2, smooth=True)

    def desenhar_curva_bezier(self):
        """Desenha a curva Bezier usando o algoritmo de De Casteljau."""
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
            self.canvas.create_line(coords, fill=self.bezier.cor_curva, width=2, smooth=True)

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

        # --- Marcador de juncao C0 ---
        if self.continuidade_c0 and len(self.bspline.pontos) > 0:
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

        # --- Vetores tangente ---
        self.desenhar_tangentes()

        # --- Vetores curvatura ---
        self.desenhar_curvaturas()


if __name__ == "__main__":
    janela = tk.Tk()
    app = AplicativoCurvas(janela)
    janela.mainloop()
