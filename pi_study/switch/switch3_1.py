import RPi.GPIO as gpio
from time import sleep

swPin = (13, 19)

gpio.setmode(gpio.BCM)
gpio.setup(swPin, gpio.IN, pull_up_down=gpio.PUD_DOWN)



def check():
    i = 1
    for pin in swPin:
        if gpio.input(pin) == gpio.HIGH:
            print(f"PORT{i}: HIGH")            
            while gpio.input(pin) == gpio.HIGH:
                sleep(0.05)
        i += 1
    
try:
    while True:
        check()
except keyboardInterrupt:
    pass
finally:
     gpio.cleanup()
