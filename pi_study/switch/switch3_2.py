import RPi.GPIO as gpio
from time import sleep

swPin = (13, 19)
prev = []

gpio.setmode(gpio.BCM)
gpio.setup(swPin, gpio.IN, pull_up_down=gpio.PUD_DOWN)

def check():
    while True:
        i = 0
        for pin in swPin:
            if i == len(prev):
                prev.append(gpio.LOW)
            if gpio.input(pin) == prev[i] and gpio.input(pin) == gpio.HIGH:
                print(f"PORT{i + 1}: HIGH")  
                prev[i] = gpio.LOW
            elif gpio.input(pin) == gpio.LOW:
                prev[i] = gpio.HIGH
            i += 1
            sleep(0.05)

try:
    check()
except keyboardInterrupt:
    pass
finally:
    gpio.cleanup()