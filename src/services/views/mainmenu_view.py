import pygame as pg
from services.components.objects.mainmenulogic import MainMenuLogic
from services.components.objects.ui_element import UiElement
from ..view_manager import View


class MainMenu(View):
    """
    The view for the main menu.
    """

    def __init__(self):
        View.__init__(self)
        self.logic = MainMenuLogic()
        self.next = None
        self.font = pg.font.SysFont("Arial", 50)
        self.menu_items = pg.sprite.Group()
        self.menu_items.add(UiElement("full_main_menu_2", 0, 0))

    def input_handler(self, event):
        """ Handles events and sets the next game view. """
        # print(pg.mouse.get_pos())
        if event.type == pg.MOUSEBUTTONDOWN:
            self.next, self.done = self.logic.get_clicked(pg.mouse.get_pos())
            if self.next == "GAME":
                self.play_level = self.profile.current_level()[0]
                if self.play_level > 37:
                    self.next, self.done = None, False
                    print("!! All levels solved !!")

    def draw(self, surface):
        """ Draws the menu on the surface given. """
        self.menu_items.draw(surface)
        mouse_pos = pg.mouse.get_pos()

        if 270 <= mouse_pos[0] <= 565 and 450 <= mouse_pos[1] <= 500:
            text, text_rect = self.draw_level_info()
            surface.blit(text, text_rect)
        elif 380 <= mouse_pos[0] <= 565 and 600 <= mouse_pos[1] <= 650:
            text, text_rect = self.draw_show_levels()
            surface.blit(text, text_rect)
        elif 180 <= mouse_pos[0] <= 565 and 755 <= mouse_pos[1] <= 805:
            text, text_rect = self.draw_show_highscores()
            surface.blit(text, text_rect)
        elif 200 <= mouse_pos[0] <= 565 and 905 <= mouse_pos[1] <= 955:
            text, text_rect = self.draw_show_profiles()
            surface.blit(text, text_rect)

    def draw_level_info(self):
        level = self.profile.current_level()
        info = "Level " + str(level[0]) + " | " + level[1]
        text = self.font.render(info, True, (150, 150, 150), None)
        text_rect = text.get_rect()
        text_rect.x = 620
        text_rect.y = 450
        return text, text_rect

    def draw_show_levels(self):
        text = self.font.render("View all levels", True, (150, 150, 150), None)
        text_rect = text.get_rect()
        text_rect.x = 620
        text_rect.y = 600
        return text, text_rect

    def draw_show_highscores(self):
        font = pg.font.SysFont("Arial", 50)
        text = font.render("View highscores", True, (150, 150, 150), None)
        text_rect = text.get_rect()
        text_rect.x = 620
        text_rect.y = 755
        return text, text_rect

    def draw_show_profiles(self):
        font = pg.font.SysFont("Arial", 50)
        text = font.render("View save slots", True, (150, 150, 150), None)
        text_rect = text.get_rect()
        text_rect.x = 620
        text_rect.y = 905
        return text, text_rect
