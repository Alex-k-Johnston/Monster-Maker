from PIL import Image
from generator import generate
import numpy as np

def create_array(template): 
    arr = np.array(template)
    height, width = np.shape(arr)
    sprite, width, height = generate(arr, width, height)
    sprite = create_image(sprite)
    return sprite
    
def create_image(sprite):
    sprite = Image.fromarray(np.uint8(sprite * 255))
    sprite = sprite.resize((sprite.size[0]*2, sprite.size[1]*2))

    return sprite.show()
    
    
