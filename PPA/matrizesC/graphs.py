import matplotlib.pyplot as plt

# Dados
dados = {
    250: {
        "threads": list(range(1, 11)),
        "average_time": [
            0.035328, 0.031367, 0.020408, 0.021576, 0.019274, 0.015604, 0.013665, 0.019075,
            0.017397, 0.015845
        ],
        "speedup": [
            1.00, 1.13, 1.73, 1.64, 1.83, 2.26, 2.59, 1.85,
            2.03, 2.23
        ],
        "efficiency": [
            100.00, 56.31, 57.70, 40.93, 36.66, 37.73, 36.93, 23.15,
            22.56, 22.30
        ],
    },
    500: {
        "threads": list(range(1, 11)),
        "average_time": [
            0.328185, 0.239428, 0.214142, 0.166439, 0.137587, 0.149000, 0.173929, 0.164251,
            0.168407, 0.161860
        ],
        "speedup": [
            1.00, 1.37, 1.53, 1.97, 2.39, 2.20, 1.89, 2.00,
            1.95, 2.03
        ],
        "efficiency": [
            100.00, 68.54, 51.09, 49.30, 47.71, 36.71, 26.96, 24.98,
            21.65, 20.28
        ],
    },
    1000: {
        "threads": list(range(1, 11)),
        "average_time": [
            3.933815, 2.707207, 2.103428, 1.782920, 1.602032, 1.486430, 1.610080, 1.665756,
            1.503910, 1.882263
        ],
        "speedup": [
            1.00, 1.45, 1.87, 2.21, 2.46, 2.65, 2.44, 2.36,
            2.62, 2.09
        ],
        "efficiency": [
            100.00, 72.65, 62.34, 55.16, 49.11, 44.11, 34.90, 29.52,
            29.06, 20.90
        ],
    },
}

# Função para plotar
def plotar_graficos(size, info):
    threads = info["threads"]
    avg_time = info["average_time"]
    speedup = info["speedup"]
    efficiency = info["efficiency"]

    plt.figure(figsize=(15, 10))

    plt.subplot(3, 1, 1)
    plt.plot(threads, avg_time, marker='o')
    plt.title(f'Matrix {size}x{size} - Average Time vs Threads (até 10 threads)')
    plt.xlabel('Threads')
    plt.ylabel('Average Time (s)')
    plt.grid(True)

    plt.subplot(3, 1, 2)
    plt.plot(threads, speedup, marker='o', color='green')
    plt.title(f'Matrix {size}x{size} - Speedup vs Threads (até 10 threads)')
    plt.xlabel('Threads')
    plt.ylabel('Speedup')
    plt.grid(True)

    plt.tight_layout()
    plt.show()

# Gerar gráficos para cada tamanho de matriz
for size, info in dados.items():
    plotar_graficos(size, info)
