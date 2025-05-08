import RPi.GPIO as gpio
from time import sleep


ledPin = (16, 20, 21)

gpio.setmode(gpio.BCM)
for pin in ledPin:
    gpio.setup(pin, gpio.OUT)



try:
    isOn = False
    while True:
        for pin in ledPin:
            if isOn:
                gpio.output(pin, gpio.LOW)
            else:
                gpio.output(pin, gpio.HIGH)
            sleep(0.1)
        isOn = not isOn
except keyboardInterrupt:
    pass
finally:
    gpio.cleanup()
