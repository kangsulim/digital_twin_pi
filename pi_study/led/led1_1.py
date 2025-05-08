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
        mode = input("""
    숫자를 입력하시오.
    1. red on
    2. red off
    3. yellow on
    4. yellow off
    5. green on
    6. green off

    """)
        if mode == "1":
            gpio.output(ledPinRed, gpio.HIGH)
        elif mode == "2":
            gpio.output(ledPinRed, gpio.LOW)
        elif mode == "3":
            gpio.output(ledPinYellow, gpio.HIGH)
        elif mode == "4":
            gpio.output(ledPinYellow, gpio.LOW)
        elif mode == "5":
            gpio.output(ledPinGreen, gpio.HIGH)
        elif mode == "6":
            gpio.output(ledPinGreen, gpio.LOW)
except keyboardInterrupt:
    pass
finally:
    gpio.cleanup()