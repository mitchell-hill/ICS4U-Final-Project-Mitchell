# main.py
import ugame
import time
from settings import WIDTH, HEIGHT, NAV_HEIGHT
from world import World

class Main:
    def __init__(self):
        self.FPS = 30  # This FPS will be handled automatically by ugame, but we can set a value here for other purposes

    def main(self):
        world = World()  # Initialize the game world
        while True:
            # Handle input using ugame's button presses instead of terminal input
            pressed_key = None
            if ugame.button_is_pressed(ugame.BUTTON_UP):
                pressed_key = 'w'
            elif ugame.button_is_pressed(ugame.BUTTON_DOWN):
                pressed_key = 's'
            elif ugame.button_is_pressed(ugame.BUTTON_LEFT):
                pressed_key = 'a'
            elif ugame.button_is_pressed(ugame.BUTTON_RIGHT):
                pressed_key = 'd'
            elif ugame.button_is_pressed(ugame.BUTTON_SELECT):
                pressed_key = 'q'

            if pressed_key:  # If a button is pressed, update the game world
                world.update(pressed_key)

            # Check for exit condition (in this case, the "select" button is pressed)
            if pressed_key == 'q':
                print("Quitting the game...")
                break

            # Wait to simulate FPS delay (this is managed by ugame automatically, no need for time.sleep)
            ugame.display.update()

if __name__ == "__main__":
    play = Main()
    play.main()
