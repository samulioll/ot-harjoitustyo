import pygame
from sprites.player import Player

class Level:
    def __init__(self, level_layout):
        self.cell_size = 100
        self.offset = 300
        self.player = None
        self.background = pygame.sprite.Group()
        self.blocks = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()

        self._initialize_sprites(level_layout)
    
    def _initialize_sprites(self, level_layout):
        for y in range(6):
            for x in range(6):
                cell = level_layout[y][x]
                x_coord = x * self.cell_size + self.offset
                y_coord = y * self.cell_size + self.offset

                if cell == "P":
                    self.player = Player(x_coord, y_coord)

        self.all_sprites.add(
            self.background,
            self.blocks,
            self.player
        )
    
