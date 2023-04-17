import pygame as pg
from .ui_element import UiElement


class MenuHighscores():
    """
    A class for the high scores menu.
    """

    def __init__(self):
        self.general_menu_items = pg.sprite.Group()
        self.level_menu_items = pg.sprite.Group()
        self.general_menu_items.add(UiElement("full_level_menu_1", 0, 0))
        self.level_menu_items.add(UiElement("full_highscores_single_level_view_1", 0, 0))
        self.font = pg.font.SysFont("Century Gothic", 50)
