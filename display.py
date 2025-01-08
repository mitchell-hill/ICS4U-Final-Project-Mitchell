# display.py
import board
import displayio
from adafruit_display_text import label
from adafruit_display_shapes.rect import rect
from adafruit_display_shapes.circle import circle
from settings import WIDTH, HEIGHT, CHAR_SIZE

class Display:
	def __init__(self):
		# Set up the display
		self.display = board.DISPLAY

		# Set up fonts using the adafruit_display_text label
		self.font = bitmap_font.load_font("/fonts/UbuntuMono-Bold-16.bdf")  # Replace with your font path
		self.game_over_font = bitmap_font.load_font("/fonts/DejaVuSansMono-Bold-48.bdf")
		self.text_color = 0xDC143C  # Crimson in hex

		# Setup display group to hold all elements
		self.display_group = displayio.Group()

	def show_life(self, life):
		# Load the life image (make sure you have an image like "life.png" on CIRCUITPY)
		img_path = "/assets/life/life.png"  # Make sure this path is correct
		life_image = displayio.OnDiskBitmap(img_path)

		# Scale the image (resize if necessary)
		tile_grid = displayio.TileGrid(life_image, pixel_shader=life_image.pixel_shader)

		life_x = CHAR_SIZE // 2
		if life != 0:
			for _ in range(life):
				tile_grid.x = life_x
				tile_grid.y = HEIGHT + (CHAR_SIZE // 2)
				self.display_group.append(tile_grid)  # Add the image to the display group
				life_x += CHAR_SIZE

	def show_level(self, level):
		# Render level text
		level_text = label.Label(self.font, text=f"Level {level}", color=self.text_color)
		level_x = WIDTH // 3
		level_text.x = level_x
		level_text.y = HEIGHT + (CHAR_SIZE // 2)
		self.display_group.append(level_text)

	def show_score(self, score):
		# Render score text
		score_text = label.Label(self.font, text=f"{score}", color=self.text_color)
		score_x = WIDTH // 3 * 2
		score_text.x = score_x
		score_text.y = HEIGHT + (CHAR_SIZE // 2)
		self.display_group.append(score_text)

	def game_over(self):
		# Game over message
		message = label.Label(self.game_over_font, text="GAME OVER!!", color=0x7FFF00)  # Chartreuse color
		instruction = label.Label(self.font, text='Press "R" to Restart', color=0x00FFFF)  # Aqua color

		message.x = WIDTH // 4
		message.y = HEIGHT // 3
		instruction.x = WIDTH // 4
		instruction.y = HEIGHT // 2

		self.display_group.append(message)
		self.display_group.append(instruction)

	def refresh(self):
		# Update the display with everything in the display group
		self.display.show(self.display_group)
