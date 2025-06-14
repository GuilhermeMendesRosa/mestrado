#ifndef __MATRIZ_H
#define __MATRIZ_H

#define random() ((rand() ^ rand()) / (RAND_MAX + 1.0))
typedef struct {
      double **dados;
      int linhas;
      int colunas;
} matriz_t;

typedef struct {
	int tid;
	int num_threads; //numero de threads em execução
	matriz_t *A;
	matriz_t *B;
	matriz_t *C;
} thread_params;


matriz_t *matriz_criar(int linhas, int colunas);

void matriz_destruir(matriz_t *m);

void matriz_preencher_rand(matriz_t *m);

void matriz_preencher(matriz_t *m, double valor);

void *matriz_multiplicar_paralelo(void *args);

matriz_t *matriz_multiplicar(matriz_t *A, matriz_t *B);

matriz_t *matriz_multiplicar_static(matriz_t *A, matriz_t *B);

matriz_t *matriz_multiplicar_dynamic(matriz_t *A, matriz_t *B);

matriz_t *matriz_multiplicar_guided(matriz_t *A, matriz_t *B);

matriz_t *matriz_multiplicar_runtime(matriz_t *A, matriz_t *B);

matriz_t *matriz_multiplicar_auto(matriz_t *A, matriz_t *B);

void *matriz_somar_paralelo(void *args);

matriz_t *matriz_somar(matriz_t *A, matriz_t *B);

void matriz_imprimir(matriz_t *m);

#endif 
