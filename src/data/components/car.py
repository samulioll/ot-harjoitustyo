import pygame as pg
import os

path_name = os.path.dirname(__file__)

class Car(pg.sprite.Sprite):
    """
    A class for all the cars.
    """
    
    def __init__(self, image_file, x=0, y=0):
        super(Car, self).__init__()

        self.image = pg.image.load(
            os.path.join(path_name, ".", "assets", image_file+".png")
        )

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        # Set other relevant info
        self.name = image_file
        text = ""
        for char in self.name:
            if char.isalpha():
                text += char
        self.id = text.capitalize()[:-1]
        self.height = self.rect.h
        self.width = self.rect.w
        self.move_axis = "x" if self.width > self.height else "y"
