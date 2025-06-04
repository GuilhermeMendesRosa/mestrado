package br.com.udesc.orquestrator_database_synchonizer.orquestrator;

import br.com.udesc.orquestrator_database_synchonizer.orquestrator.dto.Worker;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/connect")
public class Connector {

    private final WorkersPool workersPool;

    public Connector(WorkersPool workersPool) {
        this.workersPool = workersPool;
    }

    @PostMapping
    public ResponseEntity<Void> connect(@RequestBody Worker worker) {
        workersPool.connect(worker);
        return ResponseEntity.ok().build();
    }
}