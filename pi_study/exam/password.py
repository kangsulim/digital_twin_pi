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

inputValue1 = gpio.HIGH
inputValue2 = gpio.HIGH
inputValue3 = gpio.HIGH

def button1():
    global inputPassword, inputValue1
    if inputValue1 == gpio.input(buttons[0].pin) and inputValue1 == gpio.HIGH:
        inputPassword.append(1)
        inputValue1 = gpio.LOW
    elif gpio.input(buttons[0].pin) == gpio.LOW:
        inputValue1 = gpio.HIGH

def button2():
    global inputPasswordm, inputValue2
    if inputValue2 == gpio.input(buttons[1].pin) and inputValue2 == gpio.HIGH:
        inputPassword.append(2)
        inputValue2 = gpio.LOW
    elif gpio.input(buttons[1].pin) == gpio.LOW:
        inputValue2 = gpio.HIGH

def button3():
    global inputPassword, inputValue3
    if inputValue3 == gpio.input(buttons[2].pin) and inputValue3 == gpio.HIGH:
        inputPassword.append(3)
        inputValue3 = gpio.LOW
    elif gpio.input(buttons[2].pin) == gpio.LOW:
        inputValue3 = gpio.HIGH

def checkPassword():
    global inputPassword, password
    while len(inputPassword) < 3:
        button1()
        button2()
        button3()
        print(inputPassword)
        sleep(0.3)

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