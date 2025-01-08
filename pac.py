# pac.py
import time
import board
import displayio
from settings import CHAR_SIZE, PLAYER_SPEED
from animation import import_sprite

class Pac:
	def __init__(self, row, col, display_group):
		# Set the position on the grid
		self.abs_x = (row * CHAR_SIZE)
		self.abs_y = (col * CHAR_SIZE)
		
		# Initialize the display group for rendering
		self.display_group = display_group
		
		# Initialize animation frames (using displayio.Bitmap)
		self._import_character_assets()
		self.frame_index = 0
		self.animation_speed = 0.5
		self.image = self.animations["idle"][self.frame_index]  # Start with idle animation
		self.rect = displayio.Rectangle(x=self.abs_x, y=self.abs_y, width=CHAR_SIZE, height=CHAR_SIZE, outline=0x0000FF)
		
		# Player stats
		self.pac_speed = PLAYER_SPEED
		self.immune_time = 0
		self.immune = False
		self.direction = (0, 0)

		self.directions = {
			'left': (-PLAYER_SPEED, 0),
			'right': (PLAYER_SPEED, 0),
			'up': (0, -PLAYER_SPEED),
			'down': (0, PLAYER_SPEED)
		}
		
		# Initial status and score
		self.status = "idle"
		self.life = 3
		self.pac_score = 0
		
		# Add player rectangle to display group
		self.display_group.append(self.rect)

	def _import_character_assets(self):
		# Import sprites for different directions/animations
		character_path = "assets/pac/"
		self.animations = {
			"up": [],
			"down": [],
			"left": [],
			"right": [],
			"idle": [],
			"power_up": []
		}
		for animation in self.animations.keys():
			full_path = character_path + animation
			self.animations[animation] = import_sprite(full_path)
			print(f"Loaded {len(self.animations[animation])} frames for {animation} animation.")

		# Handle missing animations
		if len(self.animations["idle"]) == 0:
			print("Error: No idle frames loaded, using default image.")
			self.animations["idle"].append(displayio.Bitmap(CHAR_SIZE, CHAR_SIZE))  # Blank image

	def _is_collide(self, x, y, walls_collide_list):
		# Check if moving to a new position collides with walls
		tmp_rect = displayio.Rectangle(x=self.rect.x + x, y=self.rect.y + y, width=CHAR_SIZE, height=CHAR_SIZE, outline=0xFF0000)
		for wall in walls_collide_list:
			if tmp_rect.collides(wall):
				return True
		return False

	def move_to_start_pos(self):
		# Reset position
		self.rect.x = self.abs_x
		self.rect.y = self.abs_y

	def animate(self, pressed_keys, walls_collide_list):
		animation = self.animations[self.status]

		# Loop through frames
		self.frame_index += self.animation_speed
		if self.frame_index >= len(animation):
			self.frame_index = 0
		self.image = animation[int(self.frame_index)]

		# Handle movement and direction based on key input
		for key, key_value in pressed_keys.items():
			if key_value and not self._is_collide(*self.directions[key], walls_collide_list):
				self.direction = self.directions[key]
				self.status = key if not self.immune else "power_up"
				break

		# Move the character if no collision
		if not self._is_collide(*self.direction, walls_collide_list):
			self.rect.x += self.direction[0]
			self.rect.y += self.direction[1]
			self.status = self.status if not self.immune else "power_up"

		if self._is_collide(*self.direction, walls_collide_list):
			self.status = "idle" if not self.immune else "power_up"

	def update(self, walls_collide_list):
		# Update immunity timer and reset rect for proper placement
		self.immune = True if self.immune_time > 0 else False
		self.immune_time -= 1 if self.immune_time > 0 else 0
		self.rect = displayio.Rectangle(x=self.rect.x, y=self.rect.y, width=CHAR_SIZE, height=CHAR_SIZE, outline=0x0000FF)
