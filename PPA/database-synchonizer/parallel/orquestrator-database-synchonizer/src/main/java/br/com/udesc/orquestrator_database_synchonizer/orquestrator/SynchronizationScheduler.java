package br.com.udesc.orquestrator_database_synchonizer.orquestrator;

import br.com.udesc.orquestrator_database_synchonizer.orquestrator.dto.WorkerDTO;
import org.springframework.scheduling.annotation.Scheduled;
import org.springframework.stereotype.Component;

@Component
public class SynchronizationScheduler {

    private final WorkersPool workersPool;
    private final Tables tables;
    private final Connector connector;

    public static final int SECOND = 1000;
    public static final int MINUTE = 60 * SECOND;

    public SynchronizationScheduler(WorkersPool workersPool, Tables tables, Connector connector) {
        this.workersPool = workersPool;
        this.tables = tables;
        this.connector = connector;
    }

    @Scheduled(initialDelay = MINUTE / 6, fixedRate = 2 * MINUTE)
    public void performSync() {
        try {
            tables.startSynchronization();
            workersPool.startSynchonization();
            startWorkers();
            workersPool.waitWorkers();
            System.out.println("Synchronization completed.");
        } catch (Exception e) {
            System.err.println("Erro na sincronização: " + e.getMessage());
        }
    }

    private void startWorkers() {
        for (WorkerDTO workerDTO : workersPool.getWorkers()) {
            connector.sendSignalToStartSync(workerDTO);
        }
    }


}