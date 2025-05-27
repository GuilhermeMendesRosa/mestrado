#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <mpi.h>

int main(int argc, char** argv){
    int rank, size;
    int max_row, max_column, max_n;

    MPI_Init(&argc, &argv);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);

    // Processo master lê os parâmetros
    if(rank == 0) {
        scanf("%d", &max_row);
        scanf("%d", &max_column);
        scanf("%d", &max_n);
    }

    // Broadcast dos parâmetros para todos os processos
    MPI_Bcast(&max_row, 1, MPI_INT, 0, MPI_COMM_WORLD);
    MPI_Bcast(&max_column, 1, MPI_INT, 0, MPI_COMM_WORLD);
    MPI_Bcast(&max_n, 1, MPI_INT, 0, MPI_COMM_WORLD);

    // Calcular distribuição de linhas
    int rows_per_process = max_row / size;
    int remainder = max_row % size;
    int start_row = rank * rows_per_process + (rank < remainder ? rank : remainder);
    int end_row = start_row + rows_per_process + (rank < remainder ? 1 : 0);
    int local_rows = end_row - start_row;

    // Alocar matriz local
    char **local_mat = (char**)malloc(sizeof(char*) * local_rows);
    for (int i = 0; i < local_rows; i++)
        local_mat[i] = (char*)malloc(sizeof(char) * max_column);

    // Calcular o conjunto de Mandelbrot para as linhas locais
    for(int r = 0; r < local_rows; ++r){
        int global_r = start_row + r;
        for(int c = 0; c < max_column; ++c){
            float z_real = 0.0f, z_imag = 0.0f;
            int n = 0;
            float magnitude;

            while(1){
                magnitude = sqrt(z_real*z_real + z_imag*z_imag);
                if(magnitude >= 2 || ++n >= max_n) break;

                // z = z^2 + c
                float temp_real = z_real*z_real - z_imag*z_imag;
                float temp_imag = 2*z_real*z_imag;

                z_real = temp_real + ((float)c * 2 / max_column - 1.5f);
                z_imag = temp_imag + ((float)global_r * 2 / max_row - 1.0f);
            }
            local_mat[r][c] = (n == max_n ? '#' : '.');
        }
    }

    // Processo master coleta e imprime os resultados
    if(rank == 0) {
        // Alocar matriz completa
        char **mat = (char**)malloc(sizeof(char*) * max_row);
        for (int i = 0; i < max_row; i++)
            mat[i] = (char*)malloc(sizeof(char) * max_column);

        // Copiar dados locais do processo 0
        for(int r = 0; r < local_rows; ++r) {
            for(int c = 0; c < max_column; ++c) {
                mat[r][c] = local_mat[r][c];
            }
        }

        // Receber dados dos outros processos
        for(int proc = 1; proc < size; proc++) {
            int proc_rows_per_process = max_row / size;
            int proc_remainder = max_row % size;
            int proc_start_row = proc * proc_rows_per_process + (proc < proc_remainder ? proc : proc_remainder);
            int proc_end_row = proc_start_row + proc_rows_per_process + (proc < proc_remainder ? 1 : 0);
            int proc_local_rows = proc_end_row - proc_start_row;

            for(int r = 0; r < proc_local_rows; r++) {
                MPI_Recv(mat[proc_start_row + r], max_column, MPI_CHAR, proc, 0, MPI_COMM_WORLD, MPI_STATUS_IGNORE);
            }
        }

        // Imprimir resultado
        for(int r = 0; r < max_row; ++r){
            for(int c = 0; c < max_column; ++c)
                printf("%c", mat[r][c]);
            printf("\n");
        }

        // Liberar memória da matriz completa
        for(int i = 0; i < max_row; i++)
            free(mat[i]);
        free(mat);
    } else {
        // Processos workers enviam seus dados
        for(int r = 0; r < local_rows; r++) {
            MPI_Send(local_mat[r], max_column, MPI_CHAR, 0, 0, MPI_COMM_WORLD);
        }
    }

    // Liberar memória local
    for(int i = 0; i < local_rows; i++)
        free(local_mat[i]);
    free(local_mat);

    MPI_Finalize();
    return 0;
}