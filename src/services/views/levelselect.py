import pygame as pg
from services.components.objects.menulevels import MenuLevels
from ..view_manager import View


class LevelSelect(View):
    def __init__(self):
        View.__init__(self)
        self.menu = MenuLevels()
