import pygame as pg
from resources.services import tools
from resources.logicunits.scores_menu_logic import HighscoresMenuLogic
from resources.ui.sprites.ui_element import UiElement
from resources.services.view_manager import View


class HighScores(View):
    """ The view for the high scores state. """

    def __init__(self):
        View.__init__(self)
        self.logic = HighscoresMenuLogic()
        self.next = None
        self.selected_level = None
        self.hovering = None
        self.general_menu_items = pg.sprite.Group()
        self.level_menu_items = pg.sprite.Group()
        self.general_menu_items.add(UiElement("full_level_menu_1", 0, 0))
        self.level_menu_items.add(
            UiElement("full_highscores_single_level_view_1", 0, 0))

    def input_handler(self, event):
        """ Event type handling and sending event to logic unit for processing.

        Args:
            event: Pygame event
        """

        mouse_pos = tools.scale_mouse_pos(pg.mouse.get_pos(), self.scale)
        #print(mouse_pos)
        if event.type == pg.MOUSEBUTTONDOWN:
            if self.selected_level:
                self.selected_level = self.logic.handle_show_level(
                    mouse_pos, self.selected_level)
            else:
                info = self.logic.get_selected_level(mouse_pos)
                self.next, self.done, self.selected_level = info[0], info[1], info[2]
        if event.type == pg.MOUSEMOTION:
            self.hovering = self.logic.select_level(mouse_pos)

    def draw(self, surface):
        """ Handles which state to draw.

        Args:
            surface: The given surface to draw the box onto.
        """

        if not self.selected_level:
            self.draw_level_select(surface)
        else:
            self.draw_level_highscores(surface)

    def draw_level_select(self, surface):
        """ Draws the level selection state.

        Args:
            surface: The given surface to draw the box onto.
        """

        self.general_menu_items.draw(surface)
        self.draw_levels(surface)

    def draw_level_highscores(self, surface):
        """ Draws the level specific high scores state.

        Args:
            surface: The given surface to draw the box onto.
        """

        self.level_menu_items.draw(surface)

        font = pg.font.SysFont("Arial", 50)
        text_lvl = font.render(str(self.selected_level), True, (0, 0, 0), None)
        lvl_width = text_lvl.get_width()
        300, 505
        surface.blit(text_lvl, ((300 - (lvl_width/2)), 505))

        ordered = self.logic.level_scores(self.selected_level)
        y_bonus = 0
        for score in ordered:
            text_name = font.render(score[0], True, (0, 0, 0), None)
            text_moves = font.render(str(score[1]), True, (0, 0, 0), None)
            surface.blit(text_name, (630, 425 + y_bonus))
            surface.blit(text_moves, (920, 425 + y_bonus))
            y_bonus += 100

    def draw_levels(self, surface):
        """ Creates the numbers for the levels.

        Args:
            surface: The given surface to draw the box onto.
        """

        start_x, start_y, extra_x = 240, 375, 76
        rows = {0: 0, 1: 133, 2: 271, 3: 414, 4: 554}
        numbers = self.add_levels(50, start_x, extra_x, start_y, rows)
        for number in numbers:
            surface.blit(number[0], number[1])

    def add_levels(self, total_levels: int, start_x: int, extra_x: int,
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
        font = pg.font.SysFont("Century Gothic", 50)
        for i in range(1, total_levels+1):
            number = str(i) if i >= 10 else "0"+str(i)
            if i == self.hovering:
                text = font.render(number, True, (100, 100, 100), None)
            else:
                text = font.render(number, True, (0, 0, 0), None)
            text_rect = text.get_rect()
            text_rect.x = start_x + (extra_x * ((i-1) % 10))
            text_rect.y = start_y + rows[((i-1) // 10)]
            numbers.append((text, text_rect))
        return numbers
