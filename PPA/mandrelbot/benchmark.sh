#!/bin/bash

# Configurações do benchmark
MAX_ROW=1000
MAX_COLUMN=1000
MAX_N=100
RUNS=5  # Número de execuções por configuração para calcular média

# Detectar número de cores disponíveis
AVAILABLE_CORES=$(nproc)
echo "Cores disponíveis: $AVAILABLE_CORES"
echo "Execuções por configuração: $RUNS"

# Ajustar configurações baseado nos cores disponíveis
if [ $AVAILABLE_CORES -ge 8 ]; then
    MPI_PROCESSES=(1 2 4 8)
    OMP_THREADS=(1 2 4 8)
elif [ $AVAILABLE_CORES -ge 4 ]; then
    MPI_PROCESSES=(1 2 4)
    OMP_THREADS=(1 2 4)
else
    MPI_PROCESSES=(1 2)
    OMP_THREADS=(1 2)
fi

echo "Configurações de teste:"
echo "MPI processes: ${MPI_PROCESSES[@]}"
echo "OpenMP threads: ${OMP_THREADS[@]}"

echo "Compilando os programas..."
mpicc -o mandelbrot_mpi mandelbrot_mpi.c -lm
mpicc -fopenmp -o mandelbrot_mpi_openmp mandelbrot_mpi_openmp.c -lm

# Função para executar e medir tempo
run_benchmark() {
    local program=$1
    local processes=$2
    local threads=$3
    local output_file=$4

    echo "Executando $program com $processes processos e $threads threads ($RUNS execuções)..."

    total_time=0
    times=()

    for run in $(seq 1 $RUNS); do
        if [ "$threads" -gt 1 ]; then
            export OMP_NUM_THREADS=$threads
        fi

        # Usar --oversubscribe se necessário
        local mpi_options=""
        if [ $processes -gt $AVAILABLE_CORES ]; then
            mpi_options="--oversubscribe"
        fi

        start_time=$(date +%s.%N)
        echo "$MAX_ROW $MAX_COLUMN $MAX_N" | mpirun $mpi_options -np $processes ./$program > /dev/null 2>/dev/null
        end_time=$(date +%s.%N)

        runtime=$(echo "$end_time - $start_time" | bc -l)
        times+=($runtime)
        total_time=$(echo "$total_time + $runtime" | bc -l)

        echo "  Run $run: ${runtime}s"
    done

    avg_time=$(echo "scale=6; $total_time / $RUNS" | bc -l)

    # Calcular desvio padrão
    sum_sq_diff=0
    for time in "${times[@]}"; do
        diff=$(echo "$time - $avg_time" | bc -l)
        sq_diff=$(echo "$diff * $diff" | bc -l)
        sum_sq_diff=$(echo "$sum_sq_diff + $sq_diff" | bc -l)
    done
    variance=$(echo "scale=6; $sum_sq_diff / $RUNS" | bc -l)
    std_dev=$(echo "scale=6; sqrt($variance)" | bc -l)

    echo "  Tempo médio: ${avg_time}s (±${std_dev}s)"

    # Salvar com desvio padrão
    echo "$processes,$threads,$avg_time,$std_dev" >> $output_file
}

# Criar arquivos CSV com cabeçalhos incluindo desvio padrão
echo "processes,threads,avg_time_seconds,std_dev_seconds" > benchmark_mpi.csv
echo "processes,threads,avg_time_seconds,std_dev_seconds" > benchmark_mpi_openmp.csv

echo ""
echo "=== Benchmark MPI apenas ==="
for processes in "${MPI_PROCESSES[@]}"; do
    run_benchmark "mandelbrot_mpi" $processes 1 "benchmark_mpi.csv"
done

echo ""
echo "=== Benchmark MPI + OpenMP ==="
for processes in "${MPI_PROCESSES[@]}"; do
    for threads in "${OMP_THREADS[@]}"; do
        run_benchmark "mandelbrot_mpi_openmp" $processes $threads "benchmark_mpi_openmp.csv"
    done
done

echo ""
echo "Benchmark concluído!"
echo "Resultados salvos em:"
echo "- benchmark_mpi.csv"
echo "- benchmark_mpi_openmp.csv"

# Calcular speedups
echo "Calculando speedups..."

# Para MPI apenas
echo "processes,threads,avg_time_seconds,std_dev_seconds,speedup,efficiency" > benchmark_mpi_speedup.csv
baseline_mpi=$(awk -F',' 'NR==2 {print $3}' benchmark_mpi.csv)

tail -n +2 benchmark_mpi.csv | while IFS=',' read -r processes threads time std_dev; do
    speedup=$(echo "scale=4; $baseline_mpi / $time" | bc -l)
    efficiency=$(echo "scale=4; $speedup / $processes" | bc -l)
    echo "$processes,$threads,$time,$std_dev,$speedup,$efficiency" >> benchmark_mpi_speedup.csv
done

# Para MPI + OpenMP
echo "processes,threads,avg_time_seconds,std_dev_seconds,speedup,efficiency" > benchmark_mpi_openmp_speedup.csv
baseline_hybrid=$(awk -F',' 'NR==2 {print $3}' benchmark_mpi_openmp.csv)

tail -n +2 benchmark_mpi_openmp.csv | while IFS=',' read -r processes threads time std_dev; do
    total_cores=$(echo "$processes * $threads" | bc)
    speedup=$(echo "scale=4; $baseline_hybrid / $time" | bc -l)
    efficiency=$(echo "scale=4; $speedup / $total_cores" | bc -l)
    echo "$processes,$threads,$time,$std_dev,$speedup,$efficiency" >> benchmark_mpi_openmp_speedup.csv
done

echo "Speedups calculados e salvos em:"
echo "- benchmark_mpi_speedup.csv"
echo "- benchmark_mpi_openmp_speedup.csv"

# Mostrar resumo dos resultados
echo ""
echo "=== RESUMO DOS RESULTADOS ==="
echo "MPI apenas - Melhores speedups:"
echo "Processes,Threads,Time(s),StdDev,Speedup,Efficiency"
sort -t',' -k5 -nr benchmark_mpi_speedup.csv | head -4

echo ""
echo "MPI + OpenMP - Melhores speedups:"
echo "Processes,Threads,Time(s),StdDev,Speedup,Efficiency"
sort -t',' -k5 -nr benchmark_mpi_openmp_speedup.csv | head -4

echo ""
echo "Total de configurações testadas:"
echo "MPI: $(( ${#MPI_PROCESSES[@]} )) configurações"
echo "MPI+OpenMP: $(( ${#MPI_PROCESSES[@]} * ${#OMP_THREADS[@]} )) configurações"
echo "Total de execuções: $(( (${#MPI_PROCESSES[@]} + ${#MPI_PROCESSES[@]} * ${#OMP_THREADS[@]}) * $RUNS ))"
