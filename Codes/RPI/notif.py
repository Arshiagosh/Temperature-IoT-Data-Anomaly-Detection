from bluepy import btle


class MyDelegate(btle.DefaultDelegate):
    def __init__(self):
        btle.DefaultDelegate.__init__(self)
        # ... initialise here

    def handleNotification(self, cHandle, data):
        #print("\n- handleNotification -\n")
        dataString = data.decode("utf-8")
        if dataString[6] == "n":
            print("Not a number")
        else:
            print(float(dataString[6:-2]))
        # ... perhaps check cHandle
        # ... process 'data'


# Initialisation  -------

p = btle.Peripheral("b0:b2:1c:97:67:12")
p.setDelegate(MyDelegate())

# Setup to turn notifications on, e.g.
svc = p.getServiceByUUID("6E400001-B5A3-F393-E0A9-E50E24DCCA9E")
ch = svc.getCharacteristics("6E400003-B5A3-F393-E0A9-E50E24DCCA9E")[0]
#   ch.write( setup_data )

setup_data = b"\x01\00"
p.writeCharacteristic(ch.valHandle+1, setup_data)

# Main loop --------

while True:
    if p.waitForNotifications(1.0):
        # handleNotification() was called
        continue

    print("Waiting...")
    # Perhaps do something else here
