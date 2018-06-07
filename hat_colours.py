#!/usr/bin/env python
from sense_hat import SenseHat
sense = SenseHat()

y = (255, 255, 0)
b = (0, 0, 255)

speed = 0.05

message = "hello world"

sense.show_message(message, speed, text_colour=y, back_colour=b)
sense.clear()
