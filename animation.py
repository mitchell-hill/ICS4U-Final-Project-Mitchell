# animation.py
import ugame

def import_sprite(path, asset_type, ghost_folder_name=None, pac_folder_name=None):
	"""Load sprite assets: ghosts, life, or pac."""
	try:
		# Handle loading life sprite (life.bmp)
		if asset_type == "life":
			full_path = path + "/life/life.bmp"
			life_sprite = ugame.display.load_image(full_path)  # Load the image using ugame's method
			return life_sprite

		# Handle loading ghost sprites (for each direction of a specific ghost)
		elif asset_type == "ghost" and ghost_folder_name:
			all_ghosts = []
			directions = ["up.bmp", "down.bmp", "right.bmp", "left.bmp"]
			folder_path = path + "/ghosts/" + ghost_folder_name  # Construct the path for the ghost folder
			
			ghost_frames = []
			for direction in directions:
				full_path = folder_path + "/" + direction  # Construct the full path to the image
				if ugame.display.load_image(full_path) is not None:
					sprite_image = ugame.display.load_image(full_path)  # Load the image using ugame's method
					ghost_frames.append(sprite_image)  # Add the image to the list
				else:
					print(f"Warning: {direction} not found in {folder_path}")
			
			all_ghosts.append(ghost_frames)  # Add the frames for this specific ghost
			return all_ghosts

		# Handle loading pac sprites (down, idle, left, power_up, right, up)
		elif asset_type == "pac" and pac_folder_name:
			pac_frames = []
			pac_directions = ["down", "idle", "left", "power_up", "right", "up"]
			
			# Loop through each pac direction folder
			for direction in pac_directions:
				direction_folder = path + "/pac/" + direction
				direction_frames = []

				# Check if there are 2 frames (0.bmp and 1.bmp) or just 1 frame (0.bmp)
				for frame_index in range(2 if direction != "idle" else 1):  # Only 1 frame in "idle"
					frame_name = f"{frame_index}.bmp"
					full_path = direction_folder + "/" + frame_name
					
					if ugame.display.load_image(full_path) is not None:
						sprite_image = ugame.display.load_image(full_path)  # Load the image using ugame's method
						direction_frames.append(sprite_image)  # Add the image to the list
					else:
						print(f"Warning: {frame_name} not found in {direction_folder}")
				
				pac_frames.append(direction_frames)  # Add the frames for the current direction

			return pac_frames
		
		else:
			print("Error: Invalid asset type or missing folder name.")
			return None

	except Exception as e:
		print(f"Error loading sprite assets: {e}")
		return None
