#include <BLEDevice.h> 
#include <BLEServer.h> 
#include <BLEUtils.h> 
#include <BLE2902.h> 
#include <DHT.h> 
 
#define SERVICE_UUID           "6E400001-B5A3-F393-E0A9-E50E24DCCA9E" // UART service UUID
#define CHARACTERISTIC_UUID_RX "6E400002-B5A3-F393-E0A9-E50E24DCCA9E"
#define CHARACTERISTIC_UUID_TX "6E400003-B5A3-F393-E0A9-E50E24DCCA9E"

#define bleServerName       "ArshiaAndArminServer" 
 
#define DHT_PIN 13    // Pin to which DHT11/DHT22 data pin is connected 
#define DHT_TYPE DHT11 // Change to DHT22 if you are using DHT22 sensor 
 
BLEServer* pServer = NULL; 
BLECharacteristic* pTxCharacteristic = NULL; 
bool deviceConnected = false;
bool oldDeviceConnected = false;

DHT dht(DHT_PIN, DHT_TYPE); 

class MyServerCallbacks: public BLEServerCallbacks {
    void onConnect(BLEServer* pServer) {
      deviceConnected = true;
    };

    void onDisconnect(BLEServer* pServer) {
      deviceConnected = false;
    }
};

class MyCallbacks: public BLECharacteristicCallbacks {
    void onWrite(BLECharacteristic *pCharacteristic) {
      std::string rxValue = pCharacteristic->getValue();

      if (rxValue.length() > 0) {
        Serial.println("*********");
        Serial.print("Received Value: ");
        for (int i = 0; i < rxValue.length(); i++)
          Serial.print(rxValue[i]);

        Serial.println();
        Serial.println("*********");
      }
    }
};

void setup() { 
  Serial.begin(115200); 
  BLEDevice::init(bleServerName); 
  pServer = BLEDevice::createServer(); 
  pServer->setCallbacks(new MyServerCallbacks());
  BLEService *pService = pServer->createService(SERVICE_UUID); 
  pTxCharacteristic = pService->createCharacteristic(
										CHARACTERISTIC_UUID_TX,
										BLECharacteristic::PROPERTY_NOTIFY
									);
                  
  pTxCharacteristic->addDescriptor(new BLE2902());

  BLECharacteristic * pRxCharacteristic = pService->createCharacteristic(
											 CHARACTERISTIC_UUID_RX,
											BLECharacteristic::PROPERTY_WRITE
										);

  pRxCharacteristic->setCallbacks(new MyCallbacks());

  pService->start(); 
  pServer->getAdvertising()->start();
  Serial.println("Waiting a client connection to notify...");
 
  dht.begin(); 
  delay(2000);
} 
 
void loop() { 
  float temperature = dht.readTemperature(); 
  float humidity = dht.readHumidity(); 
 
  Serial.print("Temperature (C): "); 
  Serial.println(temperature); 
  Serial.print("Humidity (%): "); 
  Serial.println(humidity); 
 
  // Create a string with temperature and humidity values 
  String sensorData = "Temp: " + String(temperature) + "C"; 

  // Handle Bluetooth communication
  if (deviceConnected) {
    pTxCharacteristic->setValue(sensorData.c_str());
    pTxCharacteristic->notify();
    delay(500); // bluetooth stack will go into congestion if too many packets are sent
  }
  
  // Handle disconnecting
  if (!deviceConnected && oldDeviceConnected) {
    delay(1000); // give the bluetooth stack the chance to get things ready
    pServer->startAdvertising(); // restart advertising
    Serial.println("start advertising");
    oldDeviceConnected = deviceConnected;
  }

  // Handle connecting
  if (deviceConnected && !oldDeviceConnected) {
    // do stuff here on connecting
    oldDeviceConnected = deviceConnected;
  } 
}
