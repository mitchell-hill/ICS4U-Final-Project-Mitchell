#!/usr/bin/env python3

"""
Created by: Mitchel Hill
Created on: Jan 2025
This program runs the "Pacman" program on Pybadge.
"""

import stage
import ugame
import random

# Constants for the game
SCREEN_WIDTH = 160
SCREEN_HEIGHT = 128
TILE_SIZE = 16
PACMAN_RADIUS = 8
GHOST_RADIUS = 8
PELLET_RADIUS = 4
BERRY_RADIUS = 6

# Define some colors
YELLOW = 0xFFFF00
RED = 0xFF0000
WHITE = 0xFFFFFF
BLUE = 0x0000FF

# Define the map layout (1 = wall, 0 = open space, H = hole for teleportation)
MAP = [
    "##############################",
    "#............H.............#",
    "#.####.#####.####.#####.####.#",
    "#.####.#####.####.#####.####.#",
    "#............................#",
    "#.####.#####.####.#####.####.#",
    "#.####.#####.####.#####.####.#",
    "#........H.................#",
    "##############################"
]

# Hole locations (X, Y) coordinates on the map for teleportation
HOLES = [(1, 7), (7, 1)]  # (X1, Y1) on left side, (X2, Y2) on the right side

def game_scene() -> None:
    """
    This function is the main game_scene
    """
    
    # image banks for CircuitPython
    image_bank_background = stage.Bank.from_bmp16("mt_game_studio.bmp")

    image_bank_sprites = stage.Bank.from_bmp16("sprite_sheet.bmp")

    # set the background to image 0 in the image bank
    #   and the size (10x8 tiles of size 16x16)
    background = stage.Grid(image_bank_background, 10, 8, 16)

    # create a stage for background to show up on
    #   and set the frame rate to 60fps
    game = stage.Stage(ugame.display, 60)

    game.layers = [background]

    # Map rendering: Translate the map string to actual grid tiles
    for y in range(len(MAP)):
        for x in range(len(MAP[y])):
            if MAP[y][x] == "#":  # Wall tile
                background.tile(x, y, 1)  # Assuming wall tiles are at index 1
            elif MAP[y][x] == ".":  # Open space
                background.tile(x, y, 0)  # Assuming open space tiles are at index 0
            elif MAP[y][x] == "H":  # Hole tile for teleportation
                background.tile(x, y, 4)  # Assuming hole tiles are at index 4

    # Create Pac-Man (yellow circle)
    pacman = stage.Sprite(image_bank_sprites, 0)
    pacman.x = 50  # Pacman starting X position
    pacman.y = 50  # Pacman starting Y position
    game.layers.append(pacman)

    # Create one ghost (red circle)
    ghost = stage.Sprite(image_bank_sprites, 1)
    ghost.x = 100  # Ghost starting X position
    ghost.y = 50   # Ghost starting Y position
    game.layers.append(ghost)

    # Create pellets
    pellets = []
    for i in range(5):  # Create 5 pellets
        pellet = stage.Sprite(image_bank_sprites, 2)
        pellet.x = random.randint(0, SCREEN_WIDTH - TILE_SIZE)
        pellet.y = random.randint(0, SCREEN_HEIGHT - TILE_SIZE)
        pellets.append(pellet)
        game.layers.append(pellet)


    # repeat forever, game loop
    while True:
        # Handle player input
        keys = ugame.buttons()
        if keys & ugame.K_UP:  # Move Pac-Man up
            pacman.y -= 2
        if keys & ugame.K_DOWN:  # Move Pac-Man down
            pacman.y += 2
        if keys & ugame.K_LEFT:  # Move Pac-Man left
            pacman.x -= 2
        if keys & ugame.K_RIGHT:  # Move Pac-Man right
            pacman.x += 2

        # Teleportation logic: Check if Pac-Man enters a hole
        for hole in HOLES:
            hole_x, hole_y = hole
            hole_tile_x = hole_x * TILE_SIZE
            hole_tile_y = hole_y * TILE_SIZE
            # Check if Pac-Man collides with a hole (tile H)
            if abs(pacman.x - hole_tile_x) < TILE_SIZE and abs(pacman.y - hole_tile_y) < TILE_SIZE:
                # Teleport Pac-Man to the corresponding hole on the other side
                if hole == (1, 7):  # Left side hole
                    pacman.x = 7 * TILE_SIZE  # Move to right hole
                    pacman.y = 1 * TILE_SIZE
                elif hole == (7, 1):  # Right side hole
                    pacman.x = 1 * TILE_SIZE  # Move to left hole
                    pacman.y = 7 * TILE_SIZE

        # Update ghost movement (simple random movement)
        ghost.x += random.choice([-1, 1]) * 2
        ghost.y += random.choice([-1, 1]) * 2

        # Collision detection: Check if Pac-Man eats a pellet
        for pellet in pellets[:]:
            if abs(pacman.x - pellet.x) < TILE_SIZE and abs(pacman.y - pellet.y) < TILE_SIZE:
                pellets.remove(pellet)  # Remove the pellet from the list
                game.layers.remove(pellet)  # Remove it from the display

        # Refresh the display
        game.render()

if __name__ == "__main__":
    game_scene()
