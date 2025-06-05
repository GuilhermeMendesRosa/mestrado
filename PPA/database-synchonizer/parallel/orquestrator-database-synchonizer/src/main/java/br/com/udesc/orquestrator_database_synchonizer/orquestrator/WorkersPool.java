package br.com.udesc.orquestrator_database_synchonizer.orquestrator;

import br.com.udesc.orquestrator_database_synchonizer.orquestrator.dto.WorkerDTO;
import org.springframework.stereotype.Component;

import java.util.Collections;
import java.util.HashSet;
import java.util.Set;

@Component
public class WorkersPool {

    private final Set<WorkerDTO> workerDTOS = Collections.synchronizedSet(new HashSet<>());
    private Integer workersRunning = 0;

    public static final int SECOND = 1000;

    public void connect(WorkerDTO workerDTO) {
        this.workerDTOS.add(workerDTO);
    }

    public Set<WorkerDTO> getWorkers() {
        if (workerDTOS.isEmpty()) {
            throw new IllegalStateException("Nenhum worker conectado.");
        }
        return Set.copyOf(workerDTOS);
    }

    public void startSynchonization() {
        workersRunning = workerDTOS.size();
    }

    public synchronized void someWorkerFinish() {
        this.workersRunning--;
    }

    public void waitWorkers() throws InterruptedException {
        while (workersRunning > 0) {
            Thread.sleep(SECOND);
        }
    }
}