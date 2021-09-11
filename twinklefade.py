from microbit import *
import random

def twinkle(amount):
    for i in range(amount):
        x = random.randint(0, 4)
        y = random.randint(0, 4)
        bright = random.randint(0, 9)
        display.set_pixel(x, y, bright)
        sleep(80)

def fadeout():
    while True:
        for b in range(0, 10):
            for x in range(0, 5):
                for y in range(0, 5):
                    bright = display.get_pixel(x, y)
                    if bright > 0:
                        display.set_pixel(x, y, bright - 1)
            sleep(100)  # pause after each brightness change
        break  # stop the loop

while True:
    if accelerometer.was_gesture("shake"):
        display.clear()
        twinkle(20)
        fadeout()
