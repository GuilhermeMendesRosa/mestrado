#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Renderizador:

    def __init__(self, canvas, bspline, bezier, continuidade):
        self.canvas = canvas
        self.bspline = bspline
        self.bezier = bezier
        self.continuidade = continuidade
        self.raio_ponto = 6

    def _curva_ativa(self, modo_ativo):
        return self.bspline if modo_ativo == "bspline" else self.bezier

    def redesenhar(self, modo_ativo):
        self.canvas.delete("all")
        self.desenhar_instrucoes(modo_ativo)

        self.desenhar_poligonal(self.bspline)
        self.desenhar_pontos(self.bspline)
        self.desenhar_curva_bspline()

        self.desenhar_poligonal(self.bezier)
        self.desenhar_pontos(self.bezier)
        self.desenhar_curva_bezier()

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


