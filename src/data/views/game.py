import pygame as pg
from .. import view_manager
from ..components import board


class Game(view_manager._View):
    def __init__(self):
        view_manager._View.__init__(self)
        self.level = [[0,0,0,"Yellow",0,0],
                      [0,0,0,"Yellow-1",0,0],
                      [0,"Red","Red-1","Yellow-2",0,0],
                      [0,0,0,0,0,0],
                      [0,0,0,0,0,0],
                      [0,0,0,"Blue","Blue-1",0]]
        self.started = False
        self.selected = False
        self.offset = 0
        self.next = "MAINMENU"

        self.moves = 0

    def initialize_board(self, level):
        self.board = board.Board(level)

    def input_handler(self, event, profile):
        """
        Arguments:
            event: pygame event
        """
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
            self.selected = None
            self.offset = 0

    def draw(self, surface, profile):
        """
        Argument:
            surface: pygame surface
        """
        self.board.background.draw(surface)
        self.board.cars.draw(surface)


