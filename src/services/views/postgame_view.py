import pygame as pg
from services.components.objects.menupost import MenuPost
from ..view_manager import View


class PostGame(View):
    """
    The view for the post game state.
    """

    def __init__(self):
        View.__init__(self)
        self.menu = MenuPost()
        self.next = None

    def input_handler(self, event):
        """ Handles events and sends commands to the board instance. """
        # print(pg.mouse.get_pos())
        if event.type == pg.MOUSEBUTTONDOWN:
            mouse_pos = pg.mouse.get_pos()
            if 450 <= mouse_pos[0] <= 580 and 650 <= mouse_pos[1] <= 690:
                if self.play_level < 10:
                    self.next = "GAME"
                    self.play_level += 1
                    self.done = True
                else:
                    print("")
                    print("!! All levels solved !!")
                    print("")
            elif 620 <= mouse_pos[0] <= 725 and 650 <= mouse_pos[1] <= 690:
                self.next = "MAINMENU"
                self.play_level = None
                self.done = True

    def draw(self, surface):
        """ Draws the post game menu on the surface given. """
        self.menu.menu_items.draw(surface)
