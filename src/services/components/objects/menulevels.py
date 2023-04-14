import pygame as pg
from .ui_element import UiElement

class MenuLevels():
    """
    A class for the levels logic menu.
    """

    def __init__(self):
        self.menu_items = pg.sprite.Group()
        self.menu_items.add(UiElement("full_level_menu_1", 0, 0))
        self.font = pg.font.SysFont("Century Gothic", 50)

    def draw_levels(self, profile):
        """
        Creates the numbers for the levels.
        Color depends on the player's progress.
        """
        solved = len(profile.scores)
        next_lvl = str(solved + 1) if solved >= 9 else "0" + str(solved + 1)
        start_x, start_y, extra_x = 240, 375, 76
        rows = {0: 0, 1: 133, 2: 271, 3: 414, 4: 554}

        numbers = self.add_solved_levels(solved, start_x, extra_x, start_y, rows)
        numbers.append(self.add_current_level(solved, next_lvl, start_x, extra_x, start_y, rows))
        self.add_unsolved_levels(solved, start_x, extra_x, start_y, rows, numbers)
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

    def select_level(self, mouse_pos, profile):
        """
        Returns the numerical value of the clicked level.
        """
        rows = {0: (360, 425),
                1: (493, 562),
                2: (632, 702),
                3: (772, 842),
                4: (914, 984)}
        cols = {1: (227, 295),
                2: (302, 370),
                3: (377, 446),
                4: (454, 520),
                5: (528, 596),
                6: (605, 672),
                7: (680, 748),
                8: (755, 824),
                9: (831, 898),
                10: (906, 975)}

        for row, limits in rows.items():
            if limits[0] <= mouse_pos[1] <= limits[1]:
                lvl_row = row
        for col, limits in cols.items():
            if limits[0] <= mouse_pos[0] <= limits[1]:
                lvl_col = col

        level = (lvl_row * 10) + lvl_col
        if level <= len(profile.scores) + 1:
            return level
        return None
