package br.com.udesc.worker_database_synchonizer.endpoint;

import br.com.udesc.worker_database_synchonizer.worker.SynchronizerHandler;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

@RestController
public class Endpoints {

    private static final Logger logger = LoggerFactory.getLogger(Endpoints.class);

    private final SynchronizerHandler synchronizerHandler;

    public Endpoints(SynchronizerHandler synchronizerHandler) {
        this.synchronizerHandler = synchronizerHandler;
        logger.info("Endpoints inicializado");
    }

    @GetMapping("/start-sync")
    public ResponseEntity<Void> startSync() {
        logger.info("Iniciando sincronização");

        try {
            synchronizerHandler.invokeSynchronization();
            logger.info("Sincronização executada com sucesso");

        } catch (Exception e) {
            logger.error("Erro durante sincronização: {}", e.getMessage(), e);
        }

        return ResponseEntity.ok().build();
    }
}