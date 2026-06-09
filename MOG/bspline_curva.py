#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Trabalho de Computacao Grafica - Parte 2
B-spline Grau 4 (Nao Uniforme)
Passo 1: Janela, pontos de controle e interacao com mouse
"""

import tkinter as tk

class AplicativoBSpline:
    def __init__(self, raiz):
        self.raiz = raiz
        self.raiz.title("B-spline Grau 4 - Pontos de Controle")
        self.raiz.geometry("800x600")

        # Lista para guardar os pontos de controle: cada ponto eh um dicionario {"x": ..., "y": ...}
        self.pontos_controle = []

        # Variavel para saber se estamos arrastando um ponto
        self.arrastando = None
        self.raio_ponto = 6

        # Criar o canvas (area de desenho)
        self.canvas = tk.Canvas(raiz, width=800, height=600, bg="white")
        self.canvas.pack(fill=tk.BOTH, expand=True)

        # Vincular eventos do mouse
        # Botao esquerdo pressionado: adicionar ponto ou comecar a arrastar
        self.canvas.bind("<Button-1>", self.clique_esquerdo)
        # Mover mouse com botao pressionado: arrastar ponto
        self.canvas.bind("<B1-Motion>", self.arrastar)
        # Soltar botao: parar de arrastar
        self.canvas.bind("<ButtonRelease-1>", self.soltar)

        # Desenhar instrucoes na tela
        self.desenhar_instrucoes()

    def desenhar_instrucoes(self):
        """Desenha o texto de instrucoes no canvas."""
        self.canvas.create_text(
            400, 30,
            text="Clique para adicionar pontos de controle. Arraste para mover.",
            font=("Arial", 14),
            fill="gray"
        )
        
        # Aviso sobre quantos pontos faltam para a curva aparecer
        pontos_faltando = 5 - len(self.pontos_controle)
        if pontos_faltando > 0:
            self.canvas.create_text(
                400, 55,
                text=f"Adicione mais {pontos_faltando} ponto(s) para ver a curva B-spline grau 4!",
                font=("Arial", 12),
                fill="orange",
                tags="aviso"
            )

    def clique_esquerdo(self, evento):
        """
        Chamado quando o usuario clica com o botao esquerdo do mouse.
        Se clicou perto de um ponto existente, comeca a arrastar.
        Senao, cria um novo ponto de controle.
        """
        x, y = evento.x, evento.y

        # Verifica se clicou perto de um ponto existente
        for i, ponto in enumerate(self.pontos_controle):
            distancia = ((ponto["x"] - x) ** 2 + (ponto["y"] - y) ** 2) ** 0.5
            if distancia <= self.raio_ponto + 5:  # +5 de tolerancia
                self.arrastando = i
                return

        # Se nao clicou em nenhum ponto, cria um novo
        self.pontos_controle.append({"x": x, "y": y})
        self.redesenhar()

    def arrastar(self, evento):
        """
        Chamado quando o usuario move o mouse com o botao esquerdo pressionado.
        Atualiza a posicao do ponto que esta sendo arrastado.
        """
        if self.arrastando is not None:
            self.pontos_controle[self.arrastando]["x"] = evento.x
            self.pontos_controle[self.arrastando]["y"] = evento.y
            self.redesenhar()

    def soltar(self, evento):
        """Chamado quando o usuario solta o botao do mouse."""
        self.arrastando = None

    def gerar_vetor_nos(self, num_pontos):
        """
        Gera o vetor de nos nao uniforme (clamped).
        Para grau p, repetimos o primeiro valor p+1 vezes e o ultimo p+1 vezes.
        Isso forca a curva a passar pelo primeiro e ultimo ponto de controle.
        """
        p = 4  # Grau da B-spline
        # Numero de nos = numero_pontos + grau + 1
        n = num_pontos + p + 1
        nos = []
        
        # Repetir 0 nas primeiras p+1 posicoes
        for i in range(p + 1):
            nos.append(0)
        
        # Valores intermediarios: 1, 2, ..., (num_pontos - p - 1)
        for i in range(1, num_pontos - p):
            nos.append(i)
        
        # Repetir (num_pontos - p) nas ultimas p+1 posicoes
        ultimo_valor = num_pontos - p
        for i in range(p + 1):
            nos.append(ultimo_valor)
        
        return nos

    def funcao_base(self, i, p, t, nos):
        """
        Calcula a funcao base N_{i,p}(t) usando o algoritmo de Cox-de Boor.
        i = indice do ponto de controle
        p = grau
        t = parametro
        nos = vetor de nos
        """
        # Caso base: grau 0
        if p == 0:
            # N_{i,0}(t) = 1 se nos[i] <= t < nos[i+1], senao 0
            # Tratamento especial para o ultimo intervalo
            if nos[i] <= t <= nos[i + 1]:
                # Se for o ultimo no e t for exatamente igual, tambem retorna 1
                if t == nos[i + 1] and i < len(nos) - 2:
                    return 0
                return 1
            return 0
        
        # Caso recursivo
        # Termo esquerdo: ((t - nos[i]) / (nos[i+p] - nos[i])) * N_{i,p-1}(t)
        # Termo direito: ((nos[i+p+1] - t) / (nos[i+p+1] - nos[i+1])) * N_{i+1,p-1}(t)
        
        resultado = 0.0
        
        # Termo esquerdo
        denominador_esq = nos[i + p] - nos[i]
        if denominador_esq != 0:
            coef_esq = (t - nos[i]) / denominador_esq
            resultado += coef_esq * self.funcao_base(i, p - 1, t, nos)
        
        # Termo direito
        denominador_dir = nos[i + p + 1] - nos[i + 1]
        if denominador_dir != 0:
            coef_dir = (nos[i + p + 1] - t) / denominador_dir
            resultado += coef_dir * self.funcao_base(i + 1, p - 1, t, nos)
        
        return resultado

    def calcular_ponto_curva(self, t, nos):
        """
        Calcula o ponto C(t) na curva B-spline.
        C(t) = somatorio de N_{i,p}(t) * P_i
        """
        p = 4  # Grau
        x = 0.0
        y = 0.0
        
        for i in range(len(self.pontos_controle)):
            Ni = self.funcao_base(i, p, t, nos)
            x += Ni * self.pontos_controle[i]["x"]
            y += Ni * self.pontos_controle[i]["y"]
        
        return x, y

    def desenhar_curva(self):
        """
        Desenha a curva B-spline calculando pontos ao longo do parametro t.
        """
        num_pontos = len(self.pontos_controle)
        p = 4  # Grau
        
        # Precisamos de pelo menos p+1 pontos para desenhar a curva
        if num_pontos < p + 1:
            return
        
        nos = self.gerar_vetor_nos(num_pontos)
        
        # O parametro t varia de nos[p] ate nos[num_pontos]
        t_inicial = nos[p]
        t_final = nos[num_pontos]
        
        # Quanto mais passos, mais suave a curva
        passos = 100
        dt = (t_final - t_inicial) / passos
        
        coordenadas = []
        t = t_inicial
        while t <= t_final:
            x, y = self.calcular_ponto_curva(t, nos)
            coordenadas.extend([x, y])
            t += dt
        
        # Desenhar a curva como uma linha vermelha
        if len(coordenadas) >= 4:
            self.canvas.create_line(coordenadas, fill="red", width=2, smooth=True)

    def redesenhar(self):
        """
        Limpa o canvas e redesenha tudo: instrucoes, pontos de controle e linhas.
        """
        self.canvas.delete("all")
        self.desenhar_instrucoes()

        # Desenhar a poligonal de controle (linhas ligando os pontos)
        if len(self.pontos_controle) > 1:
            coordenadas = []
            for ponto in self.pontos_controle:
                coordenadas.extend([ponto["x"], ponto["y"]])
            self.canvas.create_line(coordenadas, fill="lightgray", dash=(4, 4), width=1)

        # Desenhar os pontos de controle
        for i, ponto in enumerate(self.pontos_controle):
            # Circulo preenchido
            self.canvas.create_oval(
                ponto["x"] - self.raio_ponto,
                ponto["y"] - self.raio_ponto,
                ponto["x"] + self.raio_ponto,
                ponto["y"] + self.raio_ponto,
                fill="blue",
                outline="darkblue",
                width=2
            )
            # Numero do ponto
            self.canvas.create_text(
                ponto["x"] + 12,
                ponto["y"] - 12,
                text=str(i),
                font=("Arial", 10),
                fill="darkblue"
            )

        # Desenhar a curva B-spline (se houver pontos suficientes)
        self.desenhar_curva()

# Ponto de entrada do programa
if __name__ == "__main__":
    janela = tk.Tk()
    app = AplicativoBSpline(janela)
    janela.mainloop()
