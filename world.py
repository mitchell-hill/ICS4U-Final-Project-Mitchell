# world.py
import time
import displayio
from settings import HEIGHT, WIDTH, NAV_HEIGHT, CHAR_SIZE, MAP, PLAYER_SPEED
from pac import Pac
from cell import Cell
from berry import Berry
from ghost import Ghost
from display import Display

class World:
	def __init__(self, display_group):
		self.display_group = display_group  # Group for all elements to be drawn

		self.player = None
		self.ghosts = []
		self.walls = []
		self.berries = []

		self.display = Display(self.display_group)

		self.game_over = False
		self.reset_pos = False
		self.player_score = 0
		self.game_level = 1

		self._generate_world()

	def _generate_world(self):
		# Initialize the world by adding walls, berries, ghosts, and PacMan based on the MAP
		for y_index, col in enumerate(MAP):
			for x_index, char in enumerate(col):
				if char == "1":  # Wall
					wall = Cell(x_index, y_index, CHAR_SIZE, CHAR_SIZE)
					self.walls.append(wall)
					self.display_group.append(wall.rect)  # Add wall to display group
				elif char == " ":  # Empty space for berry
					berry = Berry(x_index, y_index, CHAR_SIZE // 4)
					self.berries.append(berry)
					self.display_group.append(berry.rect)
				elif char == "B":  # Big berry (power-up)
					berry = Berry(x_index, y_index, CHAR_SIZE // 2, is_power_up=True)
					self.berries.append(berry)
					self.display_group.append(berry.rect)
				elif char == "s":  # Ghost starting position
					ghost = Ghost(x_index, y_index, "skyblue")
					self.ghosts.append(ghost)
					self.display_group.append(ghost.rect)
				elif char == "p":
					ghost = Ghost(x_index, y_index, "pink")
					self.ghosts.append(ghost)
					self.display_group.append(ghost.rect)
				elif char == "o":
					ghost = Ghost(x_index, y_index, "orange")
					self.ghosts.append(ghost)
					self.display_group.append(ghost.rect)
				elif char == "r":
					ghost = Ghost(x_index, y_index, "red")
					self.ghosts.append(ghost)
					self.display_group.append(ghost.rect)
				elif char == "P":  # PacMan starting position
					self.player = Pac(x_index, y_index, self.display_group)
					self.display_group.append(self.player.rect)

		self.walls_collide_list = [wall.rect for wall in self.walls]

	def generate_new_level(self):
		for y_index, col in enumerate(MAP):
			for x_index, char in enumerate(col):
				if char == " ":
					berry = Berry(x_index, y_index, CHAR_SIZE // 4)
					self.berries.append(berry)
					self.display_group.append(berry.rect)
				elif char == "B":
					berry = Berry(x_index, y_index, CHAR_SIZE // 2, is_power_up=True)
					self.berries.append(berry)
					self.display_group.append(berry.rect)
		time.sleep(2)

	def restart_level(self):
		self.berries.clear()
		self.display_group = [self.player.rect]  # Only keep player rect
		[ghost.move_to_start_pos() for ghost in self.ghosts]
		self.game_level = 1
		self.player.pac_score = 0
		self.player.life = 3
		self.player.move_to_start_pos()
		self.player.direction = (0, 0)
		self.player.status = "idle"
		self.generate_new_level()

	def _dashboard(self):
		# Display the navigation bar (score, life, level)
		nav = displayio.Rect(x=0, y=HEIGHT, width=WIDTH, height=NAV_HEIGHT, fill=0xA0A0A0)
		self.display_group.append(nav)
		
		self.display.show_life(self.player.life)
		self.display.show_level(self.game_level)
		self.display.show_score(self.player.pac_score)

	def _check_game_state(self):
		# Check for game over condition
		if self.player.life == 0:
			self.game_over = True

		# Check if all berries are eaten and proceed to the next level
		if len(self.berries) == 0 and self.player.life > 0:
			self.game_level += 1
			for ghost in self.ghosts:
				ghost.move_speed += self.game_level
				ghost.move_to_start_pos()

			self.player.move_to_start_pos()
			self.player.direction = (0, 0)
			self.player.status = "idle"
			self.generate_new_level()

	def update(self, pressed_keys):
		if not self.game_over:
			# Handle player movement
			self.player.animate(pressed_keys, self.walls_collide_list)

			# Teleporting to the other side of the screen
			if self.player.rect.x + CHAR_SIZE <= 0:
				self.player.rect.x = WIDTH
			elif self.player.rect.x >= WIDTH:
				self.player.rect.x = 0

			# PacMan eating berries
			for berry in self.berries:
				if self.player.rect.collides_with(berry.rect):
					if berry.is_power_up:
						self.player.immune_time = 150  # Immunity timer
						self.player.pac_score += 50
					else:
						self.player.pac_score += 10
					berry.kill()

			# Check collisions with ghosts
			for ghost in self.ghosts:
				if self.player.rect.collides_with(ghost.rect):
					if not self.player.immune:
						self.player.life -= 1
						self.reset_pos = True
						break
					else:
						ghost.move_to_start_pos()
						self.player.pac_score += 100

		self._check_game_state()

		# Update the game elements
		for wall in self.walls:
			wall.update(self.display_group)
		for berry in self.berries:
			berry.update(self.display_group)
		for ghost in self.ghosts:
			ghost.update(self.walls_collide_list)

		self.player.update()
		self.display_group.append(self.player.rect)  # Re-add the player rect to the display group
		self.display.game_over() if self.game_over else None

		self._dashboard()

		# Reset positions after PacMan dies
		if self.reset_pos and not self.game_over:
			for ghost in self.ghosts:
				ghost.move_to_start_pos()
			self.player.move_to_start_pos()
			self.reset_pos = False

		# Restart on key press
		if self.game_over:
			if "r" in pressed_keys:
				self.game_over = False
				self.restart_level()
