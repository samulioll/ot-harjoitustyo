import pygame
from ui.sprites.boardbase import Boardbase

class Menus():
    def __init__(self):
        self.profiles = pygame.sprite.Group()

    def draw_profile_selector(self):
        samuli = pygame.rect(self.display, (150,0,0), (300,300,600,600))
        self.profiles.add(samuli)

