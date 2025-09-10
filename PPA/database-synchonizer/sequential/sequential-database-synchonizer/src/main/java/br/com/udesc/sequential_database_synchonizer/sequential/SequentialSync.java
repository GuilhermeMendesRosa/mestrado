package br.com.udesc.sequential_database_synchonizer.sequential;

import jakarta.annotation.PostConstruct;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.stereotype.Component;

import java.sql.SQLException;

@Component
public class SequentialSync {

    private static final Logger logger = LoggerFactory.getLogger(SequentialSync.class);
    private final DatabaseSynchronizationService service;

    public SequentialSync(DatabaseSynchronizationService service) {
        this.service = service;
    }

    @PostConstruct
    public void sync() throws SQLException {
        long startTime = System.currentTimeMillis();
        logger.info("Iniciando sincronização sequencial das tabelas...");

        for (int i = 1; i < 31; i++) {
            String table = "tabela" + i;
            logger.debug("Sincronizando {}", table);
            service.synchronizeTable(table);
        }

        long endTime = System.currentTimeMillis();
        long duration = endTime - startTime;

        logger.info("Sincronização concluída em {} ms", duration);
    }
}
