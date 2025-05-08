import RPi.GPIO as gpio
from time import sleep

ledPin = (16, 21)

gpio.setmode(gpio.BCM)
for pin in ledPin:
    gpio.setup(pin, gpio.OUT)
    gpio.output(pin, gpio.LOW)

currentPassword = None

while True:
    password = input("new password: ")
    confirm = input("confirm password: ")
        
    if confirm != password:
        print("비밀번호가 일치하지 않습니다.")
    else:
        print("비밀번호가 설정되었습니다.")
        currentPassword = password
        break
    
try:
    while True:
        login = input("login password: ")
        
        if login != currentPassword:
            for i in range(5):
                gpio.output(ledPin[0], gpio.HIGH)
                sleep(0.1)
                gpio.output(ledPin[0], gpio.LOW)
                sleep(0.1)
        else:
            gpio.output(ledPin[1], gpio.HIGH)
            sleep(2)
            break
except keyboardInterrupt:
    pass
finally:
    gpio.cleanup()











        