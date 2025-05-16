#include <ESP32Servo.h>

Servo myServo;
int servoPin = 21;

void setup() {
  // Inicializa o servo
  myServo.attach(servoPin);
  myServo.write(90);  // Posição inicial: centro
  delay(1000);        // Aguarda 1 segundo para estabilizar
}

void loop() {
  // Move para 0 graus
  myServo.write(0);
  delay(5000);  // Aguarda 5 segundos
  
  // Move para 180 graus
  myServo.write(180);
  delay(5000);  // Aguarda 5 segundos
}