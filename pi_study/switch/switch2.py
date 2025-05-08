import RPi.GPIO as gpio
from time import sleep

swPin = 13

gpio.setmode(gpio.BCM)
gpio.setup(swPin, gpio.IN, pull_up_down=gpio.PUD_DOWN)

prev =gpio.LOW

try:
    while True:
        if gpio.input(swPin) == prev and gpio.input(swPin) == gpio.HIGH:
            print("HIGH")
            prev = gpio.LOW
        elif gpio.input(swPin) == gpio.LOW:
            prev = gpio.HIGH
        
        sleep(0.05)
except keyboardInterrupt:
    pass
finally:
    gpio.cleanup()