# berry.py
import ugame

class Berry:
    def __init__(self, row, col, size, is_power_up=False):
        self.power_up = is_power_up
        self.size = size
        self.abs_x = (row * size) + (size // 2)
        self.abs_y = (col * size) + (size // 2)

    def update(self):
        color = ugame.Color(255, 255, 0) if self.power_up else ugame.Color(255, 0, 0)
        ugame.display.draw_circle(self.abs_x, self.abs_y, self.size, color)
