#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
BSpline - Lógica da curva B-spline Grau 4 (Não Uniforme)
"""


class BSpline:
    """Curva B-spline de grau 4 (não uniforme, clamped)."""

    GRAU = 4

    def __init__(self):
        self.pontos = []

    def adicionar_ponto(self, x, y, z=0):
        """Adiciona ponto de controle (ilimitado)."""
        self.pontos.append({"x": x, "y": y, "z": z})

    def pode_adicionar(self):
        """B-spline aceita quantos pontos quiser."""
        return True

    def pronto(self):
        """True se há pontos suficientes para desenhar a curva."""
        return len(self.pontos) >= self.min_pontos

    # ---------- Propriedades (estilo POO) ----------

    @property
    def min_pontos(self):
        return self.GRAU + 1

    @property
    def max_pontos(self):
        return None  # ilimitado

    @property
    def nome(self):
        return "B-spline Grau 4"

    @property
    def cor_ponto(self):
        return "blue"

    @property
    def cor_borda(self):
        return "darkblue"

    @property
    def cor_curva(self):
        return "red"

    @property
    def cor_poligonal(self):
        return "lightgray"

    @property
    def prefixo_label(self):
        return "B"

    # ---------- Cálculo da curva ----------

    def calcular_ponto(self, t):
        """
        Calcula o ponto C(t) na curva B-spline.
        C(t) = somatorio de N_{i,p}(t) * P_i
        """
        nos = self._gerar_vetor_nos(len(self.pontos))
        p = self.GRAU
        x = 0.0
        y = 0.0
        z = 0.0
        for i in range(len(self.pontos)):
            Ni = self._funcao_base(i, p, t, nos)
            x += Ni * self.pontos[i]["x"]
            y += Ni * self.pontos[i]["y"]
            z += Ni * self.pontos[i]["z"]
        return x, y, z

    # ---------- Cox-de Boor (privados) ----------

    def _gerar_vetor_nos(self, num_pontos):
        """
        Gera o vetor de nos nao uniforme (clamped).
        Para grau p, repetimos o primeiro valor p+1 vezes e o ultimo p+1 vezes.
        """
        p = self.GRAU
        n = num_pontos + p + 1
        nos = []
        for _ in range(p + 1):
            nos.append(0)
        for i in range(1, num_pontos - p):
            nos.append(i)
        ultimo = num_pontos - p
        for _ in range(p + 1):
            nos.append(ultimo)
        return nos

    def _funcao_base(self, i, p, t, nos):
        """
        Calcula a funcao base N_{i,p}(t) usando o algoritmo de Cox-de Boor.
        """
        if p == 0:
            if nos[i] <= t <= nos[i + 1]:
                if t == nos[i + 1] and i < len(nos) - 2:
                    return 0
                return 1
            return 0

        resultado = 0.0
        den_esq = nos[i + p] - nos[i]
        if den_esq != 0:
            resultado += ((t - nos[i]) / den_esq) * self._funcao_base(i, p - 1, t, nos)
        den_dir = nos[i + p + 1] - nos[i + 1]
        if den_dir != 0:
            resultado += ((nos[i + p + 1] - t) / den_dir) * self._funcao_base(i + 1, p - 1, t, nos)
        return resultado
