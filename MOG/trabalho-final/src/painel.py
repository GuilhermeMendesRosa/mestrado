#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter as tk


class PainelPontos:

    def __init__(self, parent):
        self.frame = parent

        tk.Label(
            self.frame,
            text="Pontos de Controle",
            font=("Arial", 12, "bold"),
            bg="#f8f8f8", fg="#333333",
            pady=8
        ).pack(fill=tk.X)

        tk.Frame(self.frame, height=1, bg="#cccccc").pack(fill=tk.X)

        frame_texto = tk.Frame(self.frame, bg="#f8f8f8")
        frame_texto.pack(fill=tk.BOTH, expand=True, padx=4, pady=6)

        scrollbar = tk.Scrollbar(frame_texto)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.texto = tk.Text(
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
        self.texto.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.config(command=self.texto.yview)

        self._configurar_tags()

    def _configurar_tags(self):
        self.texto.tag_config(
            "header_bs", foreground="#1a1aff", font=("Arial", 10, "bold"))
        self.texto.tag_config(
            "ponto_bs",  foreground="#000099", font=("Courier", 10))
        self.texto.tag_config(
            "header_bz", foreground="#006600", font=("Arial", 10, "bold"))
        self.texto.tag_config(
            "ponto_bz",  foreground="#004d00", font=("Courier", 10))
        self.texto.tag_config(
            "vazio",     foreground="#999999", font=("Arial", 9, "italic"))
        self.texto.tag_config(
            "header_deriv", foreground="#555555", font=("Arial", 10, "bold"))
        self.texto.tag_config(
            "label_d1_bs",  foreground="#cc0000", font=("Courier", 9, "bold"))
        self.texto.tag_config(
            "valor_d1_bs",  foreground="#cc0000", font=("Courier", 10))
        self.texto.tag_config(
            "label_d1_bz",  foreground="#006600", font=("Courier", 9, "bold"))
        self.texto.tag_config(
            "valor_d1_bz",  foreground="#006600", font=("Courier", 10))
        self.texto.tag_config(
            "label_d2_bs",  foreground="#cc6600", font=("Courier", 9, "bold"))
        self.texto.tag_config(
            "valor_d2_bs",  foreground="#cc6600", font=("Courier", 10))
        self.texto.tag_config(
            "label_d2_bz",  foreground="#6600cc", font=("Courier", 9, "bold"))
        self.texto.tag_config(
            "valor_d2_bz",  foreground="#6600cc", font=("Courier", 10))

    def atualizar(self, bspline, bezier, continuidade):
        self.texto.config(state=tk.NORMAL)
        self.texto.delete("1.0", tk.END)

        self.texto.insert(tk.END, "\u2500\u2500 B-spline \u2500\u2500\n", "header_bs")
        if bspline.pontos:
            for i, p in enumerate(bspline.pontos):
                linha = "  B%d: (%d, %d, %d)\n" % (i, round(p["x"]), round(p["y"]), round(p["z"]))
                self.texto.insert(tk.END, linha, "ponto_bs")
        else:
            self.texto.insert(tk.END, "  (sem pontos)\n", "vazio")

        self.texto.insert(tk.END, "\n")

        self.texto.insert(tk.END, "\u2500\u2500\u2500 Bezier \u2500\u2500\u2500\n", "header_bz")
        if bezier.pontos:
            for i, p in enumerate(bezier.pontos):
                linha = "  Z%d: (%d, %d, %d)\n" % (i, round(p["x"]), round(p["y"]), round(p["z"]))
                self.texto.insert(tk.END, linha, "ponto_bz")
        else:
            self.texto.insert(tk.END, "  (sem pontos)\n", "vazio")

        if continuidade.c0:
            self.texto.insert(tk.END, "\n")
            self.texto.insert(tk.END, "\u2500\u2500 Derivadas \u2500\u2500\n", "header_deriv")

            if continuidade.pode_aplicar_c1(bspline, bezier):
                dx_bs, dy_bs, dz_bs = bspline.derivada_no_fim()
                dx_bz, dy_bz, dz_bz = bezier.derivada_no_inicio()
                self.texto.insert(tk.END, "  B'(fim):\n", "label_d1_bs")
                self.texto.insert(tk.END, "    (%.1f, %.1f, %.1f)\n" % (dx_bs, dy_bs, dz_bs), "valor_d1_bs")
                self.texto.insert(tk.END, "  Z'(inicio):\n", "label_d1_bz")
                self.texto.insert(tk.END, "    (%.1f, %.1f, %.1f)\n" % (dx_bz, dy_bz, dz_bz), "valor_d1_bz")

            if continuidade.pode_aplicar_c2(bspline, bezier):
                dx_bs2, dy_bs2, dz_bs2 = bspline.derivada_segunda_no_fim()
                dx_bz2, dy_bz2, dz_bz2 = bezier.derivada_segunda_no_inicio()
                self.texto.insert(tk.END, "  B''(fim):\n", "label_d2_bs")
                self.texto.insert(tk.END, "    (%.1f, %.1f, %.1f)\n" % (dx_bs2, dy_bs2, dz_bs2), "valor_d2_bs")
                self.texto.insert(tk.END, "  Z''(inicio):\n", "label_d2_bz")
                self.texto.insert(tk.END, "    (%.1f, %.1f, %.1f)\n" % (dx_bz2, dy_bz2, dz_bz2), "valor_d2_bz")

        self.texto.config(state=tk.DISABLED)
