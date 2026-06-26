#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Bezier:

    GRAU = 5

    def __init__(self):
        self.pontos = []

    def adicionar_ponto(self, x, y, z=0):
        if len(self.pontos) < self.max_pontos:
            self.pontos.append({"x": x, "y": y, "z": z})
            return True
        return False

    def pode_adicionar(self):
        return len(self.pontos) < self.max_pontos

    def pronto(self):
        return len(self.pontos) == self.max_pontos

    @property
    def min_pontos(self):
        return self.GRAU + 1

    @property
    def max_pontos(self):
        return self.GRAU + 1

    @property
    def nome(self):
        return "Bezier Grau 5"

    @property
    def cor_ponto(self):
        return "green2"

    @property
    def cor_borda(self):
        return "darkgreen"

    @property
    def cor_curva(self):
        return "green3"

    @property
    def cor_poligonal(self):
        return "lightgreen"

    @property
    def prefixo_label(self):
        return "Z"

    def calcular_ponto(self, t):
        return self._de_casteljau(t)

    def derivada_no_inicio(self):
        n = self.GRAU
        if len(self.pontos) < 2:
            return 0.0, 0.0, 0.0

        return (
            n * (self.pontos[1]["x"] - self.pontos[0]["x"]),
            n * (self.pontos[1]["y"] - self.pontos[0]["y"]),
            n * (self.pontos[1]["z"] - self.pontos[0]["z"]),
        )

    def derivada_segunda_no_inicio(self):
        n = self.GRAU
        if len(self.pontos) < 3:
            return 0.0, 0.0, 0.0

        return (
            n * (n - 1) * (self.pontos[2]["x"] - 2 * self.pontos[1]["x"] + self.pontos[0]["x"]),
            n * (n - 1) * (self.pontos[2]["y"] - 2 * self.pontos[1]["y"] + self.pontos[0]["y"]),
            n * (n - 1) * (self.pontos[2]["z"] - 2 * self.pontos[1]["z"] + self.pontos[0]["z"]),
        )

    def _de_casteljau(self, t):
        n = self.GRAU
        pts = [[p["x"], p["y"], p["z"]] for p in self.pontos]
        for k in range(1, n + 1):
            for i in range(n - k + 1):
                pts[i][0] = (1 - t) * pts[i][0] + t * pts[i + 1][0]
                pts[i][1] = (1 - t) * pts[i][1] + t * pts[i + 1][1]
                pts[i][2] = (1 - t) * pts[i][2] + t * pts[i + 1][2]
        return pts[0][0], pts[0][1], pts[0][2]
