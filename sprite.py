# sprite.py 
 
class Sprite:
	def __init__(self, image, x, y):
		self.image = image
		self.x = x
		self.y = y

	def move(self, dx, dy):
		self.x += dx
		self.y += dy 
