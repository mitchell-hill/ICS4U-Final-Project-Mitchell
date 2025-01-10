# animation.py
import ugame

def import_sprite(path):
    """Manually load sprite frames into ugame and return them."""
    frame_list = []
    
    # List of filenames for the sprite frames.
    # You need to know these filenames ahead of time because `ugame` doesn't support directory walking.
    image_files = ["", "", ""]  # Replace with your actual image filenames

    for image in image_files:
        full_path = f"{path}/{image}"  # Construct the full path to the image
        sprite_image = ugame.display.load_image(full_path)  # Load the image using ugame's method
        frame_list.append(sprite_image)  # Add the image to the list
    
    return frame_list
