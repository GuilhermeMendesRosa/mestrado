package br.com.udesc.orchestrator_database_synchonizer.orchestrator.endpoints;

import br.com.udesc.orchestrator_database_synchonizer.orchestrator.SynchronizationScheduler;
import br.com.udesc.orchestrator_database_synchonizer.orchestrator.Tables;
import br.com.udesc.orchestrator_database_synchonizer.orchestrator.WorkersPool;
import br.com.udesc.orchestrator_database_synchonizer.orchestrator.dto.TableDTO;
import br.com.udesc.orchestrator_database_synchonizer.orchestrator.dto.WorkerDTO;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class Endpoints {

    private static final Logger logger = LoggerFactory.getLogger(Endpoints.class);

    private final WorkersPool workersPool;
    private final Tables tables;

    public Endpoints(WorkersPool workersPool, SynchronizationScheduler synchronizationScheduler, Tables tables) {
        this.workersPool = workersPool;
        this.tables = tables;
        logger.info("Endpoints do orchestrator inicializados");
    }

    @PostMapping("/connect")
    public ResponseEntity<Void> connect(@RequestBody WorkerDTO workerDTO) {
        logger.info("Recebida conexão de worker: {}", workerDTO);

        try {
            workersPool.connect(workerDTO);
            logger.info("Worker conectado com sucesso: {}", workerDTO);
            return ResponseEntity.ok().build();

        } catch (Exception e) {
            logger.error("Erro ao conectar worker {}: {}", workerDTO, e.getMessage(), e);
            return ResponseEntity.internalServerError().build();
        }
    }

    @GetMapping("/finish")
    public ResponseEntity<Void> someWorkerFinish() {
        logger.info("Worker notificou finalização de sincronização");

        try {
            workersPool.someWorkerFinish();
            logger.info("Finalização de worker processada com sucesso");
            return ResponseEntity.ok().build();

        } catch (Exception e) {
            logger.error("Erro ao processar finalização de worker: {}", e.getMessage(), e);
            return ResponseEntity.internalServerError().build();
        }
    }

    @GetMapping("/next-table")
    public ResponseEntity<TableDTO> nextTable() {
        logger.debug("Solicitação de próxima tabela recebida");

        try {
            TableDTO nextTable = tables.nextTable();

            if (nextTable != null) {
                logger.debug("Próxima tabela fornecida: {}", nextTable);
            } else {
                logger.debug("Nenhuma tabela disponível");
            }

            return ResponseEntity.ok(nextTable);

        } catch (Exception e) {
            logger.error("Erro ao obter próxima tabela: {}", e.getMessage(), e);
            return ResponseEntity.internalServerError().build();
        }
    }
}