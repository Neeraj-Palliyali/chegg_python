# the import staments comes first always
import board
import time
import digitalio

# A DigitalInOut is used to digitally control I/O pins
x=digitalio.DigitalInOut(board.D13)

# The direction of the pin.
# Setting this will change the direction to output
x.direction = digitalio.Direction.Output


# while TRUE for looping indefinitely
while True:
    # sets the led to on
    x.value = True
    # sleeps for 75ms
    time.sleep(.75)


    x.value = False
    # turns off the bulb and waits for 25ms
    time.sleep(.25)


