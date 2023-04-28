import pygame as pg
from resources.services import tools
from resources.logicunits.lvl_menu_logic import LevelsMenuLogic
from resources.ui.sprites.ui_element import UiElement
from resources.services.view_manager import View


class LevelSelect(View):
    """ The view for the level select state. """

    def __init__(self):
        View.__init__(self)
        self.logic = LevelsMenuLogic()
        self.next = None
        self.menu_items = pg.sprite.Group()
        self.hovering = None
        self.menu_items.add(UiElement("full_level_menu_1", 0, 0))
        self.font = pg.font.SysFont("Century Gothic", 50)

    def input_handler(self, event):
        """ Event type handling and sending event to logic unit for processing.

        Args:
            event: Pygame event
        """

        mouse_pos = tools.scale_mouse_pos(pg.mouse.get_pos(), self.scale)
        #print(mouse_pos)
        if event.type == pg.MOUSEBUTTONDOWN:
            info = self.logic.get_clicked_button(mouse_pos, self.profile)
            self.next, self.done, self.play_level = info[0], info[1], info[2]
        if event.type == pg.MOUSEMOTION:
            self.hovering = self.logic.select_level(mouse_pos, self.profile)

    def draw(self, surface):
        """ Draws the level select menu.

        Args:
            surface: The given surface to draw the box onto.
        """

        self.menu_items.draw(surface)

        for number in self.draw_levels():
            surface.blit(number[0], number[1])

    def draw_levels(self):
        """ Creates the numbers for the levels.
            Color depends on the player's progress.

        Args:
            surface: The given surface to draw the box onto.
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

    def add_solved_levels(self, solved: int, start_x: int, extra_x: int,
                          start_y: int, rows: dict):
        """ Returns a list of texts for solved levels.

        Args:
            solved (int): Number of solved levels.
            start_x (int): X coordinate of the first element in a row.
            extra_x (int): X coordinate bonus to create columns.
            start_y (int): Y coordinate of the first row.
            rows (int): Dictionary with Y coordinates for all of the rows.

        Returns:
            A list of text objects of all solved levels.
        """

        numbers = []
        for i in range(1, solved+1):
            number = str(i) if i >= 10 else "0"+str(i)
            if i == self.hovering:
                text = self.font.render(number, True, (100, 100, 100), None)
            else:
                text = self.font.render(number, True, (0, 0, 0), None)
            text_rect = text.get_rect()
            text_rect.x = start_x + (extra_x * ((i-1) % 10))
            text_rect.y = start_y + rows[((i-1) // 10)]
            numbers.append((text, text_rect))
        return numbers

    def add_current_level(self, solved: int, next_lvl: int, start_x: int, extra_x: int,
                          start_y: int, rows: dict):
        """ Returns a text object for the next unsolved level.

        Args:
            solved (int): Number of solved levels.
            start_x (int): X coordinate of the first element in a row.
            extra_x (int): X coordinate bonus to create columns.
            start_y (int): Y coordinate of the first row.
            rows (int): Dictionary with Y coordinates for all of the rows.

        Returns:
            A list of text objects with all solved levels added to it.
        """

        if int(next_lvl) == self.hovering:
            text = self.font.render(next_lvl, True, (100, 200, 100), None)
        else:
            text = self.font.render(next_lvl, True, (0, 150, 0), None)
        text_rect = text.get_rect()
        text_rect.x = start_x + (extra_x * ((solved) % 10))
        text_rect.y = start_y + rows[((solved) // 10)]
        return (text, text_rect)

    def add_unsolved_levels(self, solved: int, start_x: int, extra_x: int,
                            start_y: int, rows: dict, numbers: list):
        """ Returns a list with texts for unsolved levels added to it.

        Args:
            solved (int): Number of solved levels.
            start_x (int): X coordinate of the first element in a row.
            extra_x (int): X coordinate bonus to create columns.
            start_y (int): Y coordinate of the first row.
            rows (int): Dictionary with Y coordinates for all of the rows.
            numbers (list): A list with text objects for solved levels

        Returns:
            A list of text objects with all solved levels added to it.
        """

        for i in range(solved+2, 51):
            number = str(i) if i >= 10 else "0"+str(i)
            text = self.font.render(number, True, (180, 180, 180), None)
            text_rect = text.get_rect()
            text_rect.x = start_x + (extra_x * ((i-1) % 10))
            text_rect.y = start_y + rows[((i-1) // 10)]
            numbers.append((text, text_rect))
