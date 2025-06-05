package br.com.udesc.worker_database_synchonizer.endpoint;

import br.com.udesc.worker_database_synchonizer.worker.SynchronizerHandler;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

@RestController
public class Endpoints {

    private final SynchronizerHandler synchronizerHandler;

    public Endpoints(SynchronizerHandler synchronizerHandler) {
        this.synchronizerHandler = synchronizerHandler;
    }

    @GetMapping("/start-sync")
    public ResponseEntity<Void> startSync() {
        synchronizerHandler.invokeSynchronization();
        return ResponseEntity.ok().build();
    }
}