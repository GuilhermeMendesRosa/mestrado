package br.com.roselabs.monitoramente_nivel_agua_web.coap;

import br.com.roselabs.monitoramente_nivel_agua_web.water_level.WaterLevelController;
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
        public void handlePOST(CoapExchange exchange) {
            String content = exchange.getRequestText();
            System.out.println("Recebido: " + content);

            exchange.respond(ResponseCode.CREATED, "Dados recebidos com sucesso");
        }
    }
}