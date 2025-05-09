import RPi.GPIO as gpio

class Button:

    def __init__(self, pin, onPressed):
        self.pin = pin
        self.prevState = gpio.LOW
        self.onPressed = onPressed
        gpio.setup(self.pin, gpio.IN, pull_up_down=gpio.PUD_DOWN)

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