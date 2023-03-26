import os
import pygame as pg
from . import view_manager

class Engine():
    """
    Controls the core functions of the game.
    """
    def __init__(self, caption):
        self.display = pg.display.get_surface()
        self.caption = caption
        self.clock = pg.time.Clock()
        self.view_manager = view_manager.ViewManager()

        self.running = True


    def main(self):
        """ 
        The main loop of the program. 
        """
        while self.running:
            self.get_inputs()
            self.update()
            self.draw()

    def get_inputs(self):
        """
        Gets player inputs and sends them via the event handler to the current view.
        """
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False
            self.view_manager.event_handler(event)
    
    def update(self):
        self.view_manager.update()

    def draw(self):
        if not self.view_manager.view.done:
            self.view_manager.draw(self.display)
            pg.display.update()
