import RPi.GPIO as gpio
from time import sleep

ledPinRed = 16
ledPinYellow = 20
ledPinGreen = 21

# BCM	->	GPIO 핀 번호
# BOARD	->	BOARD 기판 번호
gpio.setmode(gpio.BCM)
gpio.setup(ledPinRed, gpio.OUT)
gpio.setup(ledPinYellow, gpio.OUT)
gpio.setup(ledPinGreen, gpio.OUT)

try:
    while True:
        mode = input("mode(1/2/3): ")
        power = input("power(on/off): ")
        
        if mode == "1":
            if power == "on":
                gpio.output(ledPinRed, gpio.HIGH)
            elif power == "off":
                gpio.output(ledPinRed, gpio.LOW)
        elif mode == "2":
            if power == "on":
                gpio.output(ledPinYellow, gpio.HIGH)
            elif power == "off":
                gpio.output(ledPinYellow, gpio.LOW)
        elif mode == "3":
            if power == "on":
                gpio.output(ledPinGreen, gpio.HIGH)
            elif power == "off":
                gpio.output(ledPinGreen, gpio.LOW)
except keyboardInterrupt:
    pass
finally:
    gpio.cleanup()
