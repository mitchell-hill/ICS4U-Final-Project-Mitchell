# display.py
import ugame
import stage  # `ugame.stage` for handling sprites and layers
from settings import WIDTH, HEIGHT  # Adjust as per your game settings

class Display:
    def __init__(self):
        # Initialize the display
        self.game_display = ugame.display
        self.game_display.set_background_color(0)  # Set background color (black)
        
        # Create text objects (using `ugame`'s stage for drawing text on the screen)
        self.font = stage.FONT  # Using the built-in font
        self.game_over_font = stage.FONT  # Can use a different font for Game Over text
        
        self.text_color = 0xFFFFFF  # White text (hex code)
        
        # Initialize the game screen (e.g., for score, level, life)
        self.score_text = stage.Text(self.font, 10, 10, text="Score: 0", color=self.text_color)
        self.level_text = stage.Text(self.font, 10, 30, text="Level: 1", color=self.text_color)
        self.life_text = stage.Text(self.font, 10, 50, text="Lives: 3", color=self.text_color)

        # Create a list for all displayed texts
        self.display_texts = [self.score_text, self.level_text, self.life_text]

    def show_life(self, life):
        """Display the number of lives left using a text representation."""
        self.life_text.text = f"Lives: {life}"

    def show_level(self, level):
        """Display the current level."""
        self.level_text.text = f"Level: {level}"

    def show_score(self, score):
        """Display the current score."""
        self.score_text.text = f"Score: {score}"

    def game_over(self):
        """Display the 'Game Over' message."""
        game_over_text = stage.Text(self.game_over_font, WIDTH // 2 - 40, HEIGHT // 2 - 20, 
                                    text="GAME OVER!!", color=0xFF0000)  # Red text for Game Over
        restart_text = stage.Text(self.game_over_font, WIDTH // 2 - 40, HEIGHT // 2 + 20, 
                                  text='Press "R" to Restart', color=0xFF0000)
        self.game_display.draw_text(game_over_text)  # Draw 'Game Over' on the screen
        self.game_display.draw_text(restart_text)  # Draw restart text on the screen
        
        # For user to see and press "r" to restart
        while True:
            key = ugame.buttons.read()
            if key & ugame.K_X:  # "R" button pressed (change this based on actual input)
                return True  # Restart the game
            ugame.game.display.update()

    def update(self):
        """Update the game display."""
        # Draw current scores, levels, and lives
        self.game_display.clear()
        for text in self.display_texts:
            self.game_display.draw_text(text)  # Draw each text object
        
        # Refresh the screen with the updated elements
        self.game_display.update()

