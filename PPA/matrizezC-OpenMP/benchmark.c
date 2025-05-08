#include <stdio.h>
#include <stdlib.h>
#include <omp.h>
#include "matriz.h"

int main() {
    int size = 1000;
    double start_time, end_time;
    
    printf("Inicializando matrizes %dx%d...\n", size, size);
    
    // Criar matrizes
    matriz_t *A = matriz_criar(size, size);
    matriz_t *B = matriz_criar(size, size);
    matriz_t *C = NULL;
    
    // Preencher com valores aleatórios
    matriz_preencher_rand(A);
    matriz_preencher_rand(B);
    
    printf("Iniciando multiplicação...\n");
    
    // Medir tempo
    start_time = omp_get_wtime();
    
    // Realizar multiplicação
    C = matriz_multiplicar(A, B);
    
    // Finalizar medição
    end_time = omp_get_wtime();
    
    printf("Multiplicação concluída!\n");
    printf("Tempo de execução: %.4f segundos\n", end_time - start_time);
    
    // Liberar memória
    matriz_destruir(A);
    matriz_destruir(B);
    matriz_destruir(C);
    
    return 0;
}