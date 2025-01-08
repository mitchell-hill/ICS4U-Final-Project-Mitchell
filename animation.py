# animation.py
import board
import displayio
import os
from adafruit_display_shapes.rect import rect

# Function to import sprite images from all subdirectories in /assets
def import_sprite(path):
	surface_list = []

	try:
		# List all directories in the given path (i.e., /assets)
		directories = [d for d in os.listdir(path) if os.path.isdir(f"{path}/{d}")]
		
		for directory in directories:
			# Construct the full path for the subdirectory (e.g., /assets/pac)
			subdirectory_path = f"{path}/{directory}"
			
			# List all files in this subdirectory
			file_list = os.listdir(subdirectory_path)
			
			for image in file_list:
				# Only process image files
				if image.endswith('.bmp') or image.endswith('.png'):  # Check for image file extensions
					full_path = f"{subdirectory_path}/{image}"
					
					# Open the image file from CIRCUITPY
					with open(full_path, "rb") as file:
						image_data = file.read()

					# Convert image data to displayio Bitmap
					bitmap = displayio.OnDiskBitmap(full_path)
					
					# Create a TileGrid to display this bitmap
					sprite = displayio.TileGrid(bitmap, pixel_shader=displayio.ColorConverter())
					surface_list.append(sprite)
	
	except Exception as e:
		print(f"Error while importing sprites: {e}")
	
	return surface_list

# Usage of the import_sprite function
sprites = import_sprite("/assets")  # Pass the /assets directory

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
