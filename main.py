import time
from adafruit_display_shapes.rect import Rect
import displayio
import ugame 

# Constants for the game
WIDTH = 160  # Screen width
HEIGHT = 128  # Screen height
NAV_HEIGHT = 16  # Navigation bar height
CHAR_SIZE = 8  # Size of character sprites
PLAYER_SPEED = 2  # Player movement speed
GHOST_SPEED = PLAYER_SPEED  # Same as player speed for now

# Map layout
MAP = [
    ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
	['1',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','1'],
	['1','B','1','1',' ','1','1','1',' ','1',' ','1','1','1',' ','1','1','B','1'],
	['1',' ',' ',' ',' ','1',' ',' ',' ','1',' ',' ',' ','1',' ',' ',' ',' ','1'],
	['1','1',' ','1',' ','1',' ','1',' ','1',' ','1',' ','1',' ','1',' ','1','1'],
	['1',' ',' ','1',' ',' ',' ','1',' ',' ',' ','1',' ',' ',' ','1',' ',' ','1'],
	['1',' ','1','1','1','1',' ','1','1','1','1','1',' ','1','1','1','1',' ','1'],
	['1',' ',' ',' ',' ',' ',' ',' ',' ','r',' ',' ',' ',' ',' ',' ',' ',' ','1'],
	['1','1',' ','1','1','1',' ','1','1','-','1','1',' ','1','1','1',' ','1','1'],
	[' ',' ',' ',' ',' ','1',' ','1','s','p','o','1',' ','1',' ',' ',' ',' ',' '],
	['1','1',' ','1',' ','1',' ','1','1','1','1','1',' ','1',' ','1',' ','1','1'],
	['1',' ',' ','1',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','1',' ',' ','1'],
	['1',' ','1','1','1','1',' ','1','1','1','1','1',' ','1','1','1','1',' ','1'],
	['1',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','1'],
	['1','1','1',' ','1','1','1',' ','1','1','1',' ','1','1','1',' ','1','1','1'],
	['1',' ',' ',' ','1',' ',' ',' ',' ','P',' ',' ',' ',' ','1',' ',' ',' ','1'],
	['1','B','1',' ','1',' ','1',' ','1','1','1',' ','1',' ','1',' ','1','B','1'],
	['1',' ','1',' ',' ',' ','1',' ',' ',' ',' ',' ','1',' ',' ',' ','1',' ','1'],
	['1',' ','1','1','1',' ','1','1','1',' ','1','1','1',' ','1','1','1',' ','1'],
	['1',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','1'],
	['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1']
]

# Berry class definition
class Berry(Rect):
    def __init__(self, row, col, size=CHAR_SIZE, is_power_up=False):
        super().__init__(row * CHAR_SIZE, col * CHAR_SIZE, size, size, fill=0xFF00FF)
        self.power_up = is_power_up
        self.size = size
        self.value = 50 if is_power_up else 10  # Assign value based on type

# Cell class definition
class Cell(ugame.sprite.Sprite):
    def __init__(self, row, col, length, width):
        super().__init__()
        self.width = length
        self.height = width
        self.id = (row, col)
        self.abs_x = row * self.width
        self.abs_y = col * self.height

        self.rect = ugame.Rect(self.abs_x, self.abs_y, self.width, self.height)

        self.occupying_piece = None

    def update(self, screen):
        ugame.draw.rect(screen, ugame.Color("blue2"), self.rect)

# Load ghost sprites (dummy function, you need to implement it)
def import_sprite(sprite_path):
    # This function should load and return sprite data.
    # Here, it's just a placeholder.
    return [0xFFFFFF] * 4  # Dummy return value for sprite (replace with real data)

# Ghost class definition
class Ghost(Rect):
    def __init__(self, x, y, color):
        super().__init__(x * CHAR_SIZE, y * CHAR_SIZE, CHAR_SIZE, CHAR_SIZE, fill=color)
        self.move_speed = PLAYER_SPEED
        self.start_x = x * CHAR_SIZE
        self.start_y = y * CHAR_SIZE
        self.color = color  # Default color for the ghost

        # Load ghost sprite animations (normal and frightened)
        self.sprite_normal = import_sprite(f"assets/ghosts/{self.color}/normal")
        self.sprite_frightened = import_sprite(f"assets/ghosts/{self.color}/frightened")
        self.sprite_current = self.sprite_normal
        self.sprite_index = 0
        self.sprite_timer = 0

    def update_sprite(self):
        self.sprite_timer += 1
        if self.sprite_timer > 5:  # Adjust speed of animation
            self.sprite_timer = 0
            self.sprite_index = (self.sprite_index + 1) % len(self.sprite_current)

        self.fill = self.sprite_current[self.sprite_index]  # Update the sprite

    def move_to_start_pos(self):
        self.x = self.start_x
        self.y = self.start_y
        self.update_sprite()

# Pac class definition
class Pac(Rect):
    def __init__(self, x, y):
        super().__init__(x * CHAR_SIZE, y * CHAR_SIZE, CHAR_SIZE, CHAR_SIZE, fill=0xFFFF00)
        self.abs_x = x * CHAR_SIZE
        self.abs_y = y * CHAR_SIZE
        self.pac_speed = PLAYER_SPEED
        self.direction = (0, 0)
        self.life = 3
        self.pac_score = 0
        self.immune_time = 0
        self.immune = False

        # Load Pac-Man sprite animations
        self.sprite_left = import_sprite("assets/pac/left")
        self.sprite_right = import_sprite("assets/pac/right")
        self.sprite_up = import_sprite("assets/pac/up")
        self.sprite_down = import_sprite("assets/pac/down")
        self.sprite_current = self.sprite_right  # Default sprite direction
        self.sprite_index = 0  # Keeps track of which frame to display
        self.sprite_timer = 0  # Timer for sprite animation speed

    def animate(self, keys, walls_collide_list):
        # Determine movement direction based on keys
        directions = {
            "left": (-PLAYER_SPEED, 0),
            "right": (PLAYER_SPEED, 0),
            "up": (0, -PLAYER_SPEED),
            "down": (0, PLAYER_SPEED)
        }

        pressed = False
        for key, direction in directions.items():
            if keys.get(key, False):
                next_rect = Rect(
                    self.x + direction[0], self.y + direction[1],
                    self.width, self.height
                )
                if not any(next_rect.colliderect(wall) for wall in walls_collide_list):
                    self.direction = direction
                    pressed = True
                    break

        if pressed:
            self.x += self.direction[0]
            self.y += self.direction[1]
        
        # Update sprite animation based on movement direction
        self.update_sprite()

        # Handle immunity and power-up
        self.immune = self.immune_time > 0
        if self.immune:
            self.immune_time -= 1

    def update_sprite(self):
        # Animate the sprite by cycling through frames
        self.sprite_timer += 1
        if self.sprite_timer > 5:  # Adjust speed of animation
            self.sprite_timer = 0
            self.sprite_index = (self.sprite_index + 1) % len(self.sprite_current)
        
        # Choose the correct sprite based on the direction
        if self.direction == (0, 0):
            return  # No movement, don't change sprite
        
        if self.direction == (-PLAYER_SPEED, 0):  # Left
            self.sprite_current = self.sprite_left
        elif self.direction == (PLAYER_SPEED, 0):  # Right
            self.sprite_current = self.sprite_right
        elif self.direction == (0, -PLAYER_SPEED):  # Up
            self.sprite_current = self.sprite_up
        elif self.direction == (0, PLAYER_SPEED):  # Down
            self.sprite_current = self.sprite_down

        # Set the sprite to display based on the current index
        self.fill = self.sprite_current[self.sprite_index]  # Update the sprite

# World class to manage game objects and logic
class World:
    def __init__(self, screen):
        self.screen = screen
        self.player = Pac(1, 1)  # Starting position for Pac-Man
        self.ghosts = []
        self.walls = []
        self.berries = []
        self._generate_world()
        self.game_over = False
        self.reset_pos = False
        self.player_score = 0
        self.game_level = 1
        
    def generate_new_level(self):
        # Generate a new level based on the current level or preset configurations
        # Modify the map or add more complexity to the game here if needed
        self._generate_world()  # Rebuild the world for the new level
    
    def _generate_world(self):
        # Clear previous game elements
        self.walls.clear()
        self.berries.clear()
        self.ghosts.clear()

        # Generate walls, berries, and ghosts based on the map
        for y_index, row in enumerate(MAP):
            for x_index, cell in enumerate(row):
                if cell == "1":
                    self.walls.append(Rect(x_index * CHAR_SIZE, y_index * CHAR_SIZE, CHAR_SIZE, CHAR_SIZE, fill=0x0000FF))  # Wall color blue
                elif cell == "B":
                    self.berries.append(Berry(x_index, y_index))  # Berries
                elif cell in "spo":
                    self.ghosts.append(Ghost(x_index, y_index, color=cell))  # Ghosts - Use 's', 'p', 'o' for color

    def draw_world(self):
        # Draw all the elements on the screen
        for wall in self.walls:
            self.screen.fill(wall.fill, wall)
        for berry in self.berries:
            self.screen.fill(berry.fill, berry)
        for ghost in self.ghosts:
            self.screen.fill(ghost.fill, ghost)
        self.screen.fill(self.player.fill, self.player)  # Draw Pac-Man

    def _dashboard(self):
        # Update and show the HUD with score, lives, and level
        self.display.show_score(self.player.pac_score)
        self.display.show_life(self.player.life)
        self.display.show_level(self.game_level)

    def reset_player_position(self):
        # Reset the player to the starting position
        self.player.x = 1 * CHAR_SIZE
        self.player.y = 1 * CHAR_SIZE
        self.player.direction = (0, 0)  # Stop movement
        self.player.immune_time = 0  # Reset immunity timer

    def reset_ghosts_position(self):
        # Reset all ghosts to their starting positions
        for ghost in self.ghosts:
            ghost.move_to_start_pos()

    def check_game_over(self):
        # Check if the game is over (player has no lives left)
        if self.player.life <= 0:
            self.game_over = True

    def show_score(self, score):
        # Display the player's score on the screen
        font = ugame.font.SysFont("Arial", 16)
        score_text = font.render(f"Score: {score}", True, (255, 255, 255))
        self.screen.blit(score_text, (10, 10))  # Position score at the top-left corner

    def show_life(self, life):
        # Display the player's life on the screen
        font = ugame.font.SysFont("Arial", 16)
        life_text = font.render(f"Lives: {life}", True, (255, 255, 255))
        self.screen.blit(life_text, (WIDTH - 100, 10))  # Position lives near the top-right corner

    def show_level(self, level):
        # Display the current level on the screen
        font = ugame.font.SysFont("Arial", 16)
        level_text = font.render(f"Level: {level}", True, (255, 255, 255))
        self.screen.blit(level_text, (WIDTH // 2 - level_text.get_width() // 2, 10))  # Position level at the top center

    def update(self):
        # Update game state and logic
        if not self.game_over:
            self.check_collisions()
            self.check_game_over()
            self._dashboard()
        
        if self.reset_pos:
            self.reset_player_position()
            self.reset_ghosts_position()
            self.reset_pos = False

    def _dashboard(self):
        # Update and show the HUD with score, lives, and level
        self.show_score(self.player.pac_score)
        self.show_life(self.player.life)
        self.show_level(self.game_level)

    def check_collisions(self):
        # Check for collisions between player and various game objects
        for berry in self.berries:
            if self.player.rect.colliderect(berry.rect):
                self.player.pac_score += berry.value
                self.berries.remove(berry)

        for ghost in self.ghosts:
            if self.player.rect.colliderect(ghost.rect):
                if not self.player.immune:
                    self.player.life -= 1
                    self.reset_pos = True
                    break
                else:
                    self.player.pac_score += 100
                    self.ghosts.remove(ghost)

    def restart_level(self):
        # Reset game state and restart level
        self.berries.clear()  # Clear the berries
        self.game_level = 1  # Reset the level
        self.player.pac_score = 0  # Reset the score
        self.player.life = 3  # Reset the lives
        self.reset_pos = False  # Reset the reset position flag
        self._generate_world()  # Regenerate the world, walls, berries, etc.
        self.game_over = False  # Set the game to continue after restart

    def game_loop(self):
        # Main game loop where the actual gameplay occurs
        while True:
            if self.game_over:
                self.display_game_over_screen()
            else:
                self.update()

            # Update the screen
            ugame.display.update()
            ugame.time.Clock().tick(30)  # Limit to 30 frames per second

    def display_game_over_screen(self):
        # Code to display "Game Over" screen with restart option
        font = ugame.font.SysFont("Arial", 24)
        game_over_text = font.render("Game Over", True, (255, 0, 0))
        restart_text = font.render("Press R to Restart", True, (255, 255, 255))

        self.screen.fill((0, 0, 0))  # Fill screen with black for Game Over
        self.screen.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 2 - 30))
        self.screen.blit(restart_text, (WIDTH // 2 - restart_text.get_width() // 2, HEIGHT // 2 + 10))

        ugame.display.update()

        # Wait for user to press R to restart
        while True:
            pressed_keys = ugame.key.get_pressed()
            if pressed_keys[ugame.K_r]:
                self.restart_level()
                break
            ugame.time.wait(100)  # Adding small delay to prevent key hold-up

    # Main game loop
def main():
    # Setup game world and Pac-Man
    screen = displayio.Display(ugame.video, auto_refresh=True)
    player = Pac(1, 1)  # Starting position for Pac-Man
    game_over = False

    while True:
        # Handle button input for movement
        if ugame.buttons.is_pressed(ugame.BUTTON_UP):
            player.animate({"up": True}, [])  # Player moves up
        if ugame.buttons.is_pressed(ugame.BUTTON_DOWN):
            player.animate({"down": True}, [])  # Player moves down
        if ugame.buttons.is_pressed(ugame.BUTTON_LEFT):
            player.animate({"left": True}, [])  # Player moves left
        if ugame.buttons.is_pressed(ugame.BUTTON_RIGHT):
            player.animate({"right": True}, [])  # Player moves right

        # Update display (using the built-in displayio for ugame)
        screen.show(player)  # Show Pac-Man (you may need to handle sprite display differently)

        # Display score and other info (you could use a text label for this)
        # For simplicity, print to console
        print("Score:", player.pac_score)

        # Update display and delay for smooth game loop
        time.sleep(0.01)

# Start the game
main()