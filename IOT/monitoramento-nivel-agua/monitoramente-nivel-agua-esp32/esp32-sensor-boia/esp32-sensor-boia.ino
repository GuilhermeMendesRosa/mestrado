#include <WiFi.h>
#include <WiFiUdp.h>
#include <coap-simple.h>

// Configurações da rede WiFi
const char* ssid = "REDE_WIFI";
const char* password = "SENHA_WIFI";

// Servidor CoAP original
IPAddress servidorIP(192, 168, 0, 200);
int servidorPorta = 5683;

// Servidor Spring Boot
IPAddress springIP(192, 168, 0, 123);
int springPorta = 5683;
const char* springResource = "water-level";

// Configuração do sensor de boia
const int pinoSensor = 32;
const int pinoLED = 2;
int estadoAnteriorBoia = -1;

// Instâncias UDP e CoAP
WiFiUDP udp;
Coap coap(udp);

// Callback para respostas
void handleResponse(CoapPacket &packet, IPAddress ip, int port) {
  char payload[packet.payloadlen + 1];
  memcpy(payload, packet.payload, packet.payloadlen);
  payload[packet.payloadlen] = '\0';
  
  Serial.printf("Resposta de %s:%d: %s\n", ip.toString().c_str(), port, payload);
}

void setup() {
  pinMode(pinoSensor, INPUT_PULLUP);
  pinMode(pinoLED, OUTPUT);
  Serial.begin(115200);
  
  Serial.println("Iniciando sistema de monitoramento da boia com CoAP...");

  // Conecta ao WiFi
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("\nWiFi conectado!");
  Serial.println(WiFi.localIP());

  udp.begin(WiFi.localIP(), 0);
  coap.response(handleResponse);
}

void loop() {
  coap.loop();
  
  // Lê o estado atual da boia
  int estadoBoia = digitalRead(pinoSensor);
  digitalWrite(pinoLED, !estadoBoia);
  
  // Envia dados apenas quando houver mudança
  if (estadoBoia != estadoAnteriorBoia) {
    estadoAnteriorBoia = estadoBoia;
    
    // Envio para servidor original
    String mensagem = "estado_boia:" + String(estadoBoia);
    Serial.printf("Enviando para servidor original: %s\n", mensagem.c_str());
    coap.put(servidorIP, servidorPorta, "message", mensagem.c_str(), mensagem.length());
    
    // Processa algumas respostas
    for (int i = 0; i < 5; i++) {
      coap.loop();
      delay(50);
    }
    
    // Converte o estado para o formato esperado pelo WaterLevel
    // LÓGICA INVERTIDA: estadoBoia == 0 agora significa tanque cheio
    bool nivelBaixo = (estadoBoia == 0);
    
    // Cria string JSON simples manualmente
    String jsonStr = "{\"lowLevel\":" + String(nivelBaixo ? "true" : "false") + "}";
    
    Serial.printf("Enviando para Spring Boot: %s\n", jsonStr.c_str());
    
    // Usando put em vez de post, já que a biblioteca coap-simple não tem o método post
    coap.put(springIP, springPorta, springResource, jsonStr.c_str(), jsonStr.length());
    
    // Processa respostas
    for (int i = 0; i < 5; i++) {
      coap.loop();
      delay(50);
    }
  }
  
  delay(500);
}