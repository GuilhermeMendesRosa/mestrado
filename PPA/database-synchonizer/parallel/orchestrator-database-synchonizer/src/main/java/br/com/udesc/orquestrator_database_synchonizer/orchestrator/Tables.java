package br.com.udesc.orchestrator_database_synchonizer.orchestrator;

import br.com.udesc.orchestrator_database_synchonizer.orchestrator.dto.TableDTO;
import org.springframework.stereotype.Component;

import java.util.Stack;
import java.util.concurrent.ConcurrentLinkedDeque;

@Component
public class Tables {

    private final Stack<TableDTO> defaultStack;
    private final ConcurrentLinkedDeque<TableDTO> threadSafeStack;
    private volatile boolean synchronizationActive;

    public Tables() {
        this.defaultStack = new Stack<>();
        this.threadSafeStack = new ConcurrentLinkedDeque<>();
        this.synchronizationActive = false;

        // Inicializa a pilha padrão com 90 tabelas
        for (int i = 1; i <= 9  ; i++) {
            defaultStack.push(new TableDTO("tabela" + i));
        }
    }

    /**
     * Inicia a sincronização copiando da pilha padrão para a thread-safe
     */
    public synchronized void startSynchronization() {
        if (synchronizationActive) {
            throw new IllegalStateException("Sincronização já está ativa");
        }

        // Copia todas as tabelas da pilha padrão para a thread-safe
        threadSafeStack.clear();
        for (TableDTO table : defaultStack) {
            threadSafeStack.addFirst(table); // Mantém a ordem da pilha
        }

        synchronizationActive = true;
    }

    /**
     * Retorna a próxima tabela da pilha thread-safe
     */
    public TableDTO nextTable() {
        if (!synchronizationActive) {
            throw new IllegalStateException("Sincronização não está ativa. Chame startSynchronization() primeiro.");
        }

        TableDTO table = threadSafeStack.pollFirst();
        if (table == null) {
            table = new TableDTO();
            table.isFinished = true;
        }

        return table;
    }

    /**
     * Finaliza a sincronização limpando a pilha thread-safe
     */
    public synchronized void finalizeSynchronization() {
        threadSafeStack.clear();
        synchronizationActive = false;
    }

    /**
     * Verifica se a sincronização está ativa
     */
    public boolean isSynchronizationActive() {
        return synchronizationActive;
    }

    /**
     * Retorna o número de tabelas restantes na pilha thread-safe
     */
    public int getRemainingTables() {
        return threadSafeStack.size();
    }
}