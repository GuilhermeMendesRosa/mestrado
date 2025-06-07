package br.com.udesc.orchestrator_database_synchonizer.orchestrator;

import br.com.udesc.orchestrator_database_synchonizer.orchestrator.dto.WorkerDTO;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.scheduling.annotation.Scheduled;
import org.springframework.stereotype.Component;

import java.time.Duration;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;

@Component
public class SynchronizationScheduler {

    private static final Logger logger = LoggerFactory.getLogger(SynchronizationScheduler.class);
    private static final int SECOND = 1000;
    private static final int MINUTE = 60 * SECOND;
    private static final int INITIAL_DELAY = MINUTE / 6;
    private static final int SYNC_INTERVAL = 2 * MINUTE;
    private static final DateTimeFormatter TIME_FORMATTER = DateTimeFormatter.ofPattern("HH:mm:ss.SSS");

    private final WorkersPool workersPool;
    private final Tables tables;
    private final Connector connector;

    public SynchronizationScheduler(WorkersPool workersPool, Tables tables, Connector connector) {
        this.workersPool = workersPool;
        this.tables = tables;
        this.connector = connector;
        logger.info("SynchronizationScheduler inicializado com intervalo de {} minutos", SYNC_INTERVAL / MINUTE);
    }

    @Scheduled(initialDelay = INITIAL_DELAY, fixedRate = SYNC_INTERVAL)
    public void performSync() {
        LocalDateTime syncStartTime = LocalDateTime.now();
        logger.info("=== INICIANDO CICLO DE SINCRONIZAÇÃO ===");
        logger.info("Horário de início: {}", syncStartTime.format(TIME_FORMATTER));

        try {
            LocalDateTime prepStartTime = LocalDateTime.now();
            logger.info("Preparando tabelas para sincronização");
            tables.startSynchronization();

            logger.info("Iniciando pool de workers");
            workersPool.startSynchonization();

            Duration prepDuration = Duration.between(prepStartTime, LocalDateTime.now());
            logger.info("Preparação concluída em {}ms", prepDuration.toMillis());

            LocalDateTime signalStartTime = LocalDateTime.now();
            logger.info("Enviando sinais de início para todos os workers");
            startWorkers();

            Duration signalDuration = Duration.between(signalStartTime, LocalDateTime.now());
            logger.info("Sinais enviados em {}ms", signalDuration.toMillis());

            LocalDateTime waitStartTime = LocalDateTime.now();
            logger.info("Aguardando finalização de todos os workers");
            workersPool.waitWorkers();

            Duration waitDuration = Duration.between(waitStartTime, LocalDateTime.now());
            logger.info("Workers finalizados em {}ms", waitDuration.toMillis());

            LocalDateTime finishStartTime = LocalDateTime.now();
            logger.info("Finalizando sincronização");
            tables.finalizeSynchronization();

            Duration finishDuration = Duration.between(finishStartTime, LocalDateTime.now());
            logger.info("Finalização concluída em {}ms", finishDuration.toMillis());

            LocalDateTime syncEndTime = LocalDateTime.now();
            Duration totalDuration = Duration.between(syncStartTime, syncEndTime);

            logger.info("=== SINCRONIZAÇÃO CONCLUÍDA COM SUCESSO ===");
            logger.info("Horário de término: {}", syncEndTime.format(TIME_FORMATTER));
            logger.info("Tempo total de sincronização: {}ms ({}s)",
                    totalDuration.toMillis(),
                    String.format("%.2f", totalDuration.toMillis() / 1000.0));

            logSyncStatistics(prepDuration, signalDuration, waitDuration, finishDuration, totalDuration);

        } catch (Exception e) {
            LocalDateTime errorTime = LocalDateTime.now();
            Duration errorDuration = Duration.between(syncStartTime, errorTime);

            logger.error("=== ERRO DURANTE CICLO DE SINCRONIZAÇÃO ===");
            logger.error("Tempo até erro: {}ms", errorDuration.toMillis());
            logger.error("Erro: {}", e.getMessage(), e);

            try {
                tables.finalizeSynchronization();
                logger.info("Limpeza de emergência realizada");
            } catch (Exception cleanupError) {
                logger.error("Erro durante limpeza de emergência: {}", cleanupError.getMessage());
            }
        }
    }

    private void startWorkers() {
        logger.debug("Enviando sinais de início para {} workers", workersPool.getWorkers().size());

        for (WorkerDTO workerDTO : workersPool.getWorkers()) {
            logger.debug("Enviando sinal para worker: {}", workerDTO.getHost());
            connector.sendSignalToStartSync(workerDTO);
        }

        logger.info("Sinais enviados para todos os workers disponíveis");
    }

    private void logSyncStatistics(Duration prep, Duration signal, Duration wait, Duration finish, Duration total) {
        logger.info("=== ESTATÍSTICAS DE TEMPO ===");
        logger.info("Preparação: {}ms ({}%)", prep.toMillis(), calculatePercentage(prep, total));
        logger.info("Envio de sinais: {}ms ({}%)", signal.toMillis(), calculatePercentage(signal, total));
        logger.info("Aguardo workers: {}ms ({}%)", wait.toMillis(), calculatePercentage(wait, total));
        logger.info("Finalização: {}ms ({}%)", finish.toMillis(), calculatePercentage(finish, total));
        logger.info("Total: {}ms (100%)", total.toMillis());
    }

    private String calculatePercentage(Duration part, Duration total) {
        if (total.toMillis() == 0) return "0.00";
        double percentage = (part.toMillis() * 100.0) / total.toMillis();
        return String.format("%.2f", percentage);
    }
}