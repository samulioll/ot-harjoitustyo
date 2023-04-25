import os
import pygame as pg

screensize = 1200

path_name = os.path.dirname(__file__)[:-7] + "assets/" + str(screensize)


class Car(pg.sprite.Sprite):
    """
    A class for all the cars.
    """

    def __init__(self, image_file, x_coord=0, y_coord=0):
        super().__init__()
        self.image = pg.image.load(
            os.path.join(path_name, image_file+".png")
        )
        self.rect = self.image.get_rect()
        self.rect.x = x_coord
        self.rect.y = y_coord

        # Set other relevant info
        self.name = image_file
        text = ""
        for char in self.name:
            if char.isalpha():
                text += char
        self.car_id = text.capitalize()[:-1]
        self.height = self.rect.h
        self.width = self.rect.w
        self.move_axis = "x" if self.width > self.height else "y"
