import time
import board
import displayio
from adafruit_display_shapes.rect import Rect
from adafruit_display_text import label
import terminalio

# Set up the display
display = board.DISPLAY

# Create a Group to hold display elements
group = displayio.Group()

# Create a red rectangle
rect = Rect(10, 10, 100, 50, fill=0xFF0000)
group.append(rect)

# Create a label (text)
text = "Hello, World!"
text_area = label.Label(terminalio.FONT, text=text, color=0xFFFFFF, x=20, y=100)
group.append(text_area)

# Show everything on the display
display.show(group)

# Keep the program running
while True:
    time.sleep(0.1)  # Keep the display alive
