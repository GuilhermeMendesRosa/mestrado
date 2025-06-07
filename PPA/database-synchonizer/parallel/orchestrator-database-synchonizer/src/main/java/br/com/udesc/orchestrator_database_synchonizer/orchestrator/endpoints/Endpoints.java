package br.com.udesc.orchestrator_database_synchonizer.orchestrator.endpoints;

import br.com.udesc.orchestrator_database_synchonizer.orchestrator.SynchronizationScheduler;
import br.com.udesc.orchestrator_database_synchonizer.orchestrator.Tables;
import br.com.udesc.orchestrator_database_synchonizer.orchestrator.WorkersPool;
import br.com.udesc.orchestrator_database_synchonizer.orchestrator.dto.TableDTO;
import br.com.udesc.orchestrator_database_synchonizer.orchestrator.dto.WorkerDTO;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class Endpoints {

    private final WorkersPool workersPool;
    private final Tables tables;

    public Endpoints(WorkersPool workersPool, SynchronizationScheduler synchronizationScheduler, Tables tables) {
        this.workersPool = workersPool;
        this.tables = tables;
    }

    @PostMapping("/connect")
    public ResponseEntity<Void> connect(@RequestBody WorkerDTO workerDTO) {
        workersPool.connect(workerDTO);
        return ResponseEntity.ok().build();
    }

    @GetMapping("/finish")
    public ResponseEntity<Void> someWorkerFinish() {
        workersPool.someWorkerFinish();
        return ResponseEntity.ok().build();
    }

    @GetMapping("/next-table")
    public ResponseEntity<TableDTO> nextTable() {
        return ResponseEntity.ok(tables.nextTable());
    }
}