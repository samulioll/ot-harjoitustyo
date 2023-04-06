import pygame as pg
from .ui_element import UiElement

class Menus():
    """
    A class for all the menus.
    """
    def __init__(self):
        self.select_profile = pg.sprite.Group()
        self.main_menu = pg.sprite.Group()
        self.post_game = pg.sprite.Group()

        self.initialize_main_menu()
        self.initialize__profile_select()
    
    def initialize_main_menu(self):
        full_menu = UiElement("full_main_menu_2", 0, 0)
        self.main_menu.add(full_menu)

    def initialize__profile_select(self):
        full_menu = UiElement("full_select_profile_2", 0, 0)
        self.select_profile.add(full_menu)
