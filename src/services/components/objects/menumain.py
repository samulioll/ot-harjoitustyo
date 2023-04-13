import pygame as pg
from .ui_element import UiElement


class MenuMain():
    """
    A class for the main menu.
    """

    def __init__(self):
        self.menu_items = pg.sprite.Group()
        self.menu_items.add(UiElement("full_main_menu_2", 0, 0))
        self.font = pg.font.SysFont("Arial", 50)
    
    def draw_level_info(self, level: tuple):
        info = "Level " + level[0] + " | " + level[1]
        text = self.font.render(info, True, (150,150,150), None)
        text_rect = text.get_rect()
        text_rect.x = 620
        text_rect.y = 450
        return text, text_rect
    
    def draw_show_levels(self):
        text = self.font.render("View all levels", True, (150,150,150), None)
        text_rect = text.get_rect()
        text_rect.x = 620
        text_rect.y = 600
        return text, text_rect
    
    def draw_show_highscores(self):
        text = self.font.render("View highscores", True, (150,150,150), None)
        text_rect = text.get_rect()
        text_rect.x = 620
        text_rect.y = 755
        return text, text_rect

    def draw_show_profiles(self):
        text = self.font.render("View save slots", True, (150,150,150), None)
        text_rect = text.get_rect()
        text_rect.x = 620
        text_rect.y = 905
        return text, text_rect

