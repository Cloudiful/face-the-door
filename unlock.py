import RPi.GPIO as GPIO
import time

import data
import ui


def unlock_door():
    ui.clear_screen()

    servoPIN = 17
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(servoPIN, GPIO.OUT)

    p = GPIO.PWM(servoPIN, 50)  # GPIO 17 端口用作50hz的PWM
    p.start(7.5)
    time.sleep(1)

    p.ChangeDutyCycle(2.5)  # 顺时针旋转90度
    # print("已解锁房门。")
    ui.Title("已解锁，请在五秒内进入。", data.WIDTH // 2, data.HEIGHT // 2, 48)
    ui.draw_screen()
    time.sleep(5)

    p.ChangeDutyCycle(7.5)  # 五秒后回中
    time.sleep(1)

    ui.clear_screen()

    p.stop()
    GPIO.cleanup()
