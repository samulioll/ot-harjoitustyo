import pygame as pg
import os

path_name = os.path.dirname(__file__)

class UiElement(pg.sprite.Sprite):
    """
    A class for all the UI elements.
    """

    def __init__(self, image_file, x=0, y=0):
        super().__init__()

        self.image = pg.image.load(
            os.path.join(path_name, ".", "assets", image_file+".png")
        )

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y