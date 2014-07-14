import time

def open_outer_door():
    import RPi.GPIO as GPIO
    
    GPIO.setmode(GPIO.BCM)

    pin = 0

    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.HIGH)

    GPIO.output(pin, GPIO.LOW)
    time.sleep(0.5)
    GPIO.output(pin, GPIO.HIGH)

    return True


def open_inner_door():
    import RPi.GPIO as GPIO

    GPIO.setmode(GPIO.BCM)

    pin = 1

    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.HIGH)

    GPIO.output(pin, GPIO.LOW)
    time.sleep(0.5)
    GPIO.output(pin, GPIO.HIGH)

    return True
