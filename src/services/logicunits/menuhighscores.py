import pygame as pg
from components.sprites.ui_element import UiElement
from services import profile_manager


class MenuHighscores():
    """
    A class for the high scores menu.
    """

    def __init__(self):
        self.general_menu_items = pg.sprite.Group()
        self.level_menu_items = pg.sprite.Group()
        self.general_menu_items.add(UiElement("full_level_menu_1", 0, 0))
        self.level_menu_items.add(UiElement("full_highscores_single_level_view_1", 0, 0))
        self.font = pg.font.SysFont("Century Gothic", 50)
        self.all_profiles = profile_manager.AllProfiles()

    def draw_levels(self, profile):
        """
        Creates the numbers for the levels.
        Color depends on the player's progress.
        """
        solved = len(profile.scores)
        start_x, start_y, extra_x = 240, 375, 76
        rows = {0: 0, 1: 133, 2: 271, 3: 414, 4: 554}

        numbers = self.add_solved_levels(
            solved, start_x, extra_x, start_y, rows)
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

    def add_unsolved_levels(self, solved, start_x, extra_x, start_y, rows, numbers):
        """ Creates text for unsolved levels and adds to given list. """
        for i in range(solved+1, 51):
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

        lvl_row, lvl_col = -1, -1
        for row, limits in rows.items():
            if limits[0] <= mouse_pos[1] <= limits[1]:
                lvl_row = row
        for col, limits in cols.items():
            if limits[0] <= mouse_pos[0] <= limits[1]:
                lvl_col = col
        if lvl_row >= 0 and lvl_col >= 0:
            level = (lvl_row * 10) + lvl_col
            if level <= len(profile.scores) + 1:
                return level
            return None
        return None

    def draw_info(self, selected, level):
        font = pg.font.SysFont("Arial", 50)
        texts = []
        move_col = 0 if selected == "MOVES" else 150
        text_moves = font.render("MOVES", True, (move_col, move_col, move_col), None)
        moves_rect = text_moves.get_rect()
        moves_rect.x, moves_rect.y = 215, 740
        texts.append((text_moves, moves_rect))
        time_col = 0 if selected == "TIME" else 150
        text_time = font.render("TIME", True, (time_col, time_col, time_col), None)
        time_rect = text_time.get_rect()
        time_rect.x, time_rect.y = 240, 810
        texts.append((text_time, time_rect))
        text_level = font.render(str(level), True, (0, 0, 0), None)
        level_rect = text_level.get_rect()
        level_rect.x, level_rect.y = 285, 505
        texts.append((text_level, level_rect))
        return texts

    def draw_level_highscores(self, level):
        pass
