import RPi.GPIO as gpio

class Led:

    def __init__(self, pin, number):
        self.pin = pin
        self.number = number
        gpio.setup(self.pin, gpio.OUT)
        gpio.output(self.pin, gpio.LOW)