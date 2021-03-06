import time
from settings import TIMED_DELAY


def open_door(pin_num, sleep_time):
    import RPi.GPIO as GPIO
    time.sleep(TIMED_DELAY)
    GPIO.setmode(GPIO.BCM)

    GPIO.setup(pin_num, GPIO.OUT)
    GPIO.output(pin_num, GPIO.HIGH)

    GPIO.output(pin_num, GPIO.LOW)
    time.sleep(sleep_time)
    GPIO.output(pin_num, GPIO.HIGH)

    return True
