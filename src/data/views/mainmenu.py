import pygame as pg
from .. import view_manager
from ..components import menus

class MainMenu(view_manager._View):
    def __init__(self):
        view_manager._View.__init__(self)
        self.menu = menus.Menus()

    def input_handler(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            mouse_pos = pg.mouse.get_pos()
            if 260 <= mouse_pos[0] <= 565 and 470 <= mouse_pos[1] <= 525:
                self.next = "GAME"
                self.done = True
            elif 390 <= mouse_pos[0] <= 560 and 680 <= mouse_pos[1] <= 720:
                self.next = "LEVELSELECT"
                self.done = True
            elif 180 <= mouse_pos[0] <= 565 and 890 <= mouse_pos[1] <= 930:
                self.next = "HIGHSCORES"
                self.done = True
    
    def draw(self, surface):
        """
        Argument:
            surface: pygame surface
        """
        self.menu.main_menu.draw(surface)
