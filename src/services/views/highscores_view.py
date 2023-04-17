import pygame as pg
from services.components.objects.menuhighscores import MenuHighscores
from ..view_manager import View


class HighScores(View):
    def __init__(self):
        View.__init__(self)
        self.menu = MenuHighscores()
        self.next = None

    def input_handler(self, event):
        """ Handles events and sends commands for the menu to process. """
        # print(pg.mouse.get_pos())
