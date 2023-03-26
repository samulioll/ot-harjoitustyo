import pygame as pg
from .ui_element import UiElement

class Menus():
    def __init__(self):
        self.select_profile = pg.sprite.Group()
        self.main_menu = pg.sprite.Group()
        self.post_game = pg.sprite.Group()

        self.initialize_main_menu()
    
    def initialize_main_menu(self):
        full_menu = UiElement("full_main_menu_1", 0, 0)
        self.main_menu.add(full_menu)