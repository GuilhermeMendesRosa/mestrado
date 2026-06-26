#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
GerenciadorContinuidade - Logica pura de continuidade geometrica C0/C1/C2.
Sem dependencia de Tkinter.
"""


class GerenciadorContinuidade:
    """Gerencia os estados e a aplicacao das continuidades C0, C1 e C2."""

    def __init__(self):
        self.c0 = False
        self.c1 = False
        self.c2 = False

    def invalidar(self):
        self.c0 = False
        self.c1 = False
        self.c2 = False

    def pode_aplicar_c1(self, bspline, bezier):
        return (
            bspline.pronto() and bezier.pronto()
            and len(bspline.pontos) >= 2
        )

    def pode_aplicar_c2(self, bspline, bezier):
        return (
            bspline.pronto() and bezier.pronto()
            and len(bspline.pontos) >= 3
        )

    def aplicar_c0(self, bspline, bezier):
        """Translada a Bezier para unir as curvas com continuidade C0."""
        if not bspline.pronto() or not bezier.pronto():
            return False

        ultimo_bsp = bspline.pontos[-1]
        primeiro_bez = bezier.pontos[0]

        dx = ultimo_bsp["x"] - primeiro_bez["x"]
        dy = ultimo_bsp["y"] - primeiro_bez["y"]

        for p in bezier.pontos:
            p["x"] += dx
            p["y"] += dy

        self.c0 = True
        return True

    def aplicar_c1(self, bspline, bezier):
        """Ajusta Z_1 para igualar tangentes: C1."""
        if not self.pode_aplicar_c1(bspline, bezier):
            return False

        if not self.c0:
            if not self.aplicar_c0(bspline, bezier):
                return False

        jx = bspline.pontos[-1]["x"]
        jy = bspline.pontos[-1]["y"]

        dx_bs, dy_bs, _ = bspline.derivada_no_fim()

        bezier.pontos[1]["x"] = jx + dx_bs / 5
        bezier.pontos[1]["y"] = jy + dy_bs / 5

        self.c1 = True
        self.c2 = False
        return True

    def aplicar_c2(self, bspline, bezier):
        """Ajusta Z_2 para igualar curvaturas: C2."""
        if not self.pode_aplicar_c2(bspline, bezier):
            return False

        if not self.c0:
            if not self.aplicar_c0(bspline, bezier):
                return False

        if not self.c1:
            if not self.aplicar_c1(bspline, bezier):
                return False

        dx_bs2, dy_bs2, _ = bspline.derivada_segunda_no_fim()

        z0 = bezier.pontos[0]
        z1 = bezier.pontos[1]

        bezier.pontos[2]["x"] = dx_bs2 / 20.0 + 2 * z1["x"] - z0["x"]
        bezier.pontos[2]["y"] = dy_bs2 / 20.0 + 2 * z1["y"] - z0["y"]

        self.c2 = True
        return True
