import pygame as pg
from services.components.objects.menuhighscores import MenuHighscores
from ..view_manager import View


class HighScores(View):
    def __init__(self):
        View.__init__(self)
        self.menu = MenuHighscores()
