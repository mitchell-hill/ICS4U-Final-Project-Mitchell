import ugame
import time
import random
import board
import displayio

# Constants
SCREEN_WIDTH = 160
SCREEN_HEIGHT = 120
PACMAN_RADIUS = 10
PACMAN_COLOR = 0xFFFF00  # Yellow
BACKGROUND_COLOR = 0x000000  # Black
BERRY_COLOR = 0xFF0000  # Red
POWER_UP_COLOR = 0x00FF00  # Green
PELLET_COLOR = 0xFFFFFF  # White
GHOST_COLORS = [0xFF5733, 0xFFC0CB, 0xFF0000, 0x87CEEB]  # Orange, Pink, Red, SkyBlue
GHOST_SIZE = 10  # Ghost size

# Initialize the display
display = board.DISPLAY

# Create a group to hold game objects
game_group = displayio.Group()

# Pac-Man variables
pacman_x = SCREEN_WIDTH // 2
pacman_y = SCREEN_HEIGHT // 2

# Function to create a circle shape for Pac-Man
def create_pacman(x, y):
	pacman = displayio.Circle(x=x, y=y, radius=PACMAN_RADIUS, fill=PACMAN_COLOR)
	return pacman

# Function to create a berry (red square)
def create_berry(x, y):
	berry = displayio.Rect(x=x, y=y, width=8, height=8, fill=BERRY_COLOR)
	return berry

# Function to create a power-up (green square)
def create_power_up(x, y):
	power_up = displayio.Rect(x=x, y=y, width=8, height=8, fill=POWER_UP_COLOR)
	return power_up

# Function to create a pellet (small white circle)
def create_pellet(x, y):
	pellet = displayio.Circle(x=x, y=y, radius=3, fill=PELLET_COLOR)
	return pellet

# Function to create a ghost (using square for simplicity)
def create_ghost(x, y, color):
	ghost = displayio.Rect(x=x, y=y, width=GHOST_SIZE, height=GHOST_SIZE, fill=color)
	return ghost

# Generate random positions for berries, power-ups, and pellets
def random_position():
	x = random.randint(10, SCREEN_WIDTH - 10)
	y = random.randint(10, SCREEN_HEIGHT - 10)
	return x, y

# Create game objects
pacman = create_pacman(pacman_x, pacman_y)
berries = [create_berry(*random_position()) for _ in range(5)]
power_up = create_power_up(*random_position())
pellets = [create_pellet(*random_position()) for _ in range(10)]

# Create ghosts with random positions and colors
ghosts = [create_ghost(random.randint(20, SCREEN_WIDTH - 20), random.randint(20, SCREEN_HEIGHT - 20), color) for color in GHOST_COLORS]

# Add all game objects to the display group
game_group.append(pacman)
for berry in berries:
	game_group.append(berry)
game_group.append(power_up)
for pellet in pellets:
	game_group.append(pellet)
for ghost in ghosts:
	game_group.append(ghost)

# Score and power-up status
score = 0
has_power_up = False
power_up_timer = 0

# Function to move Pac-Man
def move_pacman(dx, dy):
	global pacman_x, pacman_y
	pacman_x = max(min(pacman_x + dx, SCREEN_WIDTH - PACMAN_RADIUS), PACMAN_RADIUS)
	pacman_y = max(min(pacman_y + dy, SCREEN_HEIGHT - PACMAN_RADIUS), PACMAN_RADIUS)
	pacman.x = pacman_x
	pacman.y = pacman_y

# Function to move ghosts in random directions
def move_ghosts():
	for ghost in ghosts:
		direction = random.choice(["up", "down", "left", "right"])
		if direction == "up":
			ghost.y = max(ghost.y - 2, 0)
		elif direction == "down":
			ghost.y = min(ghost.y + 2, SCREEN_HEIGHT - GHOST_SIZE)
		elif direction == "left":
			ghost.x = max(ghost.x - 2, 0)
		elif direction == "right":
			ghost.x = min(ghost.x + 2, SCREEN_WIDTH - GHOST_SIZE)

# Check for collisions with items
def check_collisions():
	global score, has_power_up, power_up_timer
	# Check for collision with berries
	for berry in berries[:]:
		if abs(pacman_x - berry.x) < PACMAN_RADIUS + 4 and abs(pacman_y - berry.y) < PACMAN_RADIUS + 4:
			game_group.remove(berry)  # Remove the berry
			berries.remove(berry)
			score += 10
	# Check for collision with power-up
	if abs(pacman_x - power_up.x) < PACMAN_RADIUS + 4 and abs(pacman_y - power_up.y) < PACMAN_RADIUS + 4:
		game_group.remove(power_up)  # Remove the power-up
		has_power_up = True
		power_up_timer = 500  # Activate power-up for 500 game loops
	# Check for collision with pellets
	for pellet in pellets[:]:
		if abs(pacman_x - pellet.x) < PACMAN_RADIUS + 3 and abs(pacman_y - pellet.y) < PACMAN_RADIUS + 3:
			game_group.remove(pellet)  # Remove the pellet
			pellets.remove(pellet)
			score += 1
	# Check for collision with ghosts
	for ghost in ghosts:
		if abs(pacman_x - ghost.x) < PACMAN_RADIUS + GHOST_SIZE // 2 and abs(pacman_y - ghost.y) < PACMAN_RADIUS + GHOST_SIZE // 2:
			if not has_power_up:  # Game over if Pac-Man collides with a ghost
				print("Game Over! Final Score:", score)
				ugame.gameover()
			else:
				score += 50  # Bonus points for eating a ghost while powered up
				ghosts.remove(ghost)  # Remove ghost after eating it
				game_group.remove(ghost)

# Main game loop
def main():
	global score, has_power_up, power_up_timer
	while True:
		# Handle button input for movement
		if ugame.buttons.is_pressed(ugame.BUTTON_UP):
			move_pacman(0, -2)
		if ugame.buttons.is_pressed(ugame.BUTTON_DOWN):
			move_pacman(0, 2)
		if ugame.buttons.is_pressed(ugame.BUTTON_LEFT):
			move_pacman(-2, 0)
		if ugame.buttons.is_pressed(ugame.BUTTON_RIGHT):
			move_pacman(2, 0)

		# Move ghosts
		move_ghosts()

		# Check for collisions (berries, power-ups, pellets, ghosts)
		check_collisions()

		# If power-up is active, reduce the timer
		if has_power_up:
			power_up_timer -= 1
			if power_up_timer <= 0:
				has_power_up = False

		# Redraw the screen (this is necessary to clear old frames)
		display.fill(BACKGROUND_COLOR)
		display.show(game_group)

		# Display score
		# For simplicity, we can show the score on the PyBadge's display
		# But since displayio does not have text support in `ugame`, we need additional libraries for this
		# Here we will assume you use an external method for displaying score (e.g., `label` or other text display)
		print("Score:", score)  # For debugging output
		
		# Update display and delay for smooth game loop
		time.sleep(0.05)

# Start the game
main()
