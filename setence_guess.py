#!/usr/bin/env python
from sense_hat import SenseHat
sense = SenseHat()

yellow = (255, 255, 0)
blue = (0, 0, 255)
black = (0, 0, 0)

speed = 0.01
message = "hello world"
while True:
    sense.show_message(message, speed, text_colour=yellow, back_colour=black)
    user_guess = raw_input("What is your guess? ")
    if user_guess == message:
        print "You win"
        break
    else:
        speed = speed + 0.01

sense.clear()
