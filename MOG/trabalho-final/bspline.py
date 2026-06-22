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

    def derivada_no_fim(self):
        """Derivada C'(t_fim) no endpoint da B-spline grau 4 clamped."""
        derivadas = self._calcular_pontos_derivada(1)
        if not derivadas:
            return 0.0, 0.0, 0.0

        return derivadas[-1]

    def derivada_segunda_no_fim(self):
        """Segunda derivada C''(t_fim) no endpoint da B-spline grau 4 clamped."""
        derivadas = self._calcular_pontos_derivada(2)
        if not derivadas:
            return 0.0, 0.0, 0.0

        return derivadas[-1]

    # ---------- Cox-de Boor (privados) ----------

    def _gerar_vetor_nos(self, num_pontos):
        """
        Gera o vetor de nos aberto/clamped e nao uniforme.
        Os nos internos sao obtidos por parametrizacao chord-length,
        o que os torna dependentes do espacamento entre os pontos de controle.
        """
        p = self.GRAU

        if num_pontos < p + 1:
            return []

        if num_pontos == p + 1:
            return [0.0] * (p + 1) + [1.0] * (p + 1)

        acumulado = [0.0]
        for i in range(1, num_pontos):
            dx = self.pontos[i]["x"] - self.pontos[i - 1]["x"]
            dy = self.pontos[i]["y"] - self.pontos[i - 1]["y"]
            dz = self.pontos[i]["z"] - self.pontos[i - 1]["z"]
            distancia = (dx * dx + dy * dy + dz * dz) ** 0.5
            acumulado.append(acumulado[-1] + distancia)

        total = acumulado[-1]
        if total == 0:
            parametros = [i / (num_pontos - 1) for i in range(num_pontos)]
        else:
            parametros = [valor / total for valor in acumulado]

        nos = [0.0] * (p + 1)
        for j in range(1, num_pontos - p):
            nos.append(sum(parametros[j:j + p]) / p)
        nos.extend([1.0] * (p + 1))
        return nos

    def _funcao_base(self, i, p, t, nos):
        """
        Calcula a funcao base N_{i,p}(t) usando o algoritmo de Cox-de Boor.
        """
        if p == 0:
            if t == nos[-1]:
                return 1 if i == len(self.pontos) - 1 else 0
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

    def _calcular_pontos_derivada(self, ordem):
        """Calcula os pontos de controle da derivada de ordem dada."""
        if ordem < 1:
            return []

        pontos = [(p["x"], p["y"], p["z"]) for p in self.pontos]
        nos = self._gerar_vetor_nos(len(self.pontos))
        grau = self.GRAU

        for _ in range(ordem):
            if len(pontos) < 2 or grau <= 0:
                return []

            pontos_derivada = []
            for i in range(len(pontos) - 1):
                den = nos[i + grau + 1] - nos[i + 1]
                if den == 0:
                    pontos_derivada.append((0.0, 0.0, 0.0))
                    continue

                fator = grau / den
                pontos_derivada.append(
                    (
                        fator * (pontos[i + 1][0] - pontos[i][0]),
                        fator * (pontos[i + 1][1] - pontos[i][1]),
                        fator * (pontos[i + 1][2] - pontos[i][2]),
                    )
                )

            pontos = pontos_derivada
            nos = nos[1:-1]
            grau -= 1

        return pontos
