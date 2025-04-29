#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <pthread.h>
#include "matriz.h"

// Function to calculate elapsed time in seconds
double elapsed_time_sec(struct timespec start, struct timespec end) {
    return (end.tv_sec - start.tv_sec) + (end.tv_nsec - start.tv_nsec) / 1000000000.0;
}

// Function to run tests for a specific matrix size
void run_tests_for_size(int size) {
    matriz_t *A = NULL;
    matriz_t *B = NULL;
    matriz_t *C = NULL;
    struct timespec start_time, end_time;
    const int NUM_EXECUTIONS = 10;
    const int MIN_THREADS = 1;
    const int MAX_THREADS = 22;
    double sequential_time = 0.0;  // Store sequential time for speedup calculation
    
    printf("\n=== Matrix size: %d x %d ===\n", size, size);
    printf("Running %d executions for each thread count (%d to %d)...\n", 
           NUM_EXECUTIONS, MIN_THREADS, MAX_THREADS);
    
    // Create and fill matrices
    A = matriz_criar(size, size);
    B = matriz_criar(size, size);
    
    srand(time(NULL));
    matriz_preencher_rand(A);
    matriz_preencher_rand(B);
    
    printf("\nSize,Threads,Average Time (seconds),Speedup,Efficiency\n");
    
    // Loop through different thread counts
    for (int num_threads = MIN_THREADS; num_threads <= MAX_THREADS; num_threads++) {
        double total_time = 0.0;
        
        // Run multiple executions for each thread count
        for (int run = 0; run < NUM_EXECUTIONS; run++) {
            if (num_threads == 1) {
                // Sequential multiplication
                clock_gettime(CLOCK_MONOTONIC, &start_time);
                C = matriz_multiplicar(A, B);
                clock_gettime(CLOCK_MONOTONIC, &end_time);
                
                total_time += elapsed_time_sec(start_time, end_time);
                
                matriz_destruir(C);
            } else {
                // Parallel multiplication
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
        }
        
        // Calculate average execution time for this thread count
        double avg_time = total_time / NUM_EXECUTIONS;
        
        // Store sequential time for speedup calculation
        if (num_threads == 1) {
            sequential_time = avg_time;
            printf("%d,%d,%.6f,1.00,100.00%%\n", size, num_threads, avg_time);
        } else {
            // Calculate speedup and efficiency
            double speedup = sequential_time / avg_time;
            double efficiency = (speedup / num_threads) * 100.0;
            printf("%d,%d,%.6f,%.2f,%.2f%%\n", size, num_threads, avg_time, speedup, efficiency);
        }
    }
    
    // Cleanup
    matriz_destruir(A);
    matriz_destruir(B);
}

int main() {
    const int sizes[] = {250, 500, 1000};
    const int num_sizes = sizeof(sizes) / sizeof(sizes[0]);
    
    printf("Running tests for multiple matrix sizes...\n");
    
    for (int i = 0; i < num_sizes; i++) {
        run_tests_for_size(sizes[i]);
    }
    
    return EXIT_SUCCESS;
}