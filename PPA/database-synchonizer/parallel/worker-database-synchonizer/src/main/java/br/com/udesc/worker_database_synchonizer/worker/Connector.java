package br.com.udesc.worker_database_synchonizer.worker;

import br.com.udesc.worker_database_synchonizer.dto.TableDTO;
import br.com.udesc.worker_database_synchonizer.dto.WorkerDTO;
import com.fasterxml.jackson.databind.ObjectMapper;
import jakarta.annotation.PostConstruct;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Component;

import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;

import static java.net.http.HttpResponse.BodyHandlers;

@Component
public class Connector {

    private static final Logger logger = LoggerFactory.getLogger(Connector.class);
    private static final String CONTENT_TYPE_JSON = "application/json";
    private static final int HTTP_OK = 200;
    private static final int ORCHESTRATOR_PORT = 8080;

    @Value("${orchestrator.host}")
    private String orchestratorHost;

    private final HttpClient httpClient = HttpClient.newHttpClient();
    private final ObjectMapper objectMapper = new ObjectMapper();

    @PostConstruct
    public void connectToOrchestrator() {
        logger.info("Iniciando conexão com orchestrator: {}", orchestratorHost);

        WorkerDTO workerInfo = new WorkerDTO("localhost");

        try {
            String connectionUrl = buildUrl("/connect");
            logger.debug("Enviando requisição de conexão para: {}", connectionUrl);

            String workerJson = objectMapper.writeValueAsString(workerInfo);

            HttpRequest request = HttpRequest.newBuilder()
                    .uri(URI.create(connectionUrl))
                    .header("Content-Type", CONTENT_TYPE_JSON)
                    .POST(HttpRequest.BodyPublishers.ofString(workerJson))
                    .build();

            HttpResponse<String> response = httpClient.send(request, BodyHandlers.ofString());

            logger.info("Conexão estabelecida com orchestrator. Status: {}, Resposta: {}",
                    response.statusCode(), response.body());

        } catch (Exception e) {
            logger.error("Erro ao conectar com orchestrator {}: {}", orchestratorHost, e.getMessage(), e);
        }
    }

    public TableDTO nextTable() {
        logger.debug("Solicitando próxima tabela do orchestrator");

        try {
            String nextTableUrl = buildUrl("/next-table");
            logger.debug("Requisitando próxima tabela de: {}", nextTableUrl);

            HttpRequest request = HttpRequest.newBuilder()
                    .uri(URI.create(nextTableUrl))
                    .header("Content-Type", CONTENT_TYPE_JSON)
                    .GET()
                    .build();

            HttpResponse<String> response = httpClient.send(request, BodyHandlers.ofString());

            if (response.statusCode() == HTTP_OK) {
                TableDTO tableDTO = objectMapper.readValue(response.body(), TableDTO.class);
                logger.info("Tabela recebida com sucesso: {}", tableDTO);
                return tableDTO;
            } else {
                logger.warn("Falha ao obter próxima tabela. Status: {}, Body: {}",
                        response.statusCode(), response.body());
                return null;
            }

        } catch (Exception e) {
            logger.error("Erro ao requisitar próxima tabela: {}", e.getMessage(), e);
            return null;
        }
    }

    public void synchronizationFinished() {
        logger.info("Notificando orchestrator sobre finalização da sincronização");

        try {
            String finishUrl = buildUrl("/finish");
            logger.debug("Enviando notificação de finalização para: {}", finishUrl);

            HttpRequest request = HttpRequest.newBuilder()
                    .uri(URI.create(finishUrl))
                    .header("Content-Type", CONTENT_TYPE_JSON)
                    .GET()
                    .build();

            HttpResponse<String> response = httpClient.send(request, BodyHandlers.ofString());

            logger.info("Notificação de finalização enviada. Status: {}", response.statusCode());

        } catch (Exception e) {
            logger.error("Erro ao notificar finalização da sincronização: {}", e.getMessage(), e);
            throw new RuntimeException("Falha ao notificar finalização", e);
        }
    }

    private String buildUrl(String endpoint) {
        return String.format("http://%s:%d%s", orchestratorHost, ORCHESTRATOR_PORT, endpoint);
    }
}