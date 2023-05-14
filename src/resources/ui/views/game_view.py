import pygame as pg
from resources.logicunits import game_logic
from resources.services import level_manager, tools
from resources.services.view_manager import View


class Game(View):
    """ The view for the game state. """

    def __init__(self):
        View.__init__(self)
        self.selected = False
        self.offset = 0
        self.next = "POSTGAME"
        self.logic = None
        self.moves = 0

    def initiate_level(self):
        """ Sets the board with the level matrix passed on from previous view. """

        levels = level_manager.Levels()
        self.moves = 0
        self.next = "POSTGAME"
        if self.profile:
            level_matrix = levels.get_layout(self.play_level)
            self.logic = game_logic.Board(level_matrix)

    def input_handler(self, event):
        """ Event type handling and sending event to logic unit for processing.

        Args:
            event: Pygame event
        """

        mouse_pos = tools.scale_mouse_pos(pg.mouse.get_pos(), self.scale)
        if event.type == pg.MOUSEBUTTONDOWN:
            if self.logic.get_clicked_button(mouse_pos, self.play_level) == "RESET":
                self.initiate_level()
            else:
                info = self.logic.get_clicked_button(
                    mouse_pos, self.play_level)
                self.next, self.done, self.play_level = info[0], info[1], info[2]
                self.selected = self.logic.get_selected(
                    mouse_pos)
                self.offset = (mouse_pos[0] % 100, mouse_pos[1] % 100)

        elif self.selected and event.type == pg.MOUSEMOTION:
            self.logic.move_car(self.selected, mouse_pos, self.offset)

        elif event.type == pg.MOUSEBUTTONUP:
            if self.selected:
                moved, self.done = self.logic.drop_car(self.selected)
                self.moves += moved
                if self.done:
                    self.profile.update_scores(
                        str(self.play_level), self.moves)
            self.selected, self.offset = None, 0

    def draw(self, surface):
        """ Draws the game view.

        Args:
            surface: The given surface to draw the box onto.
        """

        self.logic.background.draw(surface)
        self.logic.cars.draw(surface)
        self.draw_level_info(surface)

    def draw_level_info(self, surface):
        """ Draws the level info onto the game view.

        Args:
            surface: The given surface to draw the box onto.
        """

        font = pg.font.SysFont("Arial", 50)
        text_moves = font.render(str(self.moves), True, (0, 0, 0), None)
        moves_text = font.render("MOVES", True, (0, 0, 0), None)
        text_level = font.render(str(self.play_level), True, (0, 0, 0), None)
        moves_width = text_moves.get_width()
        surface.blit(text_moves, (755-moves_width, 918))
        surface.blit(moves_text, (775, 918))
        surface.blit(text_level, (450, 918))
