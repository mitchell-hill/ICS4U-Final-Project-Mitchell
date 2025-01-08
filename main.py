# main.py
import time
import board
import displayio
from world import World
from settings import WIDTH, HEIGHT, NAV_HEIGHT

# Create the display context using CircuitPython's displayio
display = board.DISPLAY

class Main:
	def __init__(self, display):
		self.display = display
		self.FPS = 30  # Set your desired frame rate (frames per second)
		self.display_group = displayio.Group()  # Group for displaying all the elements

	def main(self):
		world = World(self.display_group)  # Create World instance with the display group

		# Main game loop
		while True:
			# Clear screen with a black fill
			self.display_group = displayio.Group()  # Reset the display group
			self.display.show(self.display_group)

			# Handle events (e.g., button presses or touch input)
			self.handle_input()

			# Update the world state (game logic, animations, etc.)
			world.update()

			# Update the display
			self.display.show(self.display_group)

			# Control the frame rate
			time.sleep(1 / self.FPS)

	def handle_input(self):
		# Example input handling with buttons (You can use `digitalio` or `touchio` depending on your hardware)
		# For example, to check for button presses:
		# from digitalio import DigitalInOut, Direction, Pull
		# button = DigitalInOut(board.BUTTON_A)
		# button.direction = Direction.INPUT
		# button.pull = Pull.UP

		# Check if BUTTON_A is pressed
		# if not button.value:  # Button is pressed
		#     print("Button A pressed")
		
		pass  # Placeholder, modify according to your input devices

if __name__ == "__main__":
	play = Main(display)
	play.main()
