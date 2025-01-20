from PIL import Image, ImageDraw

class Rect:
    """A rectangle with optional fill and outline, drawn using Pillow."""
    
    def __init__(self, x, y, width, height, fill=None, outline=None, stroke=1):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.fill = fill
        self.outline = outline
        self.stroke = stroke
    
    def draw(self, image):
        """Draw the rectangle on a given image."""
        draw = ImageDraw.Draw(image)
        
        # Draw outline if specified
        if self.outline:
            draw.rectangle(
                [self.x, self.y, self.x + self.width, self.y + self.height],
                outline=self.outline,
                width=self.stroke
            )
        
        # Fill the rectangle if a fill color is specified
        if self.fill:
            draw.rectangle(
                [self.x, self.y, self.x + self.width, self.y + self.height],
                fill=self.fill
            )


# Example usage:
if __name__ == "__main__":
    # Create a blank white image
    image = Image.new('RGB', (400, 300), color=(255, 255, 255))
    
    # Create a Rect object
    rect = Rect(50, 50, 100, 75, fill=(255, 0, 0), outline=(0, 255, 0), stroke=3)
    
    # Draw the rectangle on the image
    rect.draw(image)
    
    # Save the image to a file
    image.save("rectangle_image.png")
    
    # Display the image (this opens the default image viewer)
    image.show()
