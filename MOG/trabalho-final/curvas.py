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
        self.raiz.geometry("1060x620")

        # --- Composicao: Main TEM uma BSpline e TEM uma Bezier ---
        self.bspline = BSpline()
        self.bezier  = Bezier()

        self.modo_ativo = "bspline"

        self.continuidade_c0 = False
        self.continuidade_c1 = False
        self.continuidade_c2 = False

        self.arrastando = None
        self.lista_arrastando = None
        self.raio_ponto = 6

        # Flag de visibilidade das setas de derivada
        self.mostrar_setas = True

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

        self.botao_setas = tk.Button(
            self.frame_controle, text="Ocultar setas",
            command=self.alternar_setas, font=("Arial", 11, "bold"),
            bg="#e0f8ff", width=16
        )
        self.botao_setas.pack(side=tk.LEFT, padx=4)

        # -------------------------------------------------------
        # Frame principal: canvas (esq.) + separador + painel (dir.)
        # -------------------------------------------------------
        self.frame_principal = tk.Frame(raiz)
        self.frame_principal.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        # Canvas principal
        self.canvas = tk.Canvas(self.frame_principal, bg="white")
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Separador vertical
        sep = tk.Frame(self.frame_principal, width=2, bg="#cccccc")
        sep.pack(side=tk.LEFT, fill=tk.Y)

        # -------------------------------------------------------
        # Painel lateral de pontos de controle
        # -------------------------------------------------------
        self.frame_pontos = tk.Frame(self.frame_principal, width=220, bg="#f8f8f8")
        self.frame_pontos.pack(side=tk.LEFT, fill=tk.Y)
        self.frame_pontos.pack_propagate(False)

        tk.Label(
            self.frame_pontos,
            text="Pontos de Controle",
            font=("Arial", 12, "bold"),
            bg="#f8f8f8", fg="#333333",
            pady=8
        ).pack(fill=tk.X)

        tk.Frame(self.frame_pontos, height=1, bg="#cccccc").pack(fill=tk.X)

        frame_texto = tk.Frame(self.frame_pontos, bg="#f8f8f8")
        frame_texto.pack(fill=tk.BOTH, expand=True, padx=4, pady=6)

        scrollbar = tk.Scrollbar(frame_texto)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.texto_pontos = tk.Text(
            frame_texto,
            yscrollcommand=scrollbar.set,
            state=tk.DISABLED,
            font=("Courier", 10),
            bg="#f8f8f8",
            relief=tk.FLAT,
            cursor="arrow",
            wrap=tk.NONE,
            width=22,
        )
        self.texto_pontos.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.config(command=self.texto_pontos.yview)

        # Tags de cor no widget de texto
        self.texto_pontos.tag_config(
            "header_bs", foreground="#1a1aff", font=("Arial", 10, "bold"))
        self.texto_pontos.tag_config(
            "ponto_bs",  foreground="#000099", font=("Courier", 10))
        self.texto_pontos.tag_config(
            "header_bz", foreground="#006600", font=("Arial", 10, "bold"))
        self.texto_pontos.tag_config(
            "ponto_bz",  foreground="#004d00", font=("Courier", 10))
        self.texto_pontos.tag_config(
            "vazio",     foreground="#999999", font=("Arial", 9, "italic"))

        # -------------------------------------------------------
        # Bindings de mouse
        # -------------------------------------------------------
        self.canvas.bind("<Button-1>",       self.clique_esquerdo)
        self.canvas.bind("<B1-Motion>",      self.arrastar)
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

    def _invalidar_continuidades(self):
        self.continuidade_c0 = False
        self.continuidade_c1 = False
        self.continuidade_c2 = False
        self.botao_c0.config(text="Unir curvas (C0)", bg="#ffffcc")
        self.botao_c1.config(text="Unir curvas (C1)", bg="#ffcccc")
        self.botao_c2.config(text="Unir curvas (C2)", bg="#ddccff")

    # ---------- Toggle setas ----------

    def alternar_setas(self):
        """Alterna a visibilidade das setas de tangente e curvatura."""
        self.mostrar_setas = not self.mostrar_setas
        if self.mostrar_setas:
            self.botao_setas.config(text="Ocultar setas", bg="#e0f8ff")
        else:
            self.botao_setas.config(text="Mostrar setas", bg="#c0c0c0")
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

        # Para Bezier grau 5, Z'(0) = 5 * (Z1 - Z0).
        self.bezier.pontos[1]["x"] = jx + dx_bs / 5
        self.bezier.pontos[1]["y"] = jy + dy_bs / 5

        self.continuidade_c1 = True
        self.continuidade_c2 = False
        self.botao_c1.config(text="Reaplicar C1", bg="#ff6666")
        self.botao_c2.config(text="Unir curvas (C2)", bg="#ddccff")
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

        dx_bs2, dy_bs2, _ = self.bspline.derivada_segunda_no_fim()

        z0 = self.bezier.pontos[0]
        z1 = self.bezier.pontos[1]

        # Para Bezier grau 5, Z''(0) = 20 * (Z2 - 2 * Z1 + Z0).
        self.bezier.pontos[2]["x"] = dx_bs2 / 20.0 + 2 * z1["x"] - z0["x"]
        self.bezier.pontos[2]["y"] = dy_bs2 / 20.0 + 2 * z1["y"] - z0["y"]

        self.continuidade_c2 = True
        self.botao_c2.config(text="Reaplicar C2", bg="#9966ff")
        self.redesenhar()

    # ---------- Tangent visualization ----------

    def desenhar_tangentes(self):
        """Desenha vetores tangente na juncao para visualizar C1."""
        if not self.mostrar_setas:
            return
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
        if not self.mostrar_setas:
            return
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

    # ---------- Instrucoes ----------

    def desenhar_instrucoes(self):
        w = self.canvas.winfo_width()
        cx = w // 2 if w > 10 else 400

        self.canvas.create_text(
            cx, 12,
            text="Clique no canvas para adicionar pontos. Arraste para move-los.",
            font=("Arial", 11), fill="gray50"
        )
        self.canvas.create_text(
            cx, 32,
            text="Modo atual: " + self._curva_ativa().nome,
            font=("Arial", 12, "bold"),
            fill=self._curva_ativa().cor_borda,
            tags="modo_texto"
        )
        faltando = self._curva_ativa().min_pontos - len(self._curva_ativa().pontos)
        if faltando > 0:
            self.canvas.create_text(
                cx, 52,
                text="Adicione mais %d ponto(s) para ver a curva %s!" % (faltando, self._curva_ativa().nome),
                font=("Arial", 10), fill="orange",
                tags="aviso"
            )
        elif self.modo_ativo == "bezier" and not self.bezier.pode_adicionar() and len(self.bezier.pontos) > self.bezier.max_pontos:
            self.canvas.create_text(
                cx, 52,
                text="Curva Bezier grau 5 usa exatamente 6 pontos!",
                font=("Arial", 10), fill="red",
                tags="aviso"
            )

        if self.continuidade_c0:
            y_base = 52 if faltando <= 0 else 72
            self.canvas.create_text(
                cx, y_base,
                text="Continuidade C0 ativa — curvas unidas por translacao",
                font=("Arial", 10), fill="green",
                tags="c0_status"
            )

            if self.continuidade_c1:
                self.canvas.create_text(
                    cx, y_base + 20,
                    text="Continuidade C1 ativa — tangentes iguais (derivadas identicas)",
                    font=("Arial", 10, "bold"), fill="darkred",
                    tags="c1_status"
                )

            if self.continuidade_c2:
                self.canvas.create_text(
                    cx, y_base + 40,
                    text="Continuidade C2 ativa — curvaturas iguais (2as derivadas identicas)",
                    font=("Arial", 10, "bold"), fill="#9933cc",
                    tags="c2_status"
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
            self.canvas.create_line(coords, fill=self.bspline.cor_curva, width=2)

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
            self.canvas.create_line(coords, fill=self.bezier.cor_curva, width=2)

    # ---------- Painel lateral: lista de pontos ----------

    def atualizar_painel_pontos(self):
        """Atualiza o painel lateral com as coordenadas atuais dos pontos de controle."""
        self.texto_pontos.config(state=tk.NORMAL)
        self.texto_pontos.delete("1.0", tk.END)

        # --- Secao B-spline ---
        self.texto_pontos.insert(tk.END, "\u2500\u2500 B-spline \u2500\u2500\n", "header_bs")
        if self.bspline.pontos:
            for i, p in enumerate(self.bspline.pontos):
                linha = "  B%d: (%d, %d)\n" % (i, round(p["x"]), round(p["y"]))
                self.texto_pontos.insert(tk.END, linha, "ponto_bs")
        else:
            self.texto_pontos.insert(tk.END, "  (sem pontos)\n", "vazio")

        self.texto_pontos.insert(tk.END, "\n")

        # --- Secao Bezier ---
        self.texto_pontos.insert(tk.END, "\u2500\u2500\u2500 Bezier \u2500\u2500\u2500\n", "header_bz")
        if self.bezier.pontos:
            for i, p in enumerate(self.bezier.pontos):
                linha = "  Z%d: (%d, %d)\n" % (i, round(p["x"]), round(p["y"]))
                self.texto_pontos.insert(tk.END, linha, "ponto_bz")
        else:
            self.texto_pontos.insert(tk.END, "  (sem pontos)\n", "vazio")

        self.texto_pontos.config(state=tk.DISABLED)

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

        # --- Atualiza painel lateral ---
        self.atualizar_painel_pontos()


if __name__ == "__main__":
    janela = tk.Tk()
    app = AplicativoCurvas(janela)
    janela.mainloop()
