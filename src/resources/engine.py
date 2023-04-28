import pygame as pg
from resources.services.view_manager import ViewManager


class Engine():
    """ Controls the main loop of the game.

        Attributes:
            caption: Caption for the game window
    """

    def __init__(self, caption):
        self.surface = pg.Surface((1200, 1200))
        self.surf_rect = self.surface.get_rect()
        self.display = pg.display.get_surface()
        self.caption = caption
        self.clock = pg.time.Clock()
        self.view_manager = ViewManager()

        self.running = True

    def main(self):
        """ The main loop of the game. """

        while self.running:
            self.get_inputs()
            self.draw()
            self.update()

    def get_inputs(self):
        """ Gets player inputs and sends them via the event handler to the current view. """

        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False
            self.view_manager.event_handler(event)

    def update(self):
        """ Updates the current view. """

        self.view_manager.update()

    def draw(self):
        """ Draws the current view. """

        self.view_manager.draw(self.surface)
        surface, rect = self.set_scale(self.surface)
        self.display.blit(surface, rect)
        pg.display.update()

    def set_scale(self, surface):
        scale = self.view_manager.get_scale()
        surf = pg.transform.smoothscale(surface, (scale*1200, scale*1200))
        surf_rect = surf.get_rect()
        return (surf, surf_rect)
