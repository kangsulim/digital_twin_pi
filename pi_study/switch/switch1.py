import RPi.GPIO as gpio
from time import sleep

swPin = 13

gpio.setmode(gpio.BCM)
gpio.setup(swPin, gpio.IN, pull_up_down=gpio.PUD_DOWN)

try:
    while True:
        print(gpio.input(swPin))
        if gpio.input(swPin) == gpio.HIGH:
            print("HIGH")
        else:
            print("LOW")
        sleep(1)
except keyboardInterrupt:
    pass
finally:
    gpio.cleanup()