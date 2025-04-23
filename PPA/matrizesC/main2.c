#include <stdio.h>
#include <stdlib.h>
#include "matriz.h"
#include <pthread.h>

int main(int argc, char **argv)
{
    int linhas = 3;
    int colunas = 3;
    int num_threads = 0;
    matriz_t *A = NULL;
    matriz_t *B = NULL;
    matriz_t *C = NULL;

    if (argc != 2) {
        printf("Uso: %s <NUM_THREADS>\n", argv[0]);
        exit(EXIT_FAILURE);
    }
    
    num_threads = atoi(argv[1]);

    // Criar as matrizes
    A = matriz_criar(linhas, colunas);
    B = matriz_criar(linhas, colunas);

    // Preencher matriz A com valores específicos
    int matriz_a[3][3] = {
        {7, 4, 8},
        {5, 7, 10},
        {3, 7, 8}
    };

    // Preencher matriz B com valores específicos
    int matriz_b[3][3] = {
        {5, 4, 8},
        {8, 3, 6},
        {5, 2, 8}
    };

    // Preencher as matrizes A e B com os valores definidos
    for(int i = 0; i < linhas; i++) {
        for(int j = 0; j < colunas; j++) {
            A->dados[i][j] = matriz_a[i][j];
            B->dados[i][j] = matriz_b[i][j];
        }
    }

    printf("Matriz A:\n");
    matriz_imprimir(A);
    printf("\nMatriz B:\n");
    matriz_imprimir(B);

    // Preparar para multiplicação paralela
    thread_params *parametros = NULL;
    pthread_t *threads = NULL;
    parametros = (thread_params*) malloc(sizeof(thread_params) * num_threads);
    threads = (pthread_t*) malloc(sizeof(pthread_t) * num_threads);

    C = matriz_criar(linhas, colunas);

    // Criar threads para multiplicação paralela
    for (int i = 0; i < num_threads; i++) {
        parametros[i].tid = i;
        parametros[i].A = A;
        parametros[i].B = B;
        parametros[i].C = C;
        parametros[i].num_threads = num_threads;
        pthread_create(&threads[i], NULL, matriz_multiplicar_paralelo, &parametros[i]);
    }

    // Aguardar todas as threads terminarem
    for (int i = 0; i < num_threads; i++) {
        pthread_join(threads[i], NULL);
    }

    printf("\nResultado da multiplicação paralela (Matriz C):\n");
    matriz_imprimir(C);

    // Liberar memória
    matriz_destruir(A);
    matriz_destruir(B);
    matriz_destruir(C);
    free(parametros);
    free(threads);

    return EXIT_SUCCESS;
}