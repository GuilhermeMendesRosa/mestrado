#include <WiFi.h>
#include <WiFiUdp.h>
#include <coap-simple.h>

// Configurações da rede WiFi
const char* ssid = "REDE_WIFI";
const char* password = "SENHA_WIFI";

// Configuração do IP fixo
IPAddress local_IP(192, 168, 0, 200);
IPAddress gateway(192, 168, 0, 1);
IPAddress subnet(255, 255, 255, 0);

// Instâncias UDP e CoAP
WiFiUDP udp;
Coap coap(udp);

// Callback para requisições CoAP
void handleMessage(CoapPacket &packet, IPAddress ip, int port) {
  char payload[packet.payloadlen + 1];
  memcpy(payload, packet.payload, packet.payloadlen);
  payload[packet.payloadlen] = '\0';
  
  Serial.printf("\nRecebido pacote CoAP de %s, tamanho: %d\n", ip.toString().c_str(), packet.payloadlen);
  Serial.printf("Conteúdo: %s\n", payload);
  
  // Responde ao cliente
  String resposta = "Recebido: ";
  resposta += payload;
  coap.sendResponse(ip, port, packet.messageid, resposta.c_str(), resposta.length());
  Serial.println("Resposta enviada ao cliente.");
}

void setup() {
  Serial.begin(115200);
  delay(1000);

  // Configura IP fixo
  if (!WiFi.config(local_IP, gateway, subnet)) {
    Serial.println("Falha ao configurar IP fixo");
  } else {
    Serial.println("IP fixo configurado com sucesso");
  }

  // Conecta ao WiFi
  Serial.printf("Conectando-se à rede %s\n", ssid);
  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("\nWiFi conectado!");
  Serial.print("Endereço IP: ");
  Serial.println(WiFi.localIP());

  // Inicia UDP na porta padrão CoAP (5683)
  udp.begin(5683);
  
  // Registra o recurso "message" no servidor CoAP
  coap.server(handleMessage, "message");
  
  Serial.println("Servidor CoAP iniciado na porta 5683");
}

void loop() {
  coap.loop();
  delay(10);
}