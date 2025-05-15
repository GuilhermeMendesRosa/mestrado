package br.com.roselabs.monitoramente_nivel_agua_backend.coap;

import jakarta.annotation.PostConstruct;
import jakarta.annotation.PreDestroy;
import org.eclipse.californium.core.CoapResource;
import org.eclipse.californium.core.CoapServer;
import org.eclipse.californium.core.server.resources.CoapExchange;
import org.eclipse.californium.core.coap.CoAP.ResponseCode;
import org.eclipse.californium.elements.config.Configuration;
import org.springframework.stereotype.Component;

@Component
public class CoAPService {

    private CoapServer server;

    @PostConstruct
    public void startServer() {
        Configuration config = Configuration.createStandardWithoutFile();

        server = new CoapServer(config);

        server.add(new WaterLevelResource());

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

        public WaterLevelResource() {
            super("hello");
        }

        @Override
        public void handleGET(CoapExchange exchange) {
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