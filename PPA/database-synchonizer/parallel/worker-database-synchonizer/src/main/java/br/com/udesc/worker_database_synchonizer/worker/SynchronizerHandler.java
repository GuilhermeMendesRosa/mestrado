package br.com.udesc.worker_database_synchonizer.worker;

import br.com.udesc.worker_database_synchonizer.dto.TableDTO;
import org.springframework.scheduling.annotation.Scheduled;
import org.springframework.stereotype.Component;

import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.TimeUnit;

@Component
public class SynchronizerHandler {

    private final Connector connector;
    private boolean synchronizationInvoked = false;
    private boolean synchronizationRunning = false;

    public SynchronizerHandler(Connector connector) {
        this.connector = connector;
    }

    public void invokeSynchronization() {
        synchronizationInvoked = true;
    }

    @Scheduled(fixedRate = 5000)
    private void synchronize() {
        if (!synchronizationInvoked || synchronizationRunning) {
            return;
        }

        synchronizationRunning = true;
        synchronizationInvoked = false;

        // Executa a sincronização em uma thread separada para não travar o scheduler
        new Thread(() -> {
            ExecutorService threadPool = Executors.newFixedThreadPool(3);

            for (int i = 0; i < 3; i++) {
                threadPool.submit(() -> {
                    while (true) {
                        TableDTO tableDTO = connector.nextTable();

                        if (Boolean.TRUE.equals(tableDTO.isFinished)) {
                            break;
                        }

                        proccessTable(tableDTO);
                    }
                });
            }

            threadPool.shutdown();

            try {
                // Agora pode esperar sem travar o scheduler
                threadPool.awaitTermination(Long.MAX_VALUE, TimeUnit.SECONDS);

                // Só chama quando todas as threads terminaram
                connector.synchronizationFinished();

            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
                throw new RuntimeException(e);
            } finally {
                synchronizationRunning = false;
            }
        }).start();
    }

    private void proccessTable(TableDTO tableDTO) {
        try {
            Thread.sleep(3000);
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
            throw new RuntimeException(e);
        }
    }
}