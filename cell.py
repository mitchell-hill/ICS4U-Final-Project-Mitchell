# cell.py
import ugame
import stage

class Cell:
    def __init__(self, row, col, length, width):
        self.width = length
        self.height = width
        self.id = (row, col)
        self.abs_x = row * self.width  # Absolute x position based on grid
        self.abs_y = col * self.height  # Absolute y position based on grid

        self.occupying_piece = None  # Holds whatever object occupies the cell (e.g., berry, player, etc.)
        
        # Create a rectangle shape for the cell, for rendering purposes
        self.cell_rect = stage.Sprite(None, self.abs_x, self.abs_y, width=self.width, height=self.height)  # Example rectangle placeholder

    def update(self, game_display):
        """Simulate the cell by visually updating its status."""
        # If the cell is occupied, display its content (e.g., berry or player)
        if self.occupying_piece:
            self.occupying_piece.update(game_display)  # Update the occupying piece (like berry or player)
        
        # Draw the cell itself on the screen (if needed)
        # For visual purposes, fill the cell with color (optional)
        game_display.fill_rect(self.abs_x, self.abs_y, self.width, self.height, 0x0000FF)  # Example: Blue color for the cell background
        
        # You can add additional logic here to show different types of cells (empty, berry, etc.)
        if self.occupying_piece is not None:
            # Assuming the occupying_piece has a `draw` or `update` method that renders it
            self.occupying_piece.update(game_display)  # Update (draw) the occupying object (e.g., berry or PacMan)
        else:
            # Cell is empty - maybe draw a border or leave it blank
            pass

    def set_occupying_piece(self, piece):
        """Sets the piece (e.g., berry, player) occupying this cell."""
        self.occupying_piece = piece  # This is where you assign a piece (like a berry or player) to the cell

    def remove_occupying_piece(self):
        """Clears the cell's occupation."""
        self.occupying_piece = None  # Clear the occupying piece (when it's eaten by PacMan, for example)
