package br.com.udesc.orchestrator_database_synchonizer.orchestrator;

import br.com.udesc.orchestrator_database_synchonizer.orchestrator.dto.WorkerDTO;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.stereotype.Component;

import java.util.Collections;
import java.util.HashSet;
import java.util.Set;

@Component
public class WorkersPool {

    private static final Logger logger = LoggerFactory.getLogger(WorkersPool.class);
    private static final int SECOND = 1000;

    private final Set<WorkerDTO> workerDTOS = Collections.synchronizedSet(new HashSet<>());
    private Integer workersRunning = 0;

    public void connect(WorkerDTO workerDTO) {
        logger.info("Conectando worker: {}", workerDTO.getHost());

        boolean isNewWorker = this.workerDTOS.add(workerDTO);

        if (isNewWorker) {
            logger.info("Worker {} conectado com sucesso. Total de workers: {}",
                    workerDTO.getHost(), workerDTOS.size());
        } else {
            logger.debug("Worker {} já estava conectado", workerDTO.getHost());
        }
    }

    public Set<WorkerDTO> getWorkers() {
        if (workerDTOS.isEmpty()) {
            logger.error("Tentativa de obter workers sem nenhum conectado");
            throw new IllegalStateException("Nenhum worker conectado.");
        }

        logger.debug("Retornando {} workers conectados", workerDTOS.size());
        return Set.copyOf(workerDTOS);
    }

    public void startSynchonization() {
        workersRunning = workerDTOS.size();
        logger.info("Iniciando sincronização com {} workers", workersRunning);
    }

    public synchronized void someWorkerFinish() {
        this.workersRunning--;
        logger.info("Worker finalizou sincronização. Workers restantes: {}", workersRunning);

        if (workersRunning == 0) {
            logger.info("Todos os workers finalizaram a sincronização");
        }
    }

    public void waitWorkers() throws InterruptedException {
        logger.info("Aguardando finalização de {} workers", workersRunning);

        while (workersRunning > 0) {
            logger.debug("Aguardando {} workers finalizarem...", workersRunning);
            Thread.sleep(SECOND);
        }

        logger.info("Todos os workers finalizaram");
    }
}