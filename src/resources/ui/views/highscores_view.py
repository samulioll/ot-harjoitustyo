import pygame as pg
from resources.logicunits.menuhighscores import HighscoresMenuLogic
from resources.ui.sprites.ui_element import UiElement
from resources.services.view_manager import View


class HighScores(View):
    def __init__(self):
        View.__init__(self)
        self.logic = HighscoresMenuLogic()
        self.next = None
        self.selected_level = None
        self.general_menu_items = pg.sprite.Group()
        self.level_menu_items = pg.sprite.Group()
        self.general_menu_items.add(UiElement("full_level_menu_1", 0, 0))
        self.level_menu_items.add(UiElement("full_highscores_single_level_view_1", 0, 0))

    def input_handler(self, event):
        """ Handles events and sends commands for the menu to process. """
        #print(pg.mouse.get_pos())
        if event.type == pg.MOUSEBUTTONDOWN:
            mouse_pos = pg.mouse.get_pos()
            if self.selected_level:
                self.logic.handle_show_level(mouse_pos)
            else:
                info = self.logic.get_selected_level(mouse_pos, self.profile)
                self.next, self.done, self.selected_level = info[0], info[1], info[2]

    def draw(self, surface):
        """ Draws the menu on the surface given. """
        if not self.selected_level:
            self.draw_level_select(surface)
        else:
            self.draw_level_highscores(surface)

    def draw_level_select(self, surface):
        self.general_menu_items.draw(surface)
        self.draw_levels(surface)

    def draw_level_highscores(self, surface):
        self.level_menu_items.draw(surface)

    def draw_levels(self, surface):
        """
        Creates the numbers for the levels.
        Color depends on the player's progress.
        """
        solved = len(self.profile.scores)
        start_x, start_y, extra_x = 240, 375, 76
        rows = {0: 0, 1: 133, 2: 271, 3: 414, 4: 554}
        numbers = self.add_solved_levels(
            solved, start_x, extra_x, start_y, rows)
        self.add_unsolved_levels(
            solved, start_x, extra_x, start_y, rows, numbers)
        for number in numbers:
            surface.blit(number[0], number[1])

    def add_solved_levels(self, solved, start_x, extra_x, start_y, rows):
        """ Returns a list of texts for solved levels. """
        numbers = []
        font = pg.font.SysFont("Century Gothic", 50)
        for i in range(1, solved+1):
            number = str(i) if i >= 10 else "0"+str(i)
            text = font.render(number, True, (0, 0, 0), None)
            text_rect = text.get_rect()
            text_rect.x = start_x + (extra_x * ((i-1) % 10))
            text_rect.y = start_y + rows[((i-1) // 10)]
            numbers.append((text, text_rect))
        return numbers

    def add_unsolved_levels(self, solved, start_x, extra_x, start_y, rows, numbers):
        """ Creates text for unsolved levels and adds to given list. """
        font = pg.font.SysFont("Century Gothic", 50)
        for i in range(solved+1, 51):
            number = str(i) if i >= 10 else "0"+str(i)
            text = font.render(number, True, (180, 180, 180), None)
            text_rect = text.get_rect()
            text_rect.x = start_x + (extra_x * ((i-1) % 10))
            text_rect.y = start_y + rows[((i-1) // 10)]
            numbers.append((text, text_rect))
