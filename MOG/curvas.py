#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Trabalho de Computacao Grafica - Partes 2 e 3
B-spline Grau 4 (Nao Uniforme) + Bezier Grau 5
Passo 2: Duas curvas no mesmo canvas com alternancia via botao toggle
"""

import tkinter as tk


class AplicativoCurvas:
    def __init__(self, raiz):
        self.raiz = raiz
        self.raiz.title("B-spline Grau 4 + Bezier Grau 5")
        self.raiz.geometry("800x600")

        self.pontos_bspline = []
        self.pontos_bezier = []

        self.modo_ativo = "bspline"

        self.arrastando = None
        self.lista_arrastando = None
        self.raio_ponto = 6

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

    def _lista_ativa(self):
        return self.pontos_bspline if self.modo_ativo == "bspline" else self.pontos_bezier

    def _min_pontos_ativos(self):
        return 5 if self.modo_ativo == "bspline" else 6

    def _nome_curva_ativa(self):
        return "B-spline Grau 4" if self.modo_ativo == "bspline" else "Bezier Grau 5"

    def _cor_destaque(self):
        return "darkblue" if self.modo_ativo == "bspline" else "darkgreen"

    # ---------- Modo ----------

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
        pontos = self._lista_ativa()

        for i, ponto in enumerate(pontos):
            distancia = ((ponto["x"] - x) ** 2 + (ponto["y"] - y) ** 2) ** 0.5
            if distancia <= self.raio_ponto + 5:
                self.arrastando = i
                self.lista_arrastando = self.modo_ativo
                return

        if self.modo_ativo == "bezier" and len(pontos) >= 6:
            self.redesenhar()  # para atualizar a mensagem de limite
            return

        pontos.append({"x": x, "y": y})
        self.redesenhar()

    def arrastar(self, evento):
        if self.arrastando is not None and self.lista_arrastando == self.modo_ativo:
            pontos = self._lista_ativa()
            pontos[self.arrastando]["x"] = evento.x
            pontos[self.arrastando]["y"] = evento.y
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
            text="Modo atual: " + self._nome_curva_ativa(),
            font=("Arial", 12, "bold"),
            fill=self._cor_destaque(),
            tags="modo_texto"
        )
        faltando = self._min_pontos_ativos() - len(self._lista_ativa())
        if faltando > 0:
            nome = "B-spline" if self.modo_ativo == "bspline" else "Bezier"
            self.canvas.create_text(
                400, 52,
                text="Adicione mais %d ponto(s) para ver a curva %s!" % (faltando, nome),
                font=("Arial", 10), fill="orange",
                tags="aviso"
            )
        elif self.modo_ativo == "bezier" and len(self._lista_ativa()) > 6:
            self.canvas.create_text(
                400, 52,
                text="Curva Bezier grau 5 usa exatamente 6 pontos!",
                font=("Arial", 10), fill="red",
                tags="aviso"
            )

    # ========== B-spline ==========

    def gerar_vetor_nos(self, num_pontos):
        p = 4
        n = num_pontos + p + 1
        nos = []
        for _ in range(p + 1):
            nos.append(0)
        for i in range(1, num_pontos - p):
            nos.append(i)
        ultimo_valor = num_pontos - p
        for _ in range(p + 1):
            nos.append(ultimo_valor)
        return nos

    def funcao_base(self, i, p, t, nos):
        if p == 0:
            if nos[i] <= t <= nos[i + 1]:
                if t == nos[i + 1] and i < len(nos) - 2:
                    return 0
                return 1
            return 0

        resultado = 0.0

        den_esq = nos[i + p] - nos[i]
        if den_esq != 0:
            resultado += ((t - nos[i]) / den_esq) * self.funcao_base(i, p - 1, t, nos)

        den_dir = nos[i + p + 1] - nos[i + 1]
        if den_dir != 0:
            resultado += ((nos[i + p + 1] - t) / den_dir) * self.funcao_base(i + 1, p - 1, t, nos)

        return resultado

    def calcular_ponto_bspline(self, t, nos):
        p = 4
        x = 0.0
        y = 0.0
        for i in range(len(self.pontos_bspline)):
            Ni = self.funcao_base(i, p, t, nos)
            x += Ni * self.pontos_bspline[i]["x"]
            y += Ni * self.pontos_bspline[i]["y"]
        return x, y

    def desenhar_bspline(self):
        num = len(self.pontos_bspline)
        if num < 5:
            return
        nos = self.gerar_vetor_nos(num)
        t_ini = nos[4]
        t_fim = nos[num]
        passos = 100
        dt = (t_fim - t_ini) / passos
        coords = []
        t = t_ini
        while t <= t_fim:
            x, y = self.calcular_ponto_bspline(t, nos)
            coords.extend([x, y])
            t += dt
        if len(coords) >= 4:
            self.canvas.create_line(coords, fill="red", width=2, smooth=True)

    # ========== Bezier Grau 5 (De Casteljau) ==========

    def de_casteljau(self, t):
        n = 5
        pontos = [[p["x"], p["y"]] for p in self.pontos_bezier]
        for k in range(1, n + 1):
            for i in range(n - k + 1):
                pontos[i][0] = (1 - t) * pontos[i][0] + t * pontos[i + 1][0]
                pontos[i][1] = (1 - t) * pontos[i][1] + t * pontos[i + 1][1]
        return pontos[0][0], pontos[0][1]

    def desenhar_bezier(self):
        if len(self.pontos_bezier) != 6:
            return
        passos = 100
        dt = 1.0 / passos
        coords = []
        t = 0.0
        while t <= 1.0:
            x, y = self.de_casteljau(t)
            coords.extend([x, y])
            t += dt
        if len(coords) >= 4:
            self.canvas.create_line(coords, fill="green3", width=2, smooth=True)

    # ========== Desenho Geral ==========

    def redesenhar(self):
        self.canvas.delete("all")
        self.desenhar_instrucoes()

        # --- B-spline ---
        if len(self.pontos_bspline) > 1:
            c = []
            for p in self.pontos_bspline:
                c.extend([p["x"], p["y"]])
            self.canvas.create_line(c, fill="lightgray", dash=(4, 4), width=1)

        for i, p in enumerate(self.pontos_bspline):
            r = self.raio_ponto
            self.canvas.create_oval(
                p["x"] - r, p["y"] - r, p["x"] + r, p["y"] + r,
                fill="blue", outline="darkblue", width=2
            )
            self.canvas.create_text(
                p["x"] + 12, p["y"] - 12,
                text="B%d" % i, font=("Arial", 10, "bold"), fill="darkblue"
            )

        self.desenhar_bspline()

        # --- Bezier ---
        if len(self.pontos_bezier) > 1:
            c = []
            for p in self.pontos_bezier:
                c.extend([p["x"], p["y"]])
            self.canvas.create_line(c, fill="lightgreen", dash=(4, 4), width=1)

        for i, p in enumerate(self.pontos_bezier):
            r = self.raio_ponto
            self.canvas.create_oval(
                p["x"] - r, p["y"] - r, p["x"] + r, p["y"] + r,
                fill="green2", outline="darkgreen", width=2
            )
            self.canvas.create_text(
                p["x"] + 12, p["y"] - 12,
                text="Z%d" % i, font=("Arial", 10, "bold"), fill="darkgreen"
            )

        self.desenhar_bezier()


if __name__ == "__main__":
    janela = tk.Tk()
    app = AplicativoCurvas(janela)
    janela.mainloop()
