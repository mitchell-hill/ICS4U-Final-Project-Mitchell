# cell.py
import board
import displayio
from adafruit_display_shapes.rect import Rect

class Cell:
	def __init__(self, row, col, length, width):
		# Set up the cell's dimensions and position
		self.width = length
		self.height = width
		self.id = (row, col)
		self.abs_x = row * self.width
		self.abs_y = col * self.height

		# Create a displayio Rect to represent the cell
		self.rect = Rect(self.abs_x, self.abs_y, self.width, self.height, fill=0x5B5B5B)  # Default color blue2 in hex

		self.occupying_piece = None

	def update(self, display_group):
		# Add or update the cell rectangle in the display group
		display_group.append(self.rect)
