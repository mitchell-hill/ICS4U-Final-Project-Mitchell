# world.py
import time
import ugame
import stage

from settings import HEIGHT, WIDTH, NAV_HEIGHT, CHAR_SIZE, MAP, PLAYER_SPEED
from pac import Pac
from cell import Cell
from berry import Berry
from ghost import Ghost
from display import Display

class World:
    def __init__(self):
        self.player = None
        self.ghosts = []
        self.walls = []
        self.berries = []

        self.display = Display()

        self.game_over = False
        self.reset_pos = False
        self.player_score = 0
        self.game_level = 1

        self._generate_world()

    def _generate_world(self):
        """Setup game entities (walls, berries, ghosts, and player)"""
        for y_index, col in enumerate(MAP):
            for x_index, char in enumerate(col):
                if char == "1":  # walls
                    self.walls.append(Cell(x_index, y_index, CHAR_SIZE, CHAR_SIZE))
                elif char == " ":
                    self.berries.append(Berry(x_index, y_index, CHAR_SIZE // 4))
                elif char == "B":
                    self.berries.append(Berry(x_index, y_index, CHAR_SIZE // 2, is_power_up=True))
                elif char == "P":
                    self.player = Pac(x_index, y_index)

                elif char == "s":
                    self.ghosts.append(Ghost(x_index, y_index, "skyblue"))
                elif char == "p":
                    self.ghosts.append(Ghost(x_index, y_index, "pink"))
                elif char == "o":
                    self.ghosts.append(Ghost(x_index, y_index, "orange"))
                elif char == "r":
                    self.ghosts.append(Ghost(x_index, y_index, "red"))

    def get_pressed_key(self):
        """Check for user input via ugame buttons."""
        if ugame.button_is_pressed(ugame.BUTTON_UP):
            return "w"
        elif ugame.button_is_pressed(ugame.BUTTON_DOWN):
            return "s"
        elif ugame.button_is_pressed(ugame.BUTTON_LEFT):
            return "a"
        elif ugame.button_is_pressed(ugame.BUTTON_RIGHT):
            return "d"
        return None

    def _dashboard(self):
        """Render game status (Life, Level, Score) on screen."""
        text = f"Life: {self.player.life} Level: {self.game_level} Score: {self.player.pac_score}"
        self.display.text(text, 10, HEIGHT - NAV_HEIGHT + 10, color=ugame.color(255, 255, 255))  # White color

    def _check_game_state(self):
        """Check game over condition or generate new level."""
        if self.player.life == 0:
            self.game_over = True

        if len(self.berries) == 0 and self.player.life > 0:
            self.game_level += 1
            for ghost in self.ghosts:
                ghost.move_speed += self.game_level
                ghost.move_to_start_pos()

            self.player.move_to_start_pos()
            self.player.direction = (0, 0)
            self.player.status = "idle"
            self.generate_new_level()

    def generate_new_level(self):
        """Generate new berries for the new level."""
        for y_index, col in enumerate(MAP):
            for x_index, char in enumerate(col):
                if char == " ":
                    self.berries.append(Berry(x_index, y_index, CHAR_SIZE // 4))
                elif char == "B":
                    self.berries.append(Berry(x_index, y_index, CHAR_SIZE // 2, is_power_up=True))

        time.sleep(2)

    def restart_level(self):
        """Restart the level, reset positions, and regenerate berries."""
        self.berries.clear()
        for ghost in self.ghosts:
            ghost.move_to_start_pos()
        self.game_level = 1
        self.player.pac_score = 0
        self.player.life = 3
        self.player.move_to_start_pos()
        self.player.direction = (0, 0)
        self.player.status = "idle"
        self.generate_new_level()

    def update(self):
        """Update the game state: Player movement, collision, score, etc."""
        if not self.game_over:
            # Player movement
            pressed_key = self.get_pressed_key()
            if pressed_key:
                self.player.animate(pressed_key, self.walls)

            # Handle teleportation logic for PacMan
            if self.player.sprite.x < 0:
                self.player.sprite.x = WIDTH - CHAR_SIZE
            elif self.player.sprite.x >= WIDTH:
                self.player.sprite.x = 0

            # PacMan eats berries
            for berry in self.berries:
                if self.player.sprite.colliderect(berry.sprite):
                    if berry.power_up:
                        self.player.immune_time = 150  # Timer for immunity
                        self.player.pac_score += 50
                    else:
                        self.player.pac_score += 10
                    berry.kill()  # Remove berry from the screen

            # Check if PacMan collides with ghosts
            for ghost in self.ghosts:
                if self.player.sprite.colliderect(ghost.sprite):
                    if not self.player.immune:
                        self.player.life -= 1
                        self.reset_pos = True
                    else:
                        ghost.move_to_start_pos()
                        self.player.pac_score += 100

        self._check_game_state()

        # Render all game objects (walls, berries, ghosts, and player)
        for wall in self.walls:
            wall.update()
        for berry in self.berries:
            berry.update()
        for ghost in self.ghosts:
            ghost.update()

        self.player.update()

        # Display game status (score, lives, level)
        self._dashboard()

        # If game over, display the "Game Over" message and restart prompt
        if self.game_over:
            self.display.text("Game Over! Press 'r' to restart", 10, HEIGHT // 2, color=ugame.color(255, 0, 0))  # Red color
            pressed_key = self.get_pressed_key()
            if pressed_key == "r":
                self.game_over = False
                self.restart_level()
