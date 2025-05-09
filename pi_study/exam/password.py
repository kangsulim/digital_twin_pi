import RPi.GPIO as gpio
from time import sleep
from threading import Thread

gpio.setmode(gpio.BCM)


class Led:

    def __init__(self, pin, number):
        self.pin = pin
        self.number = number
        gpio.setup(self.pin, gpio.OUT)
        gpio.output(self.pin, gpio.LOW)



class Button:

    def __init__(self, pin, onPressed):
        self.pin = pin
        self.prevState = gpio.LOW
        self.onPressed = onPressed
        gpio.setup(self.pin, gpio.IN, pull_up_down=gpio.PUD_DOWN)




leds = (Led(16, "Red"), Led(20, "Yellow"), Led(21, "Green"))

password = [1,2,3]

inputPassword = []

inputValue = gpio.HIGH

def button1():
    global inputPassword, inputValue
    if inputValue == gpio.input(buttons[0].pin):
        inputPassword.append(1)

def button2():
    global inputPasswordm, inputValue
    if inputValue == gpio.input(buttons[1].pin):
        inputPassword.append(2)

def button3():
    global inputPassword, inputValue
    if inputValue == gpio.input(buttons[2].pin):
        inputPassword.append(3)

def checkPassword():
    global inputPassword, password
    while len(inputPassword) < 3:
        button1()
        button2()
        button3()
        print(inputPassword)
        sleep(0.5)

    if inputPassword == password:
        rightPassword()
    else:
        wrongPassword()

def wrongPassword():
    for _ in range(3):
        for led in leds:
            gpio.output(led.pin, gpio.HIGH)
        sleep(0.5)
        for led in leds:
            gpio.output(led.pin, gpio.LOW)
        sleep(0.5)

def rightPassword():
    for _ in range(3):
        for led in leds:
            gpio.output(led.pin, gpio.HIGH)
            sleep(0.1)
            gpio.output(led.pin, gpio.LOW)
            sleep(0.1)

buttons = (Button(13, button1), Button(19, button2), Button(26, button3))

try:
    while True:
        checkPassword()
        print("프로그램을 종료하세요")
        sleep(1)
except KeyboardInterrupt:
    pass
finally:
    gpio.cleanup()