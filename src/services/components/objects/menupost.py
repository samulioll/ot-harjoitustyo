import pygame as pg
from .ui_element import UiElement


class MenuPost():
    """
    A class for the post game menu.
    """

    def __init__(self):
        self.menu_items = pg.sprite.Group()

        self.menu_items.add(UiElement("post_game_box_1", 0, 0))
