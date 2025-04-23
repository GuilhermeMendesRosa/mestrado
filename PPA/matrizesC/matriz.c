#include <stdio.h>
#include <stdlib.h>
#include "matriz.h"
#include <pthread.h>

matriz_t *matriz_criar(int linhas, int colunas)
{
   int i;
   matriz_t *retorno = NULL;
   // malloc usada para alocacao de memoria
   retorno = (matriz_t *) malloc(sizeof(matriz_t));
   retorno->linhas = linhas;
   retorno->colunas = colunas;

   double * mat = (double *) malloc(linhas * colunas * 
      sizeof(double));

   retorno->dados = (double **) malloc(sizeof(double *)* linhas);
      for (i = 0; i < linhas; i++) {
         retorno->dados[i] = &mat[i * colunas];
      }

   return retorno;
}

void matriz_destruir(matriz_t *m) 
{
    free(&m->dados[0][0]); 
    free(m->dados); // free(&m->dados[0])
    free(m);
    
    return;
}

void matriz_preencher_rand(matriz_t *m)
{
   int i, j;
   for (i = 0; i < m->linhas; i++) {
      for (j = 0; j < m->colunas; j++) {
         m->dados[i][j] = random();
      }
   }
}

void matriz_preencher(matriz_t *m, double valor)
{
   int i, j;
   for (i = 0; i < m->linhas; i++) {
      for (j = 0; j < m->colunas; j++) {
         m->dados[i][j] = valor;
      }
   }
}

void *matriz_multiplicar_paralelo(void *args) {
   thread_params *parametros = (thread_params *) args;
   
   // Começa da linha correspondente ao ID da thread
   int i = parametros->tid;
   
   // Pula num_threads linhas a cada iteração
   while (i < parametros->A->linhas) {
       // Para cada coluna da matriz resultante
       for (int j = 0; j < parametros->B->colunas; j++) {
           double soma = 0.0;
           // Faz o produto escalar da linha i de A com a coluna j de B
           for (int k = 0; k < parametros->A->colunas; k++) {
               soma += parametros->A->dados[i][k] * parametros->B->dados[k][j];
           }
           parametros->C->dados[i][j] = soma;
       }
       i += parametros->num_threads;
   }
   
   pthread_exit(NULL);
}

matriz_t *matriz_multiplicar(matriz_t *A, matriz_t *B)
{
   int i, j, k;
   double sum;
   matriz_t *m = matriz_criar(A->linhas, B->colunas);
   for (i = 0; i < m->linhas; i++) {
      for (j = 0; j < m->colunas; j++) {
         sum = 0.0;
         for (k = 0; k < m->colunas; k++) {
            sum += A->dados[i][k] * B->dados[k][j];
         }
         m->dados[i][j] = sum;
      }
   }
    return m;
}

void matriz_imprimir(matriz_t *m)
{
   
   int i, j;
   for (i = 0; i < m->linhas; i++) {
      for (j = 0; j < m->colunas; j++) {
         printf("%.17f ", m->dados[i][j]);
      }
      printf("\n");
   }
}

void *matriz_somar_paralelo(void *args)
{
	thread_params *parametros = (thread_params *) args;
	printf("sou a thread %d!!!!\n", parametros->tid);
//	parametros->num_threads
	int j;
	int i = parametros->tid; //certo
	while (i < parametros->A->linhas) {
	      for (j = 0; j < parametros->A->colunas; j++) {
        	 parametros->C->dados[i][j] = parametros->A->dados[i][j] + parametros->B->dados[i][j];
	   }
	      i += parametros->num_threads;
	}

	pthread_exit(NULL);
}

matriz_t *matriz_somar(matriz_t *A, matriz_t *B)
{
   int i, j;
   matriz_t *retorno = matriz_criar(A->linhas, A->colunas);
   for (i = 0; i < A->linhas; i++) {
      for (j = 0; j < A->colunas; j++) {
         retorno->dados[i][j] = A->dados[i][j] + B->dados[i][j];
   }
}
    return retorno;
}

