# the import staments comes first always
import board
import time
import digitalio

# A DigitalInOut is used to digitally control I/O pins
x=digitalio.DigitalInOut(board.D13)

# The direction of the pin.
# Setting this will use the defaults from the corresponding switch_to_output()
x.direction = digitalio.Direction.Output
