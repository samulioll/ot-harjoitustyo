import pygame as pg
from ..view_manager import View
from ..components import board
from ..components import level_manager


class Game(View):
    """
    The view for the game state.
    """

    def __init__(self):
        View.__init__(self)
        self.levels = level_manager.Levels()
        self.started = False
        self.selected = False
        self.offset = 0
        self.next = None

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
        # print(pg.mouse.get_pos())
        if event.type == pg.MOUSEBUTTONDOWN:
            mouse_pos = pg.mouse.get_pos()
            if 430 <= mouse_pos[0] <= 565 and 1050 <= mouse_pos[1] <= 1100:
                self.initiate_level()
            elif 615 <= mouse_pos[0] <= 720 and 1050 <= mouse_pos[1] <= 1100:
                self.next = "MAINMENU"
                self.done = True
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
                    self.profile.update_scores(
                        self.profile.current_level(), (self.moves, 0))
                    self.next = "POSTGAME"
            self.selected = None
            self.offset = 0

    def draw(self, surface):
        """ Draws the board on the surface given. """
        self.board.background.draw(surface)
        self.board.cars.draw(surface)
