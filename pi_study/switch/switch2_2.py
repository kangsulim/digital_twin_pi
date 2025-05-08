import RPi.GPIO as gpio
from time import sleep

swPin = 13

gpio.setmode(gpio.BCM)
gpio.setup(swPin, gpio.IN, pull_up_down=gpio.PUD_DOWN)

prev = gpio.LOW

try:
    while True:
        state = gpio.input(swPin)
        if prev == gpio.LOW and state == gpio.HIGH:
            print("HIGH")
        prev = state
        sleep(0.05)
except keyboardInterrupt:
    pass
finally:
    gpio.cleanup()