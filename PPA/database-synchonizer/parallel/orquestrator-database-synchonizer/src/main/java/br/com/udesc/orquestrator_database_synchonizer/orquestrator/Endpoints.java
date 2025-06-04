package br.com.udesc.orquestrator_database_synchonizer.orquestrator;

import br.com.udesc.orquestrator_database_synchonizer.orquestrator.dto.Worker;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

@RestController
public class Endpoints {

    private final WorkersPool workersPool;

    public Endpoints(WorkersPool workersPool) {
        this.workersPool = workersPool;
    }

    @PostMapping("/connect")
    public ResponseEntity<Void> connect(@RequestBody Worker worker) {
        workersPool.connect(worker);
        return ResponseEntity.ok().build();
    }
}