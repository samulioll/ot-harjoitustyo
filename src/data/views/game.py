import pygame as pg
from .. import view_manager
from ..components import board
from ..components import levels
from copy import deepcopy


class Game(view_manager._View):
    """
    The view for the game state.
    """
    def __init__(self):
        view_manager._View.__init__(self)
        self.levels = levels.Levels()
        self.started = False
        self.selected = False
        self.offset = 0
        self.next = "MAINMENU"
        self.moves = 0

    def initiate_level(self):
        """ Gets the next level and sets the board. """
        self.moves = 0
        try:
            curr_level = self.profile.current_level()
            level_matrix = self.levels.levels[curr_level]
            print("Level:", curr_level)
        except:
            level_matrix = self.levels.levels["1"]
            print("Level: 1")
        self.board = board.Board(level_matrix)


    def input_handler(self, event):
        """ Handles events and sends commands to the board instance. """
        if event.type == pg.MOUSEBUTTONDOWN:
            mouse_pos = pg.mouse.get_pos()
            self.started = True
            self.selected = self.board.get_selected(mouse_pos)
            self.offset = (mouse_pos[0] % 100, mouse_pos[1] % 100)
        elif self.selected and event.type == pg.MOUSEMOTION:
            self.board.move_car(self.selected, pg.mouse.get_pos(), self.offset)
        elif event.type == pg.MOUSEBUTTONUP:
            if self.selected:
                moved, self.done = self.board.drop_car(self.selected)
                if moved:
                    self.moves += 1
                    print("Moves:", self.moves)
                if self.done:
                    self.profile.update_scores(self.profile.current_level(), (self.moves, 0))
            self.selected = None
            self.offset = 0

    def draw(self, surface):
        """ Draws the board on the surface given. """
        self.board.background.draw(surface)
        self.board.cars.draw(surface)


