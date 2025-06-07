package br.com.udesc.worker_database_synchonizer.worker;

import br.com.udesc.worker_database_synchonizer.dto.TableDTO;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.scheduling.annotation.Async;
import org.springframework.stereotype.Component;

import java.util.concurrent.CompletableFuture;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.TimeUnit;
import java.util.concurrent.atomic.AtomicBoolean;

@Component
public class SynchronizerHandler {

    private static final Logger logger = LoggerFactory.getLogger(SynchronizerHandler.class);
    private static final int THREAD_POOL_SIZE = 3;
    private static final long PROCESSING_DELAY_MS = 3000;

    private final Connector connector;
    private final AtomicBoolean synchronizationRunning = new AtomicBoolean(false);

    public SynchronizerHandler(Connector connector) {
        this.connector = connector;
        logger.info("SynchronizerHandler inicializado");
    }

    public void invokeSynchronization() {
        logger.info("Tentativa de iniciar sincronização");

        if (synchronizationRunning.compareAndSet(false, true)) {
            logger.info("Sincronização iniciada com sucesso");
            synchronizeAsync();
        } else {
            logger.warn("Sincronização já está em execução, ignorando nova solicitação");
        }
    }

    @Async
    protected CompletableFuture<Void> synchronizeAsync() {
        return CompletableFuture.runAsync(() -> {
            logger.info("Iniciando processo de sincronização assíncrona");

            try {
                ExecutorService threadPool = Executors.newFixedThreadPool(THREAD_POOL_SIZE);
                logger.debug("Thread pool criado com {} threads", THREAD_POOL_SIZE);

                for (int i = 0; i < THREAD_POOL_SIZE; i++) {
                    final int threadId = i + 1;
                    threadPool.submit(() -> {
                        logger.debug("Thread {} iniciada para processamento de tabelas", threadId);
                        processTablesInThread(threadId);
                    });
                }

                logger.info("Aguardando finalização de todas as threads");
                threadPool.shutdown();
                threadPool.awaitTermination(Long.MAX_VALUE, TimeUnit.SECONDS);

                logger.info("Todas as threads finalizadas, notificando orchestrator");
                connector.synchronizationFinished();
                logger.info("Sincronização concluída com sucesso");

            } catch (InterruptedException e) {
                logger.error("Sincronização interrompida: {}", e.getMessage());
                Thread.currentThread().interrupt();
                throw new RuntimeException("Sincronização interrompida", e);
            } catch (Exception e) {
                logger.error("Erro durante sincronização: {}", e.getMessage(), e);
                throw new RuntimeException("Falha na sincronização", e);
            } finally {
                synchronizationRunning.set(false);
                logger.info("Flag de sincronização resetada");
            }
        });
    }

    private void processTablesInThread(int threadId) {
        logger.debug("Thread {} iniciando processamento de tabelas", threadId);

        while (true) {
            logger.debug("Thread {} solicitando próxima tabela", threadId);
            TableDTO tableDTO = connector.nextTable();

            if (tableDTO == null) {
                logger.warn("Thread {} recebeu tabela nula, continuando", threadId);
                continue;
            }

            if (Boolean.TRUE.equals(tableDTO.getFinished())) {
                logger.info("Thread {} recebeu sinal de finalização", threadId);
                break;
            }

            logger.debug("Thread {} processando tabela: {}", threadId, tableDTO);
            processTable(tableDTO, threadId);
        }

        logger.debug("Thread {} finalizada", threadId);
    }

    private void processTable(TableDTO tableDTO, int threadId) {
        logger.debug("Thread {} iniciando processamento da tabela", threadId);

        try {
            Thread.sleep(PROCESSING_DELAY_MS);
            logger.debug("Thread {} finalizou processamento da tabela", threadId);

        } catch (InterruptedException e) {
            logger.error("Thread {} interrompida durante processamento: {}", threadId, e.getMessage());
            Thread.currentThread().interrupt();
            throw new RuntimeException("Processamento interrompido", e);
        }
    }
}