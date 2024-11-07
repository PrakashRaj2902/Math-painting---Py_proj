import numpy as np
from PIL import Image

#Object where all the shapes are going to be drawn"
class Canvas:

    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = color

        #Create a 3d numpy array of zeros
        self.data = np.zeros((self.height, self.width, 3), dtype=np.uint8)
        #change [0,0,0] with user given values for color
        self.data[:] = self.color

    def make(self, image_path):
        #converts the current array into an image file
        img = Image.fromarray(self.data, 'RGB')
        img.save(image_path)
