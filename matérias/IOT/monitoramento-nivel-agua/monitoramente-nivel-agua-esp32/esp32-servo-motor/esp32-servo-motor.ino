#include <WiFi.h>
#include <WiFiUdp.h>
#include <coap-simple.h>
#include <ESP32Servo.h>

// Configurações da rede WiFi
const char* ssid = "REDE_WIFI";
const char* password = "SENHA_WIFI";

// Configuração do IP fixo
IPAddress local_IP(192, 168, 0, 200);
IPAddress gateway(192, 168, 0, 1);
IPAddress subnet(255, 255, 255, 0);

// Configuração do servo
Servo myServo;
int servoPin = 21;
int posicaoValvulaAberta = 180;
int posicaoValvulaFechada = 0;

// Instâncias UDP e CoAP
WiFiUDP udp;
Coap coap(udp);

// Callback para requisições CoAP
void handleMessage(CoapPacket &packet, IPAddress ip, int port) {
  char payload[packet.payloadlen + 1];
  memcpy(payload, packet.payload, packet.payloadlen);
  payload[packet.payloadlen] = '\0';
  
  Serial.printf("Recebido: %s de %s\n", payload, ip.toString().c_str());
  
  // Responde ao cliente
  String resposta = "Recebido: ";
  resposta += payload;
  coap.sendResponse(ip, port, packet.messageid, resposta.c_str(), resposta.length());
  
  // Processa comando para o servo
  String mensagem = String(payload);
  if (mensagem.startsWith("estado_boia:")) {
    int estadoBoia = mensagem.substring(12).toInt();
    
    if (estadoBoia == 0) {
      Serial.println("Boia submersa - Fechando válvula");
      myServo.write(posicaoValvulaFechada);
    } else {
      Serial.println("Boia não submersa - Abrindo válvula");
      myServo.write(posicaoValvulaAberta);
    }
  }
}

void setup() {
  Serial.begin(115200);
  
  // Inicializa o servo
  myServo.attach(servoPin);
  myServo.write(posicaoValvulaFechada);
  delay(1000);
  
  // Configura IP fixo
  if (!WiFi.config(local_IP, gateway, subnet)) {
    Serial.println("Falha ao configurar IP fixo");
  }

  // Conecta ao WiFi
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("\nWiFi conectado: " + WiFi.localIP().toString());

  // Inicia UDP e registra handler
  udp.begin(5683);
  coap.server(handleMessage, "message");
  Serial.println("Servidor CoAP iniciado");
}

void loop() {
  coap.loop();
  delay(10);
}