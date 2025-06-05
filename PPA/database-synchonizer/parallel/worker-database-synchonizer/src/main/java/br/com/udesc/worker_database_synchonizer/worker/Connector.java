package br.com.udesc.worker_database_synchonizer.worker;

import br.com.udesc.worker_database_synchonizer.dto.TableDTO;
import br.com.udesc.worker_database_synchonizer.dto.WorkerDTO;
import com.fasterxml.jackson.databind.ObjectMapper;
import jakarta.annotation.PostConstruct;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Component;

import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;

import static java.net.http.HttpResponse.BodyHandlers;

@Component
public class Connector {

    @Value("${orchestrator.host}")
    private String orchestratorHost;

    private final HttpClient httpClient = HttpClient.newHttpClient();
    private final ObjectMapper objectMapper = new ObjectMapper();

    @PostConstruct
    public void connectToOrchestrator() {
        WorkerDTO me = new WorkerDTO("localhost");
        try {
            String url = "http://" + orchestratorHost + ":8080/connect";
            System.out.println("Enviando requisição para: " + url);

            String workerJson = objectMapper.writeValueAsString(me);

            HttpRequest request = HttpRequest.newBuilder()
                    .uri(URI.create(url))
                    .header("Content-Type", "application/json")
                    .POST(HttpRequest.BodyPublishers.ofString(workerJson))
                    .build();

            HttpResponse<String> response = httpClient.send(request, BodyHandlers.ofString());
            System.out.println("Resposta do worker " + orchestratorHost + ": " + response.body());
        } catch (Exception e) {
            System.err.println("Erro ao conectar com worker " + orchestratorHost + ": " + e.getMessage());
        }
    }

    public TableDTO nextTable() {
        try {
            String url = "http://" + orchestratorHost + ":8080/next-table";
            System.out.println("Requisitando próxima tabela de: " + url);

            HttpRequest request = HttpRequest.newBuilder()
                    .uri(URI.create(url))
                    .header("Content-Type", "application/json")
                    .GET()
                    .build();

            HttpResponse<String> response = httpClient.send(request, BodyHandlers.ofString());

            if (response.statusCode() == 200) {
                TableDTO tableDTO = objectMapper.readValue(response.body(), TableDTO.class);
                System.out.println("Tabela recebida: " + tableDTO);
                return tableDTO;
            } else {
                System.err.println("Erro na requisição. Status: " + response.statusCode() + ", Body: " + response.body());
                return null;
            }
        } catch (Exception e) {
            System.err.println("Erro ao requisitar próxima tabela: " + e.getMessage());
            return null;
        }
    }

    public void synchronizationFinished() {
        try {
            String url = "http://" + orchestratorHost + ":8080/finish";
            System.out.println("Requisitando próxima tabela de: " + url);

            HttpRequest request = HttpRequest.newBuilder()
                    .uri(URI.create(url))
                    .header("Content-Type", "application/json")
                    .GET()
                    .build();

            HttpResponse<String> response = httpClient.send(request, BodyHandlers.ofString());

        } catch (Exception e) {
            throw new RuntimeException(e);
        }
    }
}