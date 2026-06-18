#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Bezier - Lógica da curva Bezier Grau 5 (De Casteljau)
"""


class Bezier:
    """Curva Bezier de grau 5 (exatamente 6 pontos de controle)."""

    GRAU = 5

    def __init__(self):
        self.pontos = []

    def adicionar_ponto(self, x, y, z=0):
        """Adiciona ponto se ainda não tiver 6."""
        if len(self.pontos) < self.max_pontos:
            self.pontos.append({"x": x, "y": y, "z": z})
            return True
        return False

    def pode_adicionar(self):
        """True enquanto tiver menos de 6 pontos."""
        return len(self.pontos) < self.max_pontos

    def pronto(self):
        """True exatamente quando há 6 pontos (para desenhar a curva)."""
        return len(self.pontos) == self.max_pontos

    # ---------- Propriedades (estilo POO) ----------

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
        return "#00EE00"

    @property
    def cor_borda(self):
        return "darkgreen"

    @property
    def cor_curva(self):
        return "#00CD00"

    @property
    def cor_poligonal(self):
        return "lightgreen"

    @property
    def prefixo_label(self):
        return "Z"

    # ---------- Cálculo da curva ----------

    def calcular_ponto(self, t):
        """
        Calcula o ponto B(t) na curva Bezier usando De Casteljau.
        """
        return self._de_casteljau(t)

    # ---------- De Casteljau (privado) ----------

    def _de_casteljau(self, t):
        """
        Algoritmo de De Casteljau para grau 5 (3D).
        pontos[i]^(k) = (1-t) * pontos[i]^(k-1) + t * pontos[i+1]^(k-1)
        """
        n = self.GRAU
        pts = [[p["x"], p["y"], p["z"]] for p in self.pontos]
        for k in range(1, n + 1):
            for i in range(n - k + 1):
                pts[i][0] = (1 - t) * pts[i][0] + t * pts[i + 1][0]
                pts[i][1] = (1 - t) * pts[i][1] + t * pts[i + 1][1]
                pts[i][2] = (1 - t) * pts[i][2] + t * pts[i + 1][2]
        return pts[0][0], pts[0][1], pts[0][2]
