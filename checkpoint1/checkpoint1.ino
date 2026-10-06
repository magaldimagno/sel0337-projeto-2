#include <Wire.h>
#define i2c_addr 0x08

void setup() {
  pinMode(LED_BUILTIN, OUTPUT);
  Wire.begin(i2c_addr);
  Wire.onReceive(receberDados);
}

void loop() {
  delay(100);
}

void receberDados(int numBytes) {
  while(Wire.available()){
    int comando = Wire.read();
    if (comando == 1) {
      digitalWrite(LED_BUILTIN, HIGH);
    } else if (comando == 0) {
      digitalWrite(LED_BUILTIN, LOW);
    } 
  }
}