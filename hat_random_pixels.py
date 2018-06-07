#!/usr/bin/env python
from sense_hat import SenseHat
sense = SenseHat()
import time
import random

x = random.randint(0,7)
y = random.randint(0,7)

sense.set_pixel(x, y, (0, 0, 255))
time.sleep(0.5)

sense.clear()
