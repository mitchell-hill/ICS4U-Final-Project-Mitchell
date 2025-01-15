# ghost.py
import random
import ugame
from settings import WIDTH, HEIGHT, GHOST_SPEED, CHAR_SIZE
from sprite import Sprite  # Assuming you have a sprite class to manage ghost images

class Ghost:
	def __init__(self, row, col, color, sprite_image):
		self.abs_x = row * CHAR_SIZE
		self.abs_y = col * CHAR_SIZE
		self.move_speed = GHOST_SPEED
		self.color = color
		self.move_directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
		
		self.moving_dir = "up"  # Initial movement direction
		self.directions = {'left': (-self.move_speed, 0), 'right': (self.move_speed, 0), 
						   'up': (0, -self.move_speed), 'down': (0, self.move_speed)}
		self.keys = ['left', 'right', 'up', 'down']
		self.direction = (0, 0)  # Initial direction is (0, 0)

		# Load the ghost sprite
		self.sprite = Sprite(sprite_image, self.abs_x, self.abs_y)

	def move_to_start_pos(self):
		"""Reset the ghost to its starting position."""
		self.abs_x = self.abs_x
		self.abs_y = self.abs_y
		self.sprite.move(self.abs_x, self.abs_y)

	def is_collide(self, x, y, walls_collide_list):
		"""Check if moving to the next position would result in a collision with walls."""
		new_x = self.abs_x + x
		new_y = self.abs_y + y
		# For simplicity, assume walls_collide_list contains tuples of (x, y) positions of walls
		for wall in walls_collide_list:
			if (new_x, new_y) == wall:
				return True
		return False

	def update(self, walls_collide_list):
		"""Update the ghost's position based on available moves."""
		# List of available moves
		available_moves = []
		for key in self.keys:
			if not self.is_collide(*self.directions[key], walls_collide_list):
				available_moves.append(key)

		# Randomly choose direction with a 60% chance
		randomizing = False if len(available_moves) <= 2 and self.direction != (0, 0) else True
		if randomizing and random.randrange(0, 100) <= 60:
			self.moving_dir = random.choice(available_moves)
			self.direction = self.directions[self.moving_dir]

		# Update position if the new direction does not result in a collision
		if not self.is_collide(*self.direction, walls_collide_list):
			self.abs_x += self.direction[0]
			self.abs_y += self.direction[1]
			self.sprite.move(self.abs_x, self.abs_y)  # Update sprite position
		else:
			# If collision occurs, don't move, set direction to zero
			self.direction = (0, 0)

		# Handle teleportation to the other side of the map if out of bounds
		if self.abs_x < 0:
			self.abs_x = WIDTH  # Teleport to the right side
		elif self.abs_x >= WIDTH:
			self.abs_x = 0  # Teleport to the left side

		if self.abs_y < 0:
			self.abs_y = HEIGHT  # Teleport to the bottom
		elif self.abs_y >= HEIGHT:
			self.abs_y = 0  # Teleport to the top
