import pygame as pg
from services.components.objects.menulevels import MenuLevels
from ..view_manager import View

class LevelSelect(View):
    """
    The view for the level select state.
    """
    def __init__(self):
        View.__init__(self)
        self.menu = MenuLevels()
        self.next = None

    def input_handler(self, event):
        """ Handles events and sends commands for the menu to process. """
        #print(pg.mouse.get_pos())
        if event.type == pg.MOUSEBUTTONDOWN:
            mouse_pos = pg.mouse.get_pos()
            if 430 <= mouse_pos[0] <= 770 and 1050 <= mouse_pos[1] <= 1100:
                self.next = "MAINMENU"
                self.done = True
            else:
                selected_level = self.menu.select_level(mouse_pos, self.profile)
                if selected_level:
                    self.next = "GAME"
                    self.done = True

    def draw(self, surface):
        """ Draws the menu on the surface given. """
        self.menu.menu_items.draw(surface)

        for number in self.menu.draw_levels(self.profile):
            surface.blit(number[0], number[1])
