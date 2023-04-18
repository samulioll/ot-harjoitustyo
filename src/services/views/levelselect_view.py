import pygame as pg
from services.logicunits.levelsmenulogic import LevelsMenuLogic
from components.sprites.ui_element import UiElement
from ..view_manager import View


class LevelSelect(View):
    """
    The view for the level select state.
    """

    def __init__(self):
        View.__init__(self)
        self.logic = LevelsMenuLogic()
        self.next = None
        self.menu_items = pg.sprite.Group()
        self.menu_items.add(UiElement("full_level_menu_1", 0, 0))
        self.font = pg.font.SysFont("Century Gothic", 50)

    def input_handler(self, event):
        """ Handles events and sends commands for the menu to process. """
        # print(pg.mouse.get_pos())
        if event.type == pg.MOUSEBUTTONDOWN:
            mouse_pos = pg.mouse.get_pos()
            if 430 <= mouse_pos[0] <= 770 and 1050 <= mouse_pos[1] <= 1100:
                self.next = "MAINMENU"
                self.done = True
            else:
                selected_level = self.logic.select_level(
                    mouse_pos, self.profile)
                if selected_level and selected_level <= 37:
                    self.next = "GAME"
                    self.play_level = selected_level
                    self.done = True
                else:
                    print("!! All levels solved !!")

    def draw(self, surface):
        """ Draws the menu on the surface given. """
        self.menu_items.draw(surface)

        for number in self.draw_levels():
            surface.blit(number[0], number[1])

    def draw_levels(self):
        """
        Creates the numbers for the levels.
        Color depends on the player's progress.
        """
        profile = self.profile
        solved = len(profile.scores)
        next_lvl = str(solved + 1) if solved >= 9 else "0" + str(solved + 1)
        start_x, start_y, extra_x = 240, 375, 76
        rows = {0: 0, 1: 133, 2: 271, 3: 414, 4: 554}

        numbers = self.add_solved_levels(
            solved, start_x, extra_x, start_y, rows)
        numbers.append(self.add_current_level(
            solved, next_lvl, start_x, extra_x, start_y, rows))
        self.add_unsolved_levels(
            solved, start_x, extra_x, start_y, rows, numbers)
        return numbers

    def add_solved_levels(self, solved, start_x, extra_x, start_y, rows):
        """ Returns a list of texts for solved levels. """
        numbers = []
        for i in range(1, solved+1):
            number = str(i) if i >= 10 else "0"+str(i)
            text = self.font.render(number, True, (0, 0, 0), None)
            text_rect = text.get_rect()
            text_rect.x = start_x + (extra_x * ((i-1) % 10))
            text_rect.y = start_y + rows[((i-1) // 10)]
            numbers.append((text, text_rect))
        return numbers

    def add_current_level(self, solved, next_lvl, start_x, extra_x, start_y, rows):
        """ Returns text for current next unsolved level."""
        text = self.font.render(next_lvl, True, (0, 150, 0), None)
        text_rect = text.get_rect()
        text_rect.x = start_x + (extra_x * ((solved) % 10))
        text_rect.y = start_y + rows[((solved) // 10)]
        return (text, text_rect)

    def add_unsolved_levels(self, solved, start_x, extra_x, start_y, rows, numbers):
        """ Creates text for unsolved levels and adds to given list. """
        for i in range(solved+2, 51):
            number = str(i) if i >= 10 else "0"+str(i)
            text = self.font.render(number, True, (180, 180, 180), None)
            text_rect = text.get_rect()
            text_rect.x = start_x + (extra_x * ((i-1) % 10))
            text_rect.y = start_y + rows[((i-1) // 10)]
            numbers.append((text, text_rect))
