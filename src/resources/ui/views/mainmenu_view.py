import pygame as pg
from resources.logicunits.mainmenu_logic import MainMenuLogic
from resources.ui.sprites.ui_element import UiElement
from resources.services.view_manager import View


class MainMenu(View):
    """ The view for the main menu. """

    def __init__(self):
        View.__init__(self)
        self.logic = MainMenuLogic()
        self.next = None
        self.font = pg.font.SysFont("Arial", 50)
        self.menu_items = pg.sprite.Group()
        self.menu_items.add(UiElement("full_main_menu_2", 0, 0))

    def input_handler(self, event):
        """ Event type handling and sending event to logic unit for processing.

        Args:
            event: Pygame event
        """

        # print(pg.mouse.get_pos())
        if event.type == pg.MOUSEBUTTONDOWN:
            self.next, self.done = self.logic.get_clicked(pg.mouse.get_pos())
            if self.next == "GAME":
                self.play_level = self.profile.current_level()[0]
                if self.play_level > 40:
                    self.next, self.done = None, False
                    print("!! All levels solved !!")

    def draw(self, surface):
        """ Draws the main menu.

        Args:
            surface: The given surface to draw the box onto.
        """

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
        """ Draws the next level info if hovering over CONTINUE. """

        level = self.profile.current_level()
        info = "Level " + str(level[0]) + " | " + level[1]
        text = self.font.render(info, True, (150, 150, 150), None)
        text_rect = text.get_rect()
        text_rect.x = 620
        text_rect.y = 450
        return text, text_rect

    def draw_show_levels(self):
        """ Draws the level select info if hovering over LEVELS. """

        text = self.font.render("View all levels", True, (150, 150, 150), None)
        text_rect = text.get_rect()
        text_rect.x = 620
        text_rect.y = 600
        return text, text_rect

    def draw_show_highscores(self):
        """ Draws the high scores info if hovering over HIGHSCORES. """

        font = pg.font.SysFont("Arial", 50)
        text = font.render("View highscores", True, (150, 150, 150), None)
        text_rect = text.get_rect()
        text_rect.x = 620
        text_rect.y = 755
        return text, text_rect

    def draw_show_profiles(self):
        """ Draws the profile select info if hovering over SWITCH PROFILE. """
        
        font = pg.font.SysFont("Arial", 50)
        text = font.render("View save slots", True, (150, 150, 150), None)
        text_rect = text.get_rect()
        text_rect.x = 620
        text_rect.y = 905
        return text, text_rect
