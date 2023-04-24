import pygame as pg
from resources.logicunits.resolution_menu_logic import ResolutionMenuLogic
from resources.ui.sprites.ui_element import UiElement
from resources.services.view_manager import View


class Resolution(View):
    """
    The view for changing game window size.
    """

    def __init__(self):
        View.__init__(self)
        pg.display.set_mode((505, 305))
        self.logic = ResolutionMenuLogic()
        self.next = None
        self.font = pg.font.SysFont("Arial", 50)
        self.menu_items = pg.sprite.Group()
        self.menu_items.add(UiElement("full_resolution_view_1", 0, 0))

    def input_handler(self, event):
        """ Handles events and sets the next game view. """
        print(pg.mouse.get_pos())
        if event.type == pg.MOUSEBUTTONDOWN:
            self.next, self.done, self.scale = self.logic.get_clicked(pg.mouse.get_pos(), self.profile)
            pg.display.set_mode((self.scale*1200, self.scale*1200))

    def draw(self, surface):
        """ Draws the menu on the surface given. """
        self.menu_items.draw(surface)
        mouse_pos = pg.mouse.get_pos()
