import pygame as pg
from .. import view_manager
from ..components import menus

class PostGame(view_manager._View):
    """
    The view for the post game state.
    """
    def __init__(self):
        view_manager._View.__init__(self)
        self.menu = menus.Menus

    def input_handler(self, event):
        """ Handles events and sends commands to the board instance. """
        pass

    def draw(self, surface):
        """ Draws the post game menu on the surface given. """
        self.board.background.draw(surface)
        self.board.cars.draw(surface)

