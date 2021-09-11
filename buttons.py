from microbit import *

while True:
    if button_a.was_pressed():
        sleep(500)
        if button_b.was_pressed():
            display.scroll("C")
        else:
            display.scroll("A")
    if button_b.was_pressed():
        sleep(500)
        if button_a.was_pressed():
            display.scroll("C")
        else:
            display.scroll("B")
