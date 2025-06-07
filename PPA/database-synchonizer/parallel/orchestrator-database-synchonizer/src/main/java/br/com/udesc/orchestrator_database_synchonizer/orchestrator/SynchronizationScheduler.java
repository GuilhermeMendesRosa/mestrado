package br.com.udesc.orchestrator_database_synchonizer.orchestrator;

import br.com.udesc.orchestrator_database_synchonizer.orchestrator.dto.WorkerDTO;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.scheduling.annotation.Scheduled;
import org.springframework.stereotype.Component;

@Component
public class SynchronizationScheduler {

    private static final Logger logger = LoggerFactory.getLogger(SynchronizationScheduler.class);
    private static final int SECOND = 1000;
    private static final int MINUTE = 60 * SECOND;
    private static final int INITIAL_DELAY = MINUTE / 6;
    private static final int SYNC_INTERVAL = 2 * MINUTE;

    private final WorkersPool workersPool;
    private final Tables tables;
    private final Connector connector;

    public SynchronizationScheduler(WorkersPool workersPool, Tables tables, Connector connector) {
        this.workersPool = workersPool;
        this.tables = tables;
        this.connector = connector;
        logger.info("SynchronizationScheduler inicializado com intervalo de {} minutos", SYNC_INTERVAL / MINUTE);
    }

    @Scheduled(initialDelay = INITIAL_DELAY, fixedRate = SYNC_INTERVAL)
    public void performSync() {
        logger.info("Iniciando ciclo de sincronização agendada");

        try {
            logger.debug("Preparando tabelas para sincronização");
            tables.startSynchronization();

            logger.debug("Iniciando pool de workers");
            workersPool.startSynchonization();

            logger.info("Enviando sinais de início para todos os workers");
            startWorkers();

            logger.info("Aguardando finalização de todos os workers");
            workersPool.waitWorkers();

            logger.info("Sincronização concluída com sucesso");

        } catch (Exception e) {
            logger.error("Erro durante ciclo de sincronização: {}", e.getMessage(), e);
        }
    }

    private void startWorkers() {
        logger.debug("Enviando sinais de início para {} workers", workersPool.getWorkers().size());

        for (WorkerDTO workerDTO : workersPool.getWorkers()) {
            logger.debug("Enviando sinal para worker: {}", workerDTO.getHost());
            connector.sendSignalToStartSync(workerDTO);
        }

        logger.info("Sinais enviados para todos os workers disponíveis");
    }
}