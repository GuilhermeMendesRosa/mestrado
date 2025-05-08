const int pinoSensor = 32;  // Substitua pelo pino que você está usando
const int pinoLED = 2;      // LED embutido do ESP32 (opcional para teste)

void setup() {
  pinMode(pinoSensor, INPUT_PULLUP);  // Configura com resistor pull-up interno
  pinMode(pinoLED, OUTPUT);
  Serial.begin(9600);
  Serial.println("Iniciando leitura do sensor de boia...");
}

void loop() {
  int estadoBoia = digitalRead(pinoSensor);
  
  Serial.print("Estado do sensor: ");
  Serial.println(estadoBoia);
  
  // Acende o LED quando o sensor for ativado
  digitalWrite(pinoLED, !estadoBoia);  // Lógica invertida com pull-up
  
  delay(500);
}