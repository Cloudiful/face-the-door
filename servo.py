import time

import RPi.GPIO as GPIO


def unlock():

    servoPIN = 17
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(servoPIN, GPIO.OUT)

    p = GPIO.PWM(servoPIN, 50)  # GPIO 17 端口用作50hz的PWM
    p.start(7.5)
    time.sleep(1)

    p.ChangeDutyCycle(2.5)  # 顺时针旋转90度
    print("已解锁房门。")

    time.sleep(5)

    p.ChangeDutyCycle(7.5)  # 五秒后回中
    time.sleep(1)

    p.stop()
    GPIO.cleanup()
