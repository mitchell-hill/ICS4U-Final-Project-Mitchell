# berry.py
import board
import displayio
from adafruit_display_shapes.circle import Circle
from settings import CHAR_SIZE

class Berry:
	def __init__(self, row, col, size, is_power_up=False):
		self.power_up = is_power_up
		self.size = size
		self.color = 0xD85F8D  # 'violetred' color in hex
		self.thickness = size
		self.abs_x = (row * CHAR_SIZE) + (CHAR_SIZE // 2)
		self.abs_y = (col * CHAR_SIZE) + (CHAR_SIZE // 2)

		# Create the visual representation of the berry (a circle)
		self.circle = Circle(self.abs_x, self.abs_y, self.size, fill=self.color)

	def update(self, display_group):
		# Remove any previous circle (optional if using a group for sprites)
		display_group.append(self.circle)  # Add the berry circle to the display group
