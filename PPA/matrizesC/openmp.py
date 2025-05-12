import matplotlib.pyplot as plt
import numpy as np

# Data for normal threads and OpenMP implementations
implementations = ['Normal Threads', 'Static', 'Dynamic', 'Guided', 'Runtime', 'Auto']
speedups = [6.09, 7.52, 7.16, 7.09, 7.14, 7.61]

# Create figure
plt.figure(figsize=(8, 5))

# Distinct color for each bar
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b']

# Plot speedups
bars = plt.bar(implementations, speedups, color=colors)
plt.title('Speedup Comparison (12 Threads)')
plt.ylabel('Speedup')
plt.ylim(0, max(speedups) * 1.1)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Add value labels on top of bars
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height + 0.1,
            f'{height:.2f}', ha='center', fontsize=10)

# Rotate x-axis labels for better readability
plt.xticks(rotation=30)

plt.tight_layout()
plt.show()