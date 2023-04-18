import pygame as pg
from ..view_manager import View
from services.logicunits import gamelogic
from services import level_manager


class Game(View):
    """
    The view for the game state.
    """

    def __init__(self):
        View.__init__(self)
        self.started = False
        self.selected = False
        self.offset = 0
        self.next = None
        self.logic = None
        self.moves = 0
        self.time = "00:00"

    def initiate_level(self):
        """ Gets the next level and sets the board. """
        levels = level_manager.Levels()
        self.moves = 0
        if self.profile:
            curr_level = str(self.play_level)
            level_matrix = levels.levels[curr_level]
            print("Level:", curr_level)
            self.logic = gamelogic.Board(level_matrix)

    def input_handler(self, event):
        """ Handles events and sends commands to the board instance. """
        #print(pg.mouse.get_pos())
        if event.type == pg.MOUSEBUTTONDOWN:
            mouse_pos = pg.mouse.get_pos()
            if 430 <= mouse_pos[0] <= 565 and 1050 <= mouse_pos[1] <= 1100:
                self.initiate_level()
            elif 615 <= mouse_pos[0] <= 720 and 1050 <= mouse_pos[1] <= 1100:
                self.next, self.done, self.play_level = "MAINMENU", True, None
            self.started, self.selected = True, self.logic.get_selected(
                mouse_pos)
            self.offset = (mouse_pos[0] % 100, mouse_pos[1] % 100)
        elif self.selected and event.type == pg.MOUSEMOTION:
            self.logic.move_car(self.selected, pg.mouse.get_pos(), self.offset)
        elif event.type == pg.MOUSEBUTTONUP:
            if self.selected:
                moved, self.done = self.logic.drop_car(self.selected)
                self.moves += moved
                print("Moves:", self.moves)
                if self.done:
                    self.profile.update_scores(
                        str(self.play_level), (self.moves, 0))
                    self.next = "POSTGAME"
            self.selected, self.offset = None, 0

    def draw(self, surface):
        """ Draws the board on the surface given. """
        self.logic.background.draw(surface)
        self.logic.cars.draw(surface)
        moves, moves_text, level = self.logic.draw_level_info(
            self.moves, self.play_level
        )
        surface.blit(moves, (725, 918))
        surface.blit(moves_text, (775, 918))
        surface.blit(level, (450, 918))
