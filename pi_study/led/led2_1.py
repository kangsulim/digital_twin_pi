import RPi.GPIO as gpio
from time import sleep


ledPin = (16, 20, 21)

gpio.setmode(gpio.BCM)
for pin in ledPin:
    gpio.setup(pin, gpio.OUT)

i = 1

try:
    while True:
        i += 1
        gpio.output(ledPin[i % 3], gpio.HIGH)
        sleep(0.1)
        gpio.output(ledPin[i % 3], gpio.LOW)
        sleep(0.1)
except keyboardInterrupt:
    pass
finally:
    gpio.cleanup()