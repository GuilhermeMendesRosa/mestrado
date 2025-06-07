package br.com.udesc.orchestrator_database_synchonizer.orchestrator;

import br.com.udesc.orchestrator_database_synchonizer.orchestrator.dto.WorkerDTO;
import org.springframework.stereotype.Component;

import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;

@Component
public class Connector {

    private final HttpClient httpClient = HttpClient.newHttpClient();

    public void sendSignalToStartSync(WorkerDTO workerDTO) {
        try {
            String url = "http://" +  workerDTO.host + ":8081/start-sync";
            System.out.println("Enviando requisição para: " + url);

            HttpRequest request = HttpRequest.newBuilder()
                    .uri(URI.create(url))
                    .GET()
                    .build();

            HttpResponse<String> response = httpClient.send(request, HttpResponse.BodyHandlers.ofString());
            System.out.println("Resposta do worker " + workerDTO.host + ": " + response.body());
        } catch (Exception e) {
            System.err.println("Erro ao conectar com worker " + workerDTO.host + ": " + e.getMessage());
        }
    }

}
