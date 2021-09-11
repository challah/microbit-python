from microbit import *

while True:
    if pin0.is_touched():
        display.show(Image.HAPPY)
    if pin1.is_touched():
        display.show(Image.GIRAFFE)
    if pin2.is_touched():
        display.show(Image.FABULOUS)
    else:
        display.show(Image.ASLEEP)
