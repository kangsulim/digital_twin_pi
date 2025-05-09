

if __name__ == '__main__':
    try:
        while True:
            checkPassword()
            print("프로그램을 종료하세요")
            sleep(1)
    except KeyboardInterrupt:
        pass
    finally:
        gpio.cleanup()