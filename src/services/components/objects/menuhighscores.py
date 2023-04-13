import pygame as pg
from .ui_element import UiElement


class MenuHighscores():
    """
    A class for the high scores menu.
    """

    def __init__(self):
        self.menu_items = pg.sprite.Group()

        self.menu_items.add(UiElement("full_main_menu_2", 0, 0))
