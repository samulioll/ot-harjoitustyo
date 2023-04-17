import pygame as pg
from services.components.objects.menuhighscores import MenuHighscores
from ..view_manager import View


class HighScores(View):
    def __init__(self):
        View.__init__(self)
        self.menu = MenuHighscores()
        self.next = None
        self.selected_level = None
        self.selected_score = None

    def input_handler(self, event):
        """ Handles events and sends commands for the menu to process. """
        #print(pg.mouse.get_pos())
        if event.type == pg.MOUSEBUTTONDOWN:
            mouse_pos = pg.mouse.get_pos()
            if self.selected_level:
                self.handle_show_level(mouse_pos)
            else:
                self.handle_select_level(mouse_pos)

    def handle_show_level(self, mouse_pos):
        if 215 <= mouse_pos[0] <= 395 and 740 <= mouse_pos[1] <= 790:
             self.selected_score = "MOVES"
        if 240 <= mouse_pos[0] <= 360 and 810 <= mouse_pos[1] <= 860:
             self.selected_score = "TIME"

    def handle_select_level(self, mouse_pos):
                if 430 <= mouse_pos[0] <= 770 and 1050 <= mouse_pos[1] <= 1100:
                    self.next = "MAINMENU"
                    self.done = True
                else:
                    self.selected_level = self.menu.select_level(
                        mouse_pos, self.profile)

    def draw(self, surface):
        """ Draws the menu on the surface given. """
        if not self.selected_level:
            self.draw_level_select(surface)
        else:
            self.draw_level_highscores(surface)

    def draw_level_select(self, surface):
            self.menu.general_menu_items.draw(surface)
            for number in self.menu.draw_levels(self.profile):
                surface.blit(number[0], number[1])

    def draw_level_highscores(self, surface):
            self.menu.level_menu_items.draw(surface)
            for text in self.menu.draw_info(self.selected_score, self.selected_level):
                surface.blit(text[0], text[1])
            # highscores = 