package br.com.udesc.orquestrator_database_synchonizer.orquestrator;

import br.com.udesc.orquestrator_database_synchonizer.orquestrator.dto.Worker;
import org.springframework.stereotype.Component;

import java.util.Collections;
import java.util.HashSet;
import java.util.Set;

@Component
public class WorkersPool {

    private final Set<Worker> workers = Collections.synchronizedSet(new HashSet<>());

    public void connect(Worker worker) {
        this.workers.add(worker);
    }

    public Set<Worker> getWorkers() {
        if (workers.isEmpty()) {
            throw new IllegalStateException("Nenhum worker conectado.");
        }
        return Set.copyOf(workers);
    }
}