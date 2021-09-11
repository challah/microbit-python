from microbit import *

while True:
    if button_a.was_pressed():
        display.scroll(str(temperature()) + " C")
    if button_b.was_pressed():
        degreesF = int(temperature() * (9 / 5) + 32)
        display.scroll(str(degreesF) + " F")
