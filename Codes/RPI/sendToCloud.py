import random
import json
from paho.mqtt import client as mqtt_client
from bluepy import btle


broker = 'broker.emqx.io'
port = 1883
topic = "ArminArshia/Data"
password_encryption = 'Armin'  # Encryption password


def KSA(key):
    key_length = len(key)
    S = list(range(256))
    j = 0
    for i in range(256):
        j = (j + S[i] + key[i % key_length]) % 256
        S[i], S[j] = S[j], S[i]
    return S


def PRGA(S):
    i = 0
    j = 0
    while True:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        K = S[(S[i] + S[j]) % 256]
        yield K


def RC4(key, plaintext):
    S = KSA(key)
    keystream = PRGA(S)
    cipher = []
    for byte in plaintext:
        cipher_byte = byte ^ next(keystream)
        cipher.append(cipher_byte)
    return bytes(cipher)


class MyDelegate(btle.DefaultDelegate):
    def __init__(self):
        btle.DefaultDelegate.__init__(self)

    def handleNotification(self, cHandle, data):
        data_string = data.decode("utf-8")
        if data_string[6] == "n":
            print("Not a number")
        else:
            print(float(data_string[6:-2]))
            publish_mqtt(data_string[6:-2])


def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(f'publish-{random.randint(0, 1000)}')
    client.on_connect = on_connect
    client.connect(broker, port, keepalive=3)
    return client


client = connect_mqtt()
client.loop_start()


def publish_mqtt(data):
    global client
    msg = json.dumps({"temp": float(data)})
    print(msg)
    pub_msg = RC4(password_encryption.encode(), msg.encode())
    result = client.publish(topic, pub_msg, qos=0, retain=False)
    status = result[0]
    if status == 0:
        print(f"Send `{pub_msg}` to topic `{topic}`")
    else:
        print(f"Failed to send message to topic {topic}")


p = btle.Peripheral("b0:b2:1c:97:67:12")
p.setDelegate(MyDelegate())

svc = p.getServiceByUUID("6E400001-B5A3-F393-E0A9-E50E24DCCA9E")
ch = svc.getCharacteristics("6E400003-B5A3-F393-E0A9-E50E24DCCA9E")[0]
setup_data = b"\x01\00"
p.writeCharacteristic(ch.valHandle + 1, setup_data)

while True:
    if p.waitForNotifications(0.25):
        continue
    print("Waiting...")