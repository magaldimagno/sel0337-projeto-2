#include <Wire.h>
#define i2c_addr 0x08
#define pot_addr A0

int valorlido = 0;

void setup() {
  Serial.begin(9600);
  pinMode(pot_addr, INPUT);
  Wire.begin(i2c_addr);
  Wire.onRequest(enviarDados);
}

void loop() {
  valorlido = analogRead(pot_addr);
  delay(100);
}

void enviarDados(int numBytes) {
  byte buffer[2];
  buffer[0] = highByte(valorlido);
  buffer[1] = lowByte(valorlido);

  Wire.write(buffer,2);

  Serial.print("Valor enviado: ");
  Serial.println(valorlido);
}