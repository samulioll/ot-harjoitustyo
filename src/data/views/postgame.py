import pygame as pg
from .. import view_manager
from data.components.objects import menus

class PostGame(view_manager._View):
    """
    The view for the post game state.
    """
    def __init__(self):
        view_manager._View.__init__(self)
        self.menu = menus.Menus()

    def input_handler(self, event):
        """ Handles events and sends commands to the board instance. """
        #print(pg.mouse.get_pos())
        if event.type == pg.MOUSEBUTTONDOWN:
            mouse_pos = pg.mouse.get_pos()
            if 450 <= mouse_pos[0] <= 580 and 650 <= mouse_pos[1] <= 690:
                self.next = "GAME"
                self.done = True
            elif 620 <= mouse_pos[0] <= 725 and 650 <= mouse_pos[1] <= 690:
                self.next = "MAINMENU"
                self.done = True

    def draw(self, surface):
        """ Draws the post game menu on the surface given. """
        self.menu.post_game.draw(surface)
