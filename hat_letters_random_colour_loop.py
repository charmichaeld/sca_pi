#!/usr/bin/env python
from sense_hat import SenseHat
import time
import random
sense = SenseHat()

for i, c in enumerate('Howdy'):
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)

    sense.show_letter(c, (r, g, b))
    print "Random number r=", r, " g=", g, " b=", b
    time.sleep(0.25)

sense.clear()
