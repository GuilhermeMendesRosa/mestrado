package br.com.udesc.orchestrator_database_synchonizer.orchestrator;

import br.com.udesc.orchestrator_database_synchonizer.orchestrator.dto.WorkerDTO;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.stereotype.Component;

import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;

@Component
public class Connector {

    private static final Logger logger = LoggerFactory.getLogger(Connector.class);
    private static final int WORKER_PORT = 8081;
    private static final String START_SYNC_ENDPOINT = "/start-sync";

    private final HttpClient httpClient = HttpClient.newHttpClient();

    public void sendSignalToStartSync(WorkerDTO workerDTO) {
        logger.info("Enviando sinal de início de sincronização para worker: {}", workerDTO.getHost());

        try {
            String syncUrl = buildWorkerUrl(workerDTO.getHost(), START_SYNC_ENDPOINT);
            logger.debug("Enviando requisição para: {}", syncUrl);

            HttpRequest request = HttpRequest.newBuilder()
                    .uri(URI.create(syncUrl))
                    .GET()
                    .build();

            HttpResponse<String> response = httpClient.send(request, HttpResponse.BodyHandlers.ofString());

            logger.info("Sinal enviado com sucesso para worker {}. Status: {}, Resposta: {}",
                    workerDTO.getHost(), response.statusCode(), response.body());

        } catch (Exception e) {
            logger.error("Erro ao enviar sinal de sincronização para worker {}: {}",
                    workerDTO.getHost(), e.getMessage(), e);
        }
    }

    private String buildWorkerUrl(String host, String endpoint) {
        return String.format("http://%s:%d%s", host, WORKER_PORT, endpoint);
    }
}