# pac.py
import ugame
from settings import CHAR_SIZE, PLAYER_SPEED
from animation import import_sprite  # If necessary, for actual graphics later

class Pac:
    def __init__(self, row, col):
        self.sprite = ugame.Sprite(import_sprite("assets/pac/idle")[0])  # Start with idle sprite
        self.sprite.x = row * CHAR_SIZE  # Set initial X position
        self.sprite.y = col * CHAR_SIZE  # Set initial Y position

        # Animation assets (use the `import_sprite` to load animations)
        self._import_character_assets()
        self.frame_index = 0
        self.animation_speed = 0.5  # Speed of the animation
        self.image = self.animations["idle"][self.frame_index]  # Current image

        # Movement settings
        self.pac_speed = PLAYER_SPEED
        self.immune_time = 0  # For immunity timer
        self.immune = False  # Pac-Man's immunity status

        # Movement directions (up, down, left, right)
        self.directions = {'left': (-PLAYER_SPEED, 0), 'right': (PLAYER_SPEED, 0), 'up': (0, -PLAYER_SPEED), 'down': (0, PLAYER_SPEED)}
        self.keys = {'left': 'a', 'right': 'd', 'up': 'w', 'down': 's'}  # Key mappings for movement
        self.direction = (0, 0)  # Current movement direction

        # Pac-Man status and game state
        self.status = "idle"  # Can be idle, moving, or power_up
        self.life = 3  # Initial lives
        self.pac_score = 0  # Starting score

    def _import_character_assets(self):
        """Simulate character asset loading (sprites or other animation assets)."""
        character_path = "assets/pac/"
        self.animations = {
            "up": [],    # Animation frames for moving up
            "down": [],  # Animation frames for moving down
            "left": [],  # Animation frames for moving left
            "right": [], # Animation frames for moving right
            "idle": [],  # Animation frames for idle
            "power_up": []  # Power-up animation frames
        }

        # Load animation assets (for now, these are empty lists, but you can load frame data)
        for animation in self.animations.keys():
            full_path = character_path + animation
            self.animations[animation] = import_sprite(full_path)  # If sprite import logic is needed

    def _is_collide(self, x, y, walls_collide_list):
        """Check if Pac-Man collides with a wall at the next position."""
        new_x = self.sprite.x + x
        new_y = self.sprite.y + y
        # Check for collision with any wall using `colliderect()`
        for wall in walls_collide_list:
            if self.sprite.colliderect(wall.sprite):  # Assume `wall` is a sprite
                return True
        return False

    def move_to_start_pos(self):
        """Reset Pac-Man's position to the starting coordinates."""
        self.sprite.x = self.sprite.x
        self.sprite.y = self.sprite.y

    def animate(self, pressed_key, walls_collide_list):
        """Handle Pac-Man's movement and animation."""
        animation = self.animations[self.status]  # Get the current status animation

        # Update the frame for animation
        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0
        self.image = animation[int(self.frame_index)]  # Update image for the current frame

        # Handle movement based on user input
        for key, key_value in self.keys.items():
            if pressed_key == key_value and not self._is_collide(*self.directions[key], walls_collide_list):
                self.direction = self.directions[key]
                self.status = key if not self.immune else "power_up"
                break  # Move in the direction once a valid key is pressed

        # Update position if no collision occurs
        if not self._is_collide(*self.direction, walls_collide_list):
            self.sprite.x += self.direction[0]
            self.sprite.y += self.direction[1]
            self.status = self.status if not self.immune else "power_up"
        
        # Handle collision (if any)
        if self._is_collide(*self.direction, walls_collide_list):
            self.status = "idle" if not self.immune else "power_up"

    def update(self):
        """Update Pac-Man's status, immunity, and other related logic."""
        # Handle immunity (for power-up effect)
        self.immune = True if self.immune_time > 0 else False
        self.immune_time -= 1 if self.immune_time > 0 else 0  # Decrement immunity time

        # For graphical simulation, no need for text-based position updates
        pass
