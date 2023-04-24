import os
import pygame as pg

screensize = 1200

path_name = os.path.dirname(__file__)[:-7] + "assets/" + str(screensize)


class UiElement(pg.sprite.Sprite):
    """
    A class for all the UI elements.
    """
    def __init__(self, image_file, x_coord=0, y_coord=0):
        super().__init__()
        self.image = pg.image.load(
            os.path.join(path_name, image_file+".png")
        )
        self.rect = self.image.get_rect()
        self.rect.x = x_coord
        self.rect.y = y_coord
