from microbit import *
import random

while True:
    if accelerometer.was_gesture("shake"):
        for i in range(100):
            x = random.randint(0, 4)
            y = random.randint(0, 4)
            bright = random.randint(1, 9)
            display.set_pixel(x, y, bright)
            sleep(10)
        display.clear()
