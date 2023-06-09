import pygame as pg
from resources.services import tools
from resources.logicunits.postgame_logic import PostGameLogic
from resources.ui.sprites.ui_element import UiElement
from resources.services.view_manager import View


class PostGame(View):
    """ The view for the post game state. """

    def __init__(self):
        View.__init__(self)
        self.logic = PostGameLogic()
        self.next = None
        self.menu_items = pg.sprite.Group()
        self.menu_items.add(UiElement("post_game_box_1", 0, 0))

    def input_handler(self, event):
        """ Event type handling and sending event to logic unit for processing.

        Args:
            event: Pygame event
        """

        mouse_pos = tools.scale_mouse_pos(pg.mouse.get_pos(), self.scale)
        if event.type == pg.MOUSEBUTTONDOWN:
            self.next, self.play_level, self.done = self.logic.get_next(
                mouse_pos, self.play_level)

    def draw(self, surface):
        """ Draws the post game menu.

        Args:
            surface: The given surface to draw the box onto.
        """

        self.menu_items.draw(surface)
