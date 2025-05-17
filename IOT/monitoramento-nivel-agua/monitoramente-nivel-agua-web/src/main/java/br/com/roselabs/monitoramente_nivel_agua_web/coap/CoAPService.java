package br.com.roselabs.monitoramente_nivel_agua_web.coap;

import br.com.roselabs.monitoramente_nivel_agua_web.water_level.WaterLevel;
import br.com.roselabs.monitoramente_nivel_agua_web.water_level.WaterLevelController;
import com.fasterxml.jackson.databind.ObjectMapper;
import jakarta.annotation.PostConstruct;
import jakarta.annotation.PreDestroy;
import org.eclipse.californium.core.CoapResource;
import org.eclipse.californium.core.CoapServer;
import org.eclipse.californium.core.server.resources.CoapExchange;
import org.eclipse.californium.core.coap.CoAP.ResponseCode;
import org.eclipse.californium.elements.config.Configuration;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;

@Component
public class CoAPService {

    @Autowired
    private WaterLevelController waterLevelController;

    private CoapServer server;

    @PostConstruct
    public void startServer() {
        Configuration config = Configuration.createStandardWithoutFile();

        server = new CoapServer(config);

        server.add(new WaterLevelResource(waterLevelController));

        server.start();

        System.out.println("Servidor CoAP iniciado na porta 5683");
    }

    @PreDestroy
    public void stopServer() {
        if (server != null) {
            server.stop();
            System.out.println("Servidor CoAP parado");
        }
    }

    static class WaterLevelResource extends CoapResource {
        private final WaterLevelController waterLevelController;

        public WaterLevelResource(WaterLevelController waterLevelController) {
            super("water-level");
            this.waterLevelController = waterLevelController;
        }

        @Override
        public void handleGET(CoapExchange exchange) {
            waterLevelController.toggleWaterLevel();
            exchange.respond(ResponseCode.CONTENT, "Olá do servidor CoAP!");
        }

        @Override
        public void handlePUT(CoapExchange exchange) {
            String content = exchange.getRequestText();
            System.out.println("Recebido: " + content);

            try {
                // Usar ObjectMapper para deserializar o JSON
                ObjectMapper objectMapper = new ObjectMapper();
                WaterLevel receivedWaterLevel = objectMapper.readValue(content, WaterLevel.class);

                // Atualizar o nível de água
                waterLevelController.setWaterLevel(receivedWaterLevel);

                exchange.respond(ResponseCode.CREATED, "Dados processados com sucesso");
            } catch (Exception e) {
                System.err.println("Erro ao processar JSON: " + e.getMessage());
                exchange.respond(ResponseCode.BAD_REQUEST, "Erro: " + e.getMessage());
            }
        }
    }
}