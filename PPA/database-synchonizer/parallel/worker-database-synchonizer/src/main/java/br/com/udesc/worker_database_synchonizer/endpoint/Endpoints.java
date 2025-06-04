package br.com.udesc.worker_database_synchonizer.endpoint;

import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

@RestController
public class Endpoints {


    @GetMapping("/start-sync")
    public ResponseEntity<Void> startSync() {
        return ResponseEntity.ok().build();
    }
}