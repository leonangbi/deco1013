from microbit import *
import neopixel
from random import randint
import music


display.scroll("READY!")
sleep(200)


"""
music.play(music)

"""
steps = 0
goal = 0
display.show(steps)
"""
red =
green = randint(0, 127)
blue = randint(156, 255)
"""
np = neopixel.NeoPixel(pin0, 30)

for pixel_id in range(0, len(np)):
        red = randint(250, 255)
        green = randint(0, 127)
        blue = randint(156, 255)
        np[pixel_id] = (red, green, blue)
        np.show()
while True:

    if button_b.was_pressed():
        goal += 10
        display.scroll("GOAL 20")
        sleep(2000)
    display.show(steps)
    if accelerometer.was_gesture('shake'):
        steps += 1
        display.show(steps, delay=0)
        if steps >= 1:
            np.clear()
            np.show()
    # assume the user finishes exercising
    if button_a.was_pressed():
        display.scroll(steps)
        sleep(1000)
        if steps >= 10:
            display.show(Image.FABULOUS)
            break
"""
np = neopixel.NeoPixel(pin0, 30)
while True:
    for pixel_id in range(0, len(np)):
        red = randint(250, 255)
        green = randint(0, 127)
        blue = randint(156, 255)
        np[pixel_id] = (red, green, blue)
        np.show()

        if steps >= 1:
        np.clear
        np.show

        """







