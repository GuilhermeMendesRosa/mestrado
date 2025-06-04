package br.com.udesc.orquestrator_database_synchonizer.orquestrator;

import br.com.udesc.orquestrator_database_synchonizer.orquestrator.dto.Worker;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.scheduling.annotation.Scheduled;
import org.springframework.stereotype.Component;

import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.util.Set;

@Component
public class SynchronizationScheduler {

    private final WorkersPool workersPool;

    private final HttpClient httpClient = HttpClient.newHttpClient();

    public static final int MINUTE = 60000;

    public SynchronizationScheduler(WorkersPool workersPool) {
        this.workersPool = workersPool;
    }

    @Scheduled(initialDelay = MINUTE, fixedRate = 2 * MINUTE)
    public void performSync() {
        try {
            Set<Worker> workers = workersPool.getWorkers();

            for (Worker worker : workers) {
                sendSignalToStartSync(worker);
            }

        } catch (Exception e) {
            System.err.println("Erro na sincronização: " + e.getMessage());
        }
    }

    private void sendSignalToStartSync(Worker worker) {
        try {
            String url = worker.host + ":8081/start-sync";
            System.out.println("Enviando requisição para: " + url);

            HttpRequest request = HttpRequest.newBuilder()
                    .uri(URI.create(url))
                    .GET()
                    .build();

            HttpResponse<String> response = httpClient.send(request, HttpResponse.BodyHandlers.ofString());
            System.out.println("Resposta do worker " + worker.host + ": " + response.body());
        } catch (Exception e) {
            System.err.println("Erro ao conectar com worker " + worker.host + ": " + e.getMessage());
        }
    }
}