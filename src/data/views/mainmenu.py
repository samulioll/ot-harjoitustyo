import pygame as pg
from .. import view_manager
from ..components import menus

class Menu(view_manager._View):
    def __init__(self):
        view_manager._View.__init__(self)
        self.menu = menus.Menus()

    def input_handler(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            mouse_pos = pg.mouse.get_pos()
            if 260 <= mouse_pos[0] <= 565 and 470 <= mouse_pos[1] <= 525:
                self.next = "GAME"
                self.done = True
    
    def draw(self, surface):
        """ Draw screen. """
        self.menu.main_menu.draw(surface)
