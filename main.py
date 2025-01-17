import time
import random
from adafruit_display_shapes.rect import Rect
from adafruit_display_text import label
import displayio
import terminalio

# Settings
WIDTH = 160  # Screen width
HEIGHT = 128  # Screen height
NAV_HEIGHT = 16  # Navigation bar height
CHAR_SIZE = 8  # Size of character sprites
PLAYER_SPEED = 2  # Player movement speed
MAP = [['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
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

class Cell(Rect):
    def __init__(self, x, y, width, height):
        super().__init__(x * CHAR_SIZE, y * CHAR_SIZE, width, height, fill=0x0000FF)

class Berry(Rect):
    def __init__(self, x, y, size, is_power_up=False):
        color = 0xFFFF00 if is_power_up else 0xFF0000
        super().__init__(x * CHAR_SIZE + (CHAR_SIZE - size) // 2, y * CHAR_SIZE + (CHAR_SIZE - size) // 2, size, size, fill=color)
        self.power_up = is_power_up

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

class Display:
    def __init__(self, screen):
        self.screen = screen

    def show_life(self, life):
        # Logic for displaying life
        pass

    def show_level(self, level):
        # Logic for displaying level
        pass

    def show_score(self, score):
        # Logic for displaying score
        pass

    def game_over(self):
        # Logic for displaying game-over screen
        pass
    
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
        self.sprite_left = import_sprite("assets/pacman/left")
        self.sprite_right = import_sprite("assets/pacman/right")
        self.sprite_up = import_sprite("assets/pacman/up")
        self.sprite_down = import_sprite("assets/pacman/down")
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

class World:
    def __init__(self, screen):
        self.screen = screen
        self.player = Pac(1, 1)
        self.ghosts = []
        self.walls = []
        self.berries = []
        self._generate_world()
        self.game_over = False
        self.reset_pos = False
        self.player_score = 0
        self.game_level = 1
        
		    def _generate_world(self):
        # Generate walls, berries, ghosts based on the map
        for y_index, row in enumerate(MAP):
            for x_index, cell in enumerate(row):
                if cell == "1":
                    self.walls.append(Rect(x_index * CHAR_SIZE, y_index * CHAR_SIZE, CHAR_SIZE, CHAR_SIZE))
                elif cell in "B":
                    self.berries.append(Berry(x_index, y_index))
                elif cell in "spo":
                    self.ghosts.append(Ghost(x_index, y_index, color=cell))

    def update(self):
        if not self.game_over:
            keys = {
                "left": pygame.key.get_pressed()[pygame.K_LEFT],
                "right": pygame.key.get_pressed()[pygame.K_RIGHT],
                "up": pygame.key.get_pressed()[pygame.K_UP],
                "down": pygame.key.get_pressed()[pygame.K_DOWN]
            }
            
            # Move player
            self.player.animate(keys, self.walls)

            # Check collisions between player and berries
            for berry in self.berries:
                if self.player.rect.colliderect(berry):
                    self.player.pac_score += berry.value
                    self.berries.remove(berry)

            # Check collisions with ghosts
            for ghost in self.ghosts:
                if self.player.rect.colliderect(ghost):
                    if not self.player.immune:
                        self.player.life -= 1
                        self.reset_pos = True
                        break
                    else:
                        self.player.pac_score += 100
                        self.ghosts.remove(ghost)

            # Handle game level progression and reset position
            if len(self.berries) == 0:
                self.game_level += 1
                self.player.move_to_start_pos()
                for ghost in self.ghosts:
                    ghost.move_to_start_pos()
                self.generate_new_level()

        if self.game_over:
            self.display_game_over_screen()

    def display_game_over_screen(self):
# Code to display "Game Over" screen with restart option
        font = pygame.font.SysFont("Arial", 24)
        game_over_text = font.render("Game Over", True, (255, 0, 0))
        restart_text = font.render("Press R to Restart", True, (255, 255, 255))

        self.screen.fill((0, 0, 0))  # Fill screen with black for Game Over
        self.screen.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 2 - 30))
        self.screen.blit(restart_text, (WIDTH // 2 - restart_text.get_width() // 2, HEIGHT // 2 + 10))

        pygame.display.update()

        # Wait for user to press R to restart
        while True:
            pressed_keys = pygame.key.get_pressed()
            if pressed_keys[pygame.K_r]:
                self.restart_level()
                break
            pygame.time.wait(100)  # Adding small delay to prevent key hold-up

    def restart_level(self):
        # Reset game state and restart level
        self.berries.empty()
        self.game_level = 1
        self.player.pac_score = 0
        self.player.life = 3
        self.reset_pos = False
        self._generate_world()  # Regenerate the world, walls, berries, etc.
        self.display.game_over()  # Reset game over display

    def _dashboard(self):
        # Update and show the HUD with score, lives, and level
        self.display.show_score(self.player.pac_score)
        self.display.show_life(self.player.life)
        self.display.show_level(self.game_level)

    def game_loop(self):
        # Main game loop where the actual gameplay occurs
        while True:
            if self.game_over:
                self.display_game_over_screen()
            else:
                self.update()

            # Update the screen
            pygame.display.update()
            pygame.time.Clock().tick(30)  # Limit to 30 frames per second

if __name__ == "__main__":
    screen = pygame.display.set_mode((WIDTH, HEIGHT + NAV_HEIGHT))  # Window size
    pygame.display.set_caption("PacMan")  # Set the window title
    world = World(screen)  # Create the game world
    world.game_loop()  # Start the main game loop


