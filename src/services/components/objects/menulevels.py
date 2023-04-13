import pygame as pg
from .ui_element import UiElement


class MenuLevels():
    """
    A class for the high scores menu.
    """

    def __init__(self):
        self.menu_items = pg.sprite.Group()
        self.menu_items.add(UiElement("full_level_menu_1", 0, 0))
        self.font = pg.font.SysFont("Century Gothic", 50)

    def draw_levels(self, surface, profile):
        solved = len(profile.scores)
        next = str(solved + 1) if solved > 9 else "0" + str(solved + 1)
        numbers = []
        start_x = 240
        extra_x = 76
        start_y = 375
        extra_y = 135
        rows = {0: 0, 1: 133, 2: 271, 3: 414, 4: 554}

        for i in range(1, solved+1):
            number = str(i) if i >= 10 else "0"+str(i)
            text = self.font.render(number, True, (0, 0, 0), None)
            text_rect = text.get_rect()
            text_rect.x = start_x + (extra_x * ((i-1) % 10)) 
            text_rect.y = start_y + rows[((i-1) // 10)]
            numbers.append((text, text_rect))
        
        text = self.font.render(next, True, (0, 150, 0), None)
        text_rect = text.get_rect()
        text_rect.x = start_x + (extra_x * ((i-1) % 10)) + extra_x
        text_rect.y = start_y + rows[((i-1) // 10)]
        numbers.append((text, text_rect))

        for i in range(solved+2, 51):
            number = str(i) if i >= 10 else "0"+str(i)
            text = self.font.render(number, True, (150, 150, 150), None)
            text_rect = text.get_rect()
            text_rect.x = start_x + (extra_x * ((i-1) % 10)) 
            text_rect.y = start_y + rows[((i-1) // 10)]
            numbers.append((text, text_rect))
        
        return numbers

    def select_level(self, mouse_pos, profile):
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
        
        for row, range in rows.items():
            if range[0] <= mouse_pos[1] <= range[1]:
                lvl_row = row
        for col, range in cols.items():
            if range[0] <= mouse_pos[0] <= range[1]:
                lvl_col = col

        level = (lvl_row * 10) + lvl_col

        if level <= len(profile.scores) + 1:
            return level
        else: return None
        