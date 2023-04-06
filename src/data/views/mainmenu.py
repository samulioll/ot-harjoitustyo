import pygame as pg
from .. import view_manager
from data.components.objects import menus

class MainMenu(view_manager._View):
    """
    The view for the main menu.
    """
    def __init__(self):
        view_manager._View.__init__(self)
        self.menu = menus.Menus()

    def input_handler(self, event):
        """ Handles events and sets the next game view. """
        #print(pg.mouse.get_pos())
        if event.type == pg.MOUSEBUTTONDOWN:
            mouse_pos = pg.mouse.get_pos()
            if 270 <= mouse_pos[0] <= 565 and 450 <= mouse_pos[1] <= 500:
                self.next = "GAME"
                self.done = True
            elif 380 <= mouse_pos[0] <= 565 and 600 <= mouse_pos[1] <= 650:
                self.next = "LEVELSELECT"
                self.done = True
            elif 180 <= mouse_pos[0] <= 565 and 755 <= mouse_pos[1] <= 805:
                self.next = "HIGHSCORES"
                self.done = True
            elif 200 <= mouse_pos[0] <= 565 and 905 <= mouse_pos[1] <= 955:
                self.next = "PROFILESELECT"
                self.done = True
    
    def draw(self, surface):
        """ Draws the menu on the surface given. """
        self.menu.main_menu.draw(surface)
