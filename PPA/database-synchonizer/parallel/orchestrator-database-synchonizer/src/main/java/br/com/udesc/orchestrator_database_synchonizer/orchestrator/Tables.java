package br.com.udesc.orchestrator_database_synchonizer.orchestrator;

import br.com.udesc.orchestrator_database_synchonizer.orchestrator.dto.TableDTO;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.stereotype.Component;

import java.util.Stack;
import java.util.concurrent.ConcurrentLinkedDeque;

@Component
public class Tables {

    private static final Logger logger = LoggerFactory.getLogger(Tables.class);
    private static final int DEFAULT_TABLE_COUNT = 9;

    private final Stack<TableDTO> defaultStack;
    private final ConcurrentLinkedDeque<TableDTO> threadSafeStack;
    private volatile boolean synchronizationActive;

    public Tables() {
        this.defaultStack = new Stack<>();
        this.threadSafeStack = new ConcurrentLinkedDeque<>();
        this.synchronizationActive = false;

        initializeDefaultTables();
        logger.info("Tables inicializado com {} tabelas padrão", DEFAULT_TABLE_COUNT);
    }

    private void initializeDefaultTables() {
        for (int i = 1; i <= DEFAULT_TABLE_COUNT; i++) {
            defaultStack.push(new TableDTO("tabela" + i));
        }
        logger.debug("Inicializadas {} tabelas na pilha padrão", DEFAULT_TABLE_COUNT);
    }

    public synchronized void startSynchronization() {
        logger.info("Iniciando sincronização de tabelas");

        if (synchronizationActive) {
            logger.warn("Tentativa de iniciar sincronização já ativa");
            throw new IllegalStateException("Sincronização já está ativa");
        }

        threadSafeStack.clear();
        for (TableDTO table : defaultStack) {
            threadSafeStack.addFirst(table);
        }

        synchronizationActive = true;
        logger.info("Sincronização iniciada com {} tabelas disponíveis", threadSafeStack.size());
    }

    public TableDTO nextTable() {
        if (!synchronizationActive) {
            logger.error("Tentativa de obter tabela sem sincronização ativa");
            throw new IllegalStateException("Sincronização não está ativa. Chame startSynchronization() primeiro.");
        }

        TableDTO table = threadSafeStack.pollFirst();

        if (table == null) {
            logger.info("Todas as tabelas foram processadas, retornando sinal de finalização");
            table = new TableDTO();
            table.setFinished(true);
        } else {
            logger.debug("Fornecendo tabela: {}. Restantes: {}", table.getName(), threadSafeStack.size());
        }

        return table;
    }

    public synchronized void finalizeSynchronization() {
        logger.info("Finalizando sincronização de tabelas");

        threadSafeStack.clear();
        synchronizationActive = false;

        logger.info("Sincronização finalizada");
    }

    public boolean isSynchronizationActive() {
        return synchronizationActive;
    }

    public int getRemainingTables() {
        return threadSafeStack.size();
    }
}