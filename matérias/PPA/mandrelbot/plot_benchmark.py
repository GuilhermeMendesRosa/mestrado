#!/usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os

# Configurar estilo dos gráficos
plt.style.use('seaborn-v0_8')
sns.set_palette("husl")

def load_data():
    """Carrega os dados dos CSVs de benchmark"""
    try:
        mpi_data = pd.read_csv('benchmark_mpi_speedup.csv')
        hybrid_data = pd.read_csv('benchmark_mpi_openmp_speedup.csv')
        return mpi_data, hybrid_data
    except FileNotFoundError as e:
        print(f"Erro: Arquivo não encontrado - {e}")
        print("Execute o benchmark primeiro!")
        return None, None

def plot_speedup_comparison(mpi_data, hybrid_data):
    """Gráfico comparando speedups MPI vs MPI+OpenMP"""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

    # MPI apenas
    ax1.plot(mpi_data['processes'], mpi_data['speedup'], 'o-', linewidth=2, markersize=8, label='MPI')
    ax1.plot(mpi_data['processes'], mpi_data['processes'], '--', alpha=0.7, label='Speedup Ideal')
    ax1.set_xlabel('Número de Processos MPI')
    ax1.set_ylabel('Speedup')
    ax1.set_title('Speedup - MPI Apenas')
    ax1.legend()
    ax1.grid(True, alpha=0.3)

    # MPI + OpenMP (melhor configuração por número de processos)
    best_hybrid = hybrid_data.loc[hybrid_data.groupby('processes')['speedup'].idxmax()]
    total_cores = best_hybrid['processes'] * best_hybrid['threads']

    ax2.plot(total_cores, best_hybrid['speedup'], 's-', linewidth=2, markersize=8, label='MPI+OpenMP (melhor)', color='orange')
    ax2.plot(mpi_data['processes'], mpi_data['speedup'], 'o-', linewidth=2, markersize=8, label='MPI apenas', alpha=0.7)
    ax2.plot(total_cores, total_cores, '--', alpha=0.7, label='Speedup Ideal')
    ax2.set_xlabel('Total de Cores Utilizados')
    ax2.set_ylabel('Speedup')
    ax2.set_title('Comparação de Speedup')
    ax2.legend()
    ax2.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig('speedup_comparison.png', dpi=300, bbox_inches='tight')
    plt.show()

def plot_efficiency_analysis(mpi_data, hybrid_data):
    """Gráfico de eficiência"""
    fig, ax = plt.subplots(figsize=(12, 8))

    # MPI apenas
    ax.plot(mpi_data['processes'], mpi_data['efficiency'], 'o-', linewidth=2, markersize=8, label='MPI apenas')

    # MPI + OpenMP - diferentes configurações
    for threads in sorted(hybrid_data['threads'].unique()):
        subset = hybrid_data[hybrid_data['threads'] == threads]
        total_cores = subset['processes'] * subset['threads']
        ax.plot(total_cores, subset['efficiency'], 's-', linewidth=2, markersize=6, 
                label=f'MPI+OpenMP ({threads} threads/proc)', alpha=0.8)

    ax.axhline(y=1.0, color='red', linestyle='--', alpha=0.7, label='Eficiência Ideal (100%)')
    ax.set_xlabel('Total de Cores Utilizados')
    ax.set_ylabel('Eficiência')
    ax.set_title('Análise de Eficiência')
    ax.legend()
    ax.grid(True, alpha=0.3)
    ax.set_ylim(0, 1.1)

    plt.tight_layout()
    plt.savefig('efficiency_analysis.png', dpi=300, bbox_inches='tight')
    plt.show()

def plot_execution_times(mpi_data, hybrid_data):
    """Gráfico de tempos de execução com barras de erro"""
    fig, ax = plt.subplots(figsize=(12, 8))

    # Preparar dados para o gráfico
    x_pos = np.arange(len(mpi_data))
    width = 0.35

    # MPI apenas
    ax.bar(x_pos - width/2, mpi_data['avg_time_seconds'], width, 
           yerr=mpi_data['std_dev_seconds'], capsize=5, 
           label='MPI apenas', alpha=0.8)

    # MPI + OpenMP (melhor configuração por número de processos)
    best_hybrid = hybrid_data.loc[hybrid_data.groupby('processes')['avg_time_seconds'].idxmin()]

    if len(best_hybrid) == len(mpi_data):
        ax.bar(x_pos + width/2, best_hybrid['avg_time_seconds'], width,
               yerr=best_hybrid['std_dev_seconds'], capsize=5,
               label='MPI+OpenMP (melhor)', alpha=0.8)

    ax.set_xlabel('Configuração')
    ax.set_ylabel('Tempo de Execução (segundos)')
    ax.set_title('Tempos de Execução com Desvio Padrão')
    ax.set_xticks(x_pos)
    ax.set_xticklabels([f'{p} proc' for p in mpi_data['processes']])
    ax.legend()
    ax.grid(True, alpha=0.3, axis='y')

    plt.tight_layout()
    plt.savefig('execution_times.png', dpi=300, bbox_inches='tight')
    plt.show()

def plot_heatmap_hybrid(hybrid_data):
    """Heatmap do speedup para diferentes configurações MPI+OpenMP"""
    # Criar matriz pivot
    pivot_speedup = hybrid_data.pivot(index='threads', columns='processes', values='speedup')
    pivot_efficiency = hybrid_data.pivot(index='threads', columns='processes', values='efficiency')

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

    # Heatmap de speedup
    sns.heatmap(pivot_speedup, annot=True, fmt='.2f', cmap='YlOrRd', ax=ax1)
    ax1.set_title('Speedup - MPI+OpenMP')
    ax1.set_xlabel('Processos MPI')
    ax1.set_ylabel('Threads OpenMP por Processo')

    # Heatmap de eficiência
    sns.heatmap(pivot_efficiency, annot=True, fmt='.2f', cmap='RdYlGn', ax=ax2, vmin=0, vmax=1)
    ax2.set_title('Eficiência - MPI+OpenMP')
    ax2.set_xlabel('Processos MPI')
    ax2.set_ylabel('Threads OpenMP por Processo')

    plt.tight_layout()
    plt.savefig('heatmap_hybrid.png', dpi=300, bbox_inches='tight')
    plt.show()

def generate_summary_table(mpi_data, hybrid_data):
    """Gera tabela resumo dos melhores resultados"""
    print("\n" + "="*60)
    print("RESUMO DOS MELHORES RESULTADOS")
    print("="*60)

    # Melhor MPI
    best_mpi = mpi_data.loc[mpi_data['speedup'].idxmax()]
    print(f"\nMPI APENAS:")
    print(f"  Melhor speedup: {best_mpi['speedup']:.2f}x com {best_mpi['processes']} processos")
    print(f"  Tempo: {best_mpi['avg_time_seconds']:.3f}s (±{best_mpi['std_dev_seconds']:.3f}s)")
    print(f"  Eficiência: {best_mpi['efficiency']:.2f}")

    # Melhor híbrido
    best_hybrid = hybrid_data.loc[hybrid_data['speedup'].idxmax()]
    total_cores = best_hybrid['processes'] * best_hybrid['threads']
    print(f"\nMPI + OPENMP:")
    print(f"  Melhor speedup: {best_hybrid['speedup']:.2f}x com {best_hybrid['processes']} proc × {best_hybrid['threads']} threads")
    print(f"  Total de cores: {total_cores}")
    print(f"  Tempo: {best_hybrid['avg_time_seconds']:.3f}s (±{best_hybrid['std_dev_seconds']:.3f}s)")
    print(f"  Eficiência: {best_hybrid['efficiency']:.2f}")

    # Comparação
    improvement = (best_hybrid['speedup'] / best_mpi['speedup'] - 1) * 100
    print(f"\nCOMPARAÇÃO:")
    print(f"  Melhoria do híbrido sobre MPI: {improvement:+.1f}%")

    # Salvar resumo em arquivo
    with open('benchmark_summary.txt', 'w') as f:
        f.write("RESUMO DOS RESULTADOS DO BENCHMARK\n")
        f.write("="*40 + "\n\n")
        f.write(f"MPI APENAS:\n")
        f.write(f"  Speedup: {best_mpi['speedup']:.2f}x\n")
        f.write(f"  Processos: {best_mpi['processes']}\n")
        f.write(f"  Tempo: {best_mpi['avg_time_seconds']:.3f}s\n")
        f.write(f"  Eficiência: {best_mpi['efficiency']:.2f}\n\n")
        f.write(f"MPI + OPENMP:\n")
        f.write(f"  Speedup: {best_hybrid['speedup']:.2f}x\n")
        f.write(f"  Configuração: {best_hybrid['processes']} proc × {best_hybrid['threads']} threads\n")
        f.write(f"  Tempo: {best_hybrid['avg_time_seconds']:.3f}s\n")
        f.write(f"  Eficiência: {best_hybrid['efficiency']:.2f}\n\n")
        f.write(f"Melhoria: {improvement:+.1f}%\n")

def main():
    print("Carregando dados dos benchmarks...")
    mpi_data, hybrid_data = load_data()

    if mpi_data is None or hybrid_data is None:
        return

    print(f"Dados carregados:")
    print(f"  MPI: {len(mpi_data)} configurações")
    print(f"  MPI+OpenMP: {len(hybrid_data)} configurações")

    print("\nGerando gráficos...")

    # Gerar todos os gráficos
    plot_speedup_comparison(mpi_data, hybrid_data)
    plot_efficiency_analysis(mpi_data, hybrid_data)
    plot_execution_times(mpi_data, hybrid_data)
    plot_heatmap_hybrid(hybrid_data)

    # Gerar resumo
    generate_summary_table(mpi_data, hybrid_data)

    print("\nGráficos salvos:")
    print("  - speedup_comparison.png")
    print("  - efficiency_analysis.png") 
    print("  - execution_times.png")
    print("  - heatmap_hybrid.png")
    print("  - benchmark_summary.txt")

if __name__ == "__main__":
    main()
