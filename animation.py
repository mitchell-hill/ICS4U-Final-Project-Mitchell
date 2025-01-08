# animation.py
import board
import displayio
from os import walk
from adafruit_display_shapes.rect import Rect

# Function to import sprite images
def import_sprite(path):
	surface_list = []

	# Initialize display context
	for _, __, img_file in walk(path):
		for image in img_file:
			full_path = f"{path}/{image}"
			
			# Open the image file from CIRCUITPY (use open() for raw byte data)
			with open(full_path, "rb") as file:
				image_data = file.read()

			# Convert image data to displayio Bitmap (you'll likely want to use a format like .bmp, .png, etc.)
			# You might use an external tool to convert your image to a bitmap
			bitmap = displayio.OnDiskBitmap(full_path)
			
			# Create a TileGrid to display this bitmap
			sprite = displayio.TileGrid(bitmap, pixel_shader=displayio.ColorConverter())
			surface_list.append(sprite)
	
	return surface_list

# Usage of the import_sprite function
sprites = import_sprite("/sprites")  # Change this path to where your images are stored

# Example of displaying the first sprite on the screen
display = board.DISPLAY
group = displayio.Group()

# Add the first sprite (assuming at least one image is available)
if sprites:
	group.append(sprites[0])

display.show(group)

# Keep running
while True:
	pass
