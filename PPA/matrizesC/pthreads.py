import matplotlib.pyplot as plt
import numpy as np

# Dados fornecidos
threads = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16])
speedup = np.array([1.00,1.49,2.29,3.61,4.70,5.16,4.81,4.94,5.22,5.54,5.85,6.09,5.36,5.07,5.29,5.20])

fig, ax = plt.subplots(figsize=(10,6))

ax.set_xlabel('Threads')
ax.set_ylabel('Speedup', color='tab:blue')
ax.plot(threads, speedup, marker='o', color='tab:blue', label='Speedup')
ax.tick_params(axis='y', labelcolor='tab:blue')
ax.set_xticks(threads)

fig.suptitle('Speedup por Número de Threads')
fig.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()
