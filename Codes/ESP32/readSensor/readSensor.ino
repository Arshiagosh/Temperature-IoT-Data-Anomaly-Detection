#include <DHT.h>

#define DHTPIN  13

DHT dht(DHTPIN, DHT11);
void setup() {
  // put your setup code here, to run once:
  dht.begin();
  delay(2000);
  Serial.begin(115200);

}

void loop() {
  // put your main code here, to run repeatedly:
  float temp = dht.readTemperature();
  Serial.print("Temp: ");
  Serial.println(temp);
  delay(1000);
}
