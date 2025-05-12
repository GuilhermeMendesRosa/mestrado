import matplotlib.pyplot as plt
import numpy as np

# Dados fornecidos
threads = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16])
speedup = np.array([1.00,1.49,2.29,3.61,4.70,5.16,4.81,4.94,5.22,5.54,5.85,6.09,5.36,5.07,5.29,5.20])
efficiency = np.array([100.00,74.74,76.29,90.20,93.97,86.07,68.66,61.71,58.05,55.35,53.17,50.71,41.22,36.21,35.26,32.52])

fig, ax1 = plt.subplots(figsize=(10,6))

color = 'tab:blue'
ax1.set_xlabel('Threads')
ax1.set_ylabel('Speedup', color=color)
ax1.plot(threads, speedup, marker='o', color=color, label='Speedup')
ax1.tick_params(axis='y', labelcolor=color)
ax1.set_xticks(threads)

ax2 = ax1.twinx()  # Instancia um segundo eixo y
color = 'tab:red'
ax2.set_ylabel('Eficiência (%)', color=color)
ax2.plot(threads, efficiency, marker='s', color=color, label='Eficiência (%)')
ax2.tick_params(axis='y', labelcolor=color)

fig.suptitle('Comparação de Speedup e Eficiência por Número de Threads')
fig.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()