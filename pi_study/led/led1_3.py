import RPi.GPIO as gpio
from time import sleep

ledPin = (16, 20, 21)

# BCM	->	GPIO 핀 번호
# BOARD	->	BOARD 기판 번호
gpio.setmode(gpio.BCM)
gpio.setup(ledPin, gpio.OUT)

try:
    while True:
        number = int(input("mode(1/2/3): "))
        power = input("power(on/off): ")
        
        if power == "on":
            gpio.output(ledPin[number - 1], gpio.HIGH)
        elif power == "off":
            gpio.output(ledPin[number - 1], gpio.LOW)
except keyboardInterrupt:
    pass
finally:
    gpio.cleanup()

