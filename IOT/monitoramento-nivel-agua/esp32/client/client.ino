#include <WiFi.h>
#include <WiFiUdp.h>
#include <coap-simple.h>

// Configurações da rede WiFi
const char* ssid = "REDE_WIFI";
const char* password = "SENHA_WIFI";

// Servidor CoAP
IPAddress servidorIP(192, 168, 0, 200);
int servidorPorta = 5683; // Porta padrão CoAP

// Instâncias UDP e CoAP
WiFiUDP udp;
Coap coap(udp);

// Callback para respostas
void handleResponse(CoapPacket &packet, IPAddress ip, int port) {
  char payload[packet.payloadlen + 1];
  memcpy(payload, packet.payload, packet.payloadlen);
  payload[packet.payloadlen] = '\0';
  
  Serial.printf("Resposta do servidor: %s\n", payload);
}

void setup() {
  Serial.begin(115200);
  delay(1000);

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

  // Inicia UDP (porta local aleatória)
  udp.begin(WiFi.localIP(), 0);
  
  // Registra callback para respostas
  coap.response(handleResponse);
  
  Serial.println("Cliente CoAP pronto");
}

void loop() {
  // Processa mensagens CoAP
  coap.loop();
  
  // Mensagem a ser enviada
  String mensagem = "Olá, servidor!";
  Serial.printf("\nEnviando mensagem para %s:%d: %s\n", servidorIP.toString().c_str(), servidorPorta, mensagem.c_str());
  
  // Envia requisição PUT para o recurso "message"
  // Usando a versão correta do método put()
  int messageID = coap.put(servidorIP, servidorPorta, "message", mensagem.c_str(), mensagem.length());
  Serial.printf("Mensagem CoAP enviada com ID: %d\n", messageID);
  
  // Espera resposta
  for (int i = 0; i < 10; i++) {
    coap.loop();
    delay(50);
  }
  
  delay(2000); // Aguarda 2 segundos para o próximo envio
}