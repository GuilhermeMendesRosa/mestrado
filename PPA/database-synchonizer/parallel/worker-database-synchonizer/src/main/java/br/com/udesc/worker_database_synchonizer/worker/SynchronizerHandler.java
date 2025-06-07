package br.com.udesc.worker_database_synchonizer.worker;

import br.com.udesc.worker_database_synchonizer.dto.TableDTO;
import org.springframework.scheduling.annotation.Async;
import org.springframework.stereotype.Component;

import java.util.concurrent.CompletableFuture;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.TimeUnit;
import java.util.concurrent.atomic.AtomicBoolean;

@Component
public class SynchronizerHandler {

    private final Connector connector;
    private final AtomicBoolean synchronizationRunning = new AtomicBoolean(false);

    public SynchronizerHandler(Connector connector) {
        this.connector = connector;
    }

    public void invokeSynchronization() {
        if (synchronizationRunning.compareAndSet(false, true)) {
            synchronizeAsync();
        }
    }

    @Async
    protected CompletableFuture<Void> synchronizeAsync() {
        return CompletableFuture.runAsync(() -> {
            try {
                ExecutorService threadPool = Executors.newFixedThreadPool(3);

                for (int i = 0; i < 3; i++) {
                    threadPool.submit(() -> {
                        while (true) {
                            TableDTO tableDTO = connector.nextTable();

                            if (Boolean.TRUE.equals(tableDTO.getFinished())) {
                                break;
                            }

                            processTable(tableDTO);
                        }
                    });
                }

                threadPool.shutdown();
                threadPool.awaitTermination(Long.MAX_VALUE, TimeUnit.SECONDS);
                connector.synchronizationFinished();

            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
                throw new RuntimeException(e);
            } finally {
                synchronizationRunning.set(false);
            }
        });
    }

    private void processTable(TableDTO tableDTO) {
        try {
            Thread.sleep(3000);
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
            throw new RuntimeException(e);
        }
    }
}