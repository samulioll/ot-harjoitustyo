import pygame as pg
from services.components.objects.menumain import MenuMain
from ..view_manager import View


class MainMenu(View):
    """
    The view for the main menu.
    """

    def __init__(self):
        View.__init__(self)
        self.menu = MenuMain()
        self.next = None

    def input_handler(self, event):
        """ Handles events and sets the next game view. """
        # print(pg.mouse.get_pos())
        if event.type == pg.MOUSEBUTTONDOWN:
            self.next, self.done = self.menu.get_clicked(pg.mouse.get_pos())
            if self.next == "GAME":
                self.play_level = self.profile.current_level()[0]
                if self.play_level > 10:
                    self.next, self.done = None, False
                    print("")
                    print("!! All levels solved !!")
                    print("")

    def draw(self, surface):
        """ Draws the menu on the surface given. """
        self.menu.menu_items.draw(surface)
        mouse_pos = pg.mouse.get_pos()

        if 270 <= mouse_pos[0] <= 565 and 450 <= mouse_pos[1] <= 500:
            text, text_rect = self.menu.draw_level_info(
                self.profile.current_level())
            surface.blit(text, text_rect)
        elif 380 <= mouse_pos[0] <= 565 and 600 <= mouse_pos[1] <= 650:
            text, text_rect = self.menu.draw_show_levels()
            surface.blit(text, text_rect)
        elif 180 <= mouse_pos[0] <= 565 and 755 <= mouse_pos[1] <= 805:
            text, text_rect = self.menu.draw_show_highscores()
            surface.blit(text, text_rect)
        elif 200 <= mouse_pos[0] <= 565 and 905 <= mouse_pos[1] <= 955:
            text, text_rect = self.menu.draw_show_profiles()
            surface.blit(text, text_rect)
