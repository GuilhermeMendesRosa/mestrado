#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <pthread.h>
#include <omp.h>
#include "matriz.h"

// Enum para identificar os tipos de implementação
typedef enum {
    SEQUENTIAL,
    PTHREAD,
    OMP_STATIC,
    OMP_DYNAMIC,
    OMP_GUIDED,
    OMP_RUNTIME,
    OMP_AUTO
} implementation_type;

// Function to calculate elapsed time in seconds
double elapsed_time_sec(struct timespec start, struct timespec end) {
    return (end.tv_sec - start.tv_sec) + (end.tv_nsec - start.tv_nsec) / 1000000000.0;
}

// Function to run tests for a specific matrix size
void run_tests_for_size() {
    int size = 500;
    matriz_t *A = NULL;
    matriz_t *B = NULL;
    matriz_t *C = NULL;
    struct timespec start_time, end_time;
    const int NUM_EXECUTIONS = 30;
    const int MIN_THREADS = 1;
    const int MAX_THREADS = 16;
    double sequential_time = 0.0;  // Store sequential time for speedup calculation
    
    printf("\n=== Matrix size: %d x %d ===\n", size, size);
    
    // Create and fill matrices
    A = matriz_criar(size, size);
    B = matriz_criar(size, size);
    
    srand(time(NULL));
    matriz_preencher_rand(A);
    matriz_preencher_rand(B);
    
    printf("\nImplementation,Threads,Average Time (seconds),Speedup,Efficiency\n");
    
    // Test sequential implementation first
    double total_time = 0.0;
    for (int run = 0; run < NUM_EXECUTIONS; run++) {
        clock_gettime(CLOCK_MONOTONIC, &start_time);
        C = matriz_multiplicar(A, B);
        clock_gettime(CLOCK_MONOTONIC, &end_time);
        
        total_time += elapsed_time_sec(start_time, end_time);
        matriz_destruir(C);
    }
    
    sequential_time = total_time / NUM_EXECUTIONS;
    printf("Sequential,1,%.6f,1.00,100.00%%\n", sequential_time);
    
    // Loop through different thread counts for pthread implementation
    printf("\n--- Pthread Implementation ---\n");
    printf("Threads,Average Time (seconds),Speedup,Efficiency\n");
    
    for (int num_threads = 1; num_threads <= MAX_THREADS; num_threads++) {
        total_time = 0.0;
        
        for (int run = 0; run < NUM_EXECUTIONS; run++) {
            C = matriz_criar(size, size);
            
            thread_params *parametros = (thread_params*) malloc(sizeof(thread_params) * num_threads);
            pthread_t *threads = (pthread_t*) malloc(sizeof(pthread_t) * num_threads);
            
            clock_gettime(CLOCK_MONOTONIC, &start_time);
            
            for (int i = 0; i < num_threads; i++) {
                parametros[i].tid = i;
                parametros[i].A = A;
                parametros[i].B = B;
                parametros[i].C = C;
                parametros[i].num_threads = num_threads;
                pthread_create(&threads[i], NULL, matriz_multiplicar_paralelo, &parametros[i]);
            }
            
            for (int i = 0; i < num_threads; i++) {
                pthread_join(threads[i], NULL);
            }
            
            clock_gettime(CLOCK_MONOTONIC, &end_time);
            
            total_time += elapsed_time_sec(start_time, end_time);
            
            matriz_destruir(C);
            free(parametros);
            free(threads);
        }
        
        double avg_time = total_time / NUM_EXECUTIONS;
        double speedup = sequential_time / avg_time;
        double efficiency = (speedup / num_threads) * 100.0;
        printf("%d,%.6f,%.2f,%.2f%%\n", num_threads, avg_time, speedup, efficiency);
    }
    
    // Test OpenMP implementations
    const char* omp_schedules[] = {"Static", "Dynamic", "Guided", "Runtime", "Auto"};
    
    printf("\n--- OpenMP Implementations ---\n");
    printf("Schedule,Average Time (seconds),Speedup,Efficiency\n");
    
    // Run each OpenMP schedule type
    for (int sched = 0; sched < 5; sched++) {
        total_time = 0.0;
        
        for (int run = 0; run < NUM_EXECUTIONS; run++) {
            clock_gettime(CLOCK_MONOTONIC, &start_time);
            
            switch (sched) {
                case 0: // Static
                    C = matriz_multiplicar_static(A, B);
                    break;
                case 1: // Dynamic
                    C = matriz_multiplicar_dynamic(A, B);
                    break;
                case 2: // Guided
                    C = matriz_multiplicar_guided(A, B);
                    break;
                case 3: // Runtime
                    C = matriz_multiplicar_runtime(A, B);
                    break;
                case 4: // Auto
                    C = matriz_multiplicar_auto(A, B);
                    break;
            }
            
            clock_gettime(CLOCK_MONOTONIC, &end_time);
            
            total_time += elapsed_time_sec(start_time, end_time);
            matriz_destruir(C);
        }
        
        double avg_time = total_time / NUM_EXECUTIONS;
        double speedup = sequential_time / avg_time;
        
        // Get the current number of threads in OpenMP
        int omp_num_threads;
        #pragma omp parallel
        {
            #pragma omp master
            omp_num_threads = omp_get_num_threads();
        }
        
        double efficiency = (speedup / omp_num_threads) * 100.0;
        printf("%s,%.6f,%.2f,%.2f%% (threads: %d)\n", 
               omp_schedules[sched], avg_time, speedup, efficiency, omp_num_threads);
    }
    
    // Cleanup
    matriz_destruir(A);
    matriz_destruir(B);
}

int main() {
    printf("Running benchmarks for matrix multiplication...\n");
    
    run_tests_for_size();
    
    return EXIT_SUCCESS;
}