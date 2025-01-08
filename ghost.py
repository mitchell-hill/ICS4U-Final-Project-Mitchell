# ghost.py
import board
import displayio
import random
from settings import WIDTH, HEIGHT, CHAR_SIZE, GHOST_SPEED

class Ghost:
	def __init__(self, row, col, color):
		# Initialize position and settings
		self.abs_x = row * CHAR_SIZE
		self.abs_y = col * CHAR_SIZE
		self.rect = displayio.Rectangle(x=self.abs_x, y=self.abs_y, width=CHAR_SIZE, height=CHAR_SIZE, fill=0x000000)
		self.move_speed = GHOST_SPEED
		self.color = color
		self.move_directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]

		# Load ghost images for different movement directions
		self.img_path = f'/assets/ghosts/{color}/'
		self.moving_dir = "up"
		self.img_name = f'{self.moving_dir}.bmp'
		self.image = displayio.OnDiskBitmap(self.img_path + self.img_name)

		# Use TileGrid for sprite-like behavior
		self.tile_grid = displayio.TileGrid(self.image, pixel_shader=self.image.pixel_shader)

		self.directions = {'left': (-self.move_speed, 0), 'right': (self.move_speed, 0),
						   'up': (0, -self.move_speed), 'down': (0, self.move_speed)}
		self.keys = ['left', 'right', 'up', 'down']
		self.direction = (0, 0)

	def move_to_start_pos(self):
		# Reset to start position
		self.rect.x = self.abs_x
		self.rect.y = self.abs_y

	def is_collide(self, x, y, walls_collide_list):
		# Check for collision with walls
		tmp_rect = displayio.Rectangle(x=self.rect.x + x, y=self.rect.y + y, width=CHAR_SIZE, height=CHAR_SIZE, fill=0)
		for wall in walls_collide_list:
			if tmp_rect.collide(wall):
				return True
		return False

	def _animate(self):
		# Update the ghost's image based on the moving direction
		self.img_name = f'{self.moving_dir}.bmp'
		self.image = displayio.OnDiskBitmap(self.img_path + self.img_name)
		self.tile_grid = displayio.TileGrid(self.image, pixel_shader=self.image.pixel_shader)
		self.rect = self.tile_grid

	def update(self, walls_collide_list):
		# Move ghost and handle random movement
		available_moves = []
		for key in self.keys:
			if not self.is_collide(*self.directions[key], walls_collide_list):
				available_moves.append(key)

		randomizing = False if len(available_moves) <= 2 and self.direction != (0, 0) else True

		# 60% chance of randomizing ghost move
		if randomizing and random.randrange(0, 100) <= 60:
			self.moving_dir = random.choice(available_moves)
			self.direction = self.directions[self.moving_dir]

		# Move ghost if no collision in the chosen direction
		if not self.is_collide(*self.direction, walls_collide_list):
			self.rect.x += self.direction[0]
			self.rect.y += self.direction[1]
		else:
			self.direction = (0, 0)

		# Teleport the ghost to the other side if it moves out of bounds
		if self.rect.x + CHAR_SIZE <= 0:
			self.rect.x = WIDTH
		elif self.rect.x >= WIDTH:
			self.rect.x = 0

		if self.rect.y + CHAR_SIZE <= 0:
			self.rect.y = HEIGHT
		elif self.rect.y >= HEIGHT:
			self.rect.y = 0

		# Update animation (based on current direction)
		self._animate()
