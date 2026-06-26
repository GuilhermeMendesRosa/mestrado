#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter as tk
from src.aplicativo import AplicativoCurvas


if __name__ == "__main__":
    janela = tk.Tk()
    app = AplicativoCurvas(janela)
    janela.mainloop()
