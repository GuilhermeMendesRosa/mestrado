#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <pthread.h>
#include "matriz.h"

// Function to calculate elapsed time in seconds
double elapsed_time_sec(struct timespec start, struct timespec end) {
    return (end.tv_sec - start.tv_sec) + (end.tv_nsec - start.tv_nsec) / 1000000000.0;
}

int main(int argc, char **argv) {
    int size = 0;
    int num_threads = 0;
    matriz_t *A = NULL;
    matriz_t *B = NULL;
    matriz_t *C_seq = NULL;   // Result from sequential multiplication
    matriz_t *C_par = NULL;   // Result from parallel multiplication
    struct timespec start_time, end_time;
    double seq_time, par_time;
    
    if (argc != 3) {
        printf("Usage: %s <MATRIX_SIZE> <NUM_THREADS>\n", argv[0]);
        exit(EXIT_FAILURE);
    }
    
    size = atoi(argv[1]);
    num_threads = atoi(argv[2]);
    
    printf("Matrix size: %d x %d\n", size, size);
    printf("Number of threads: %d\n", num_threads);
    
    // Create and fill matrices
    A = matriz_criar(size, size);
    B = matriz_criar(size, size);
    
    srand(time(NULL));
    matriz_preencher_rand(A);
    matriz_preencher_rand(B);
    
    // Print small matrices
    if (size <= 10) {
        printf("\nMatrix A:\n");
        matriz_imprimir(A);
        printf("\nMatrix B:\n");
        matriz_imprimir(B);
    }
    
    // Sequential multiplication
    printf("\nPerforming sequential multiplication...\n");
    clock_gettime(CLOCK_MONOTONIC, &start_time);
    C_seq = matriz_multiplicar(A, B);
    clock_gettime(CLOCK_MONOTONIC, &end_time);
    seq_time = elapsed_time_sec(start_time, end_time);
    printf("Sequential multiplication completed in %.6f seconds\n", seq_time);
    
    // Parallel multiplication
    printf("\nPerforming parallel multiplication with %d threads...\n", num_threads);
    C_par = matriz_criar(size, size);
    
    thread_params *parametros = (thread_params*) malloc(sizeof(thread_params) * num_threads);
    pthread_t *threads = (pthread_t*) malloc(sizeof(pthread_t) * num_threads);
    
    clock_gettime(CLOCK_MONOTONIC, &start_time);
    
    for (int i = 0; i < num_threads; i++) {
        parametros[i].tid = i;
        parametros[i].A = A;
        parametros[i].B = B;
        parametros[i].C = C_par;
        parametros[i].num_threads = num_threads;
        pthread_create(&threads[i], NULL, matriz_multiplicar_paralelo, &parametros[i]);
    }
    
    for (int i = 0; i < num_threads; i++) {
        pthread_join(threads[i], NULL);
    }
    
    clock_gettime(CLOCK_MONOTONIC, &end_time);
    par_time = elapsed_time_sec(start_time, end_time);
    printf("Parallel multiplication completed in %.6f seconds\n", par_time);
    
    // Print results for small matrices
    if (size <= 10) {
        printf("\nSequential multiplication result:\n");
        matriz_imprimir(C_seq);
        printf("\nParallel multiplication result:\n");
        matriz_imprimir(C_par);
    }
    
    // Performance comparison
    double speedup = seq_time / par_time;
    printf("\nPerformance comparison:\n");
    printf("Sequential time: %.6f seconds\n", seq_time);
    printf("Parallel time:   %.6f seconds\n", par_time);
    printf("Speedup:         %.2fx\n", speedup);
    printf("Efficiency:      %.2f%%\n", (speedup / num_threads) * 100);
    
    // Verify results
    int correct = 1;
    for (int i = 0; i < size && correct; i++) {
        for (int j = 0; j < size; j++) {
            if (C_seq->dados[i][j] != C_par->dados[i][j]) {
                correct = 0;
                printf("ERROR: Results differ at [%d][%d]\n", i, j);
                break;
            }
        }
    }
    
    if (correct) {
        printf("VERIFICATION: Results from both methods match.\n");
    }
    
    // Cleanup
    matriz_destruir(A);
    matriz_destruir(B);
    matriz_destruir(C_seq);
    matriz_destruir(C_par);
    free(parametros);
    free(threads);
    
    return EXIT_SUCCESS;
}