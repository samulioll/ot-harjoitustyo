import pygame, os

# Path to this file's directory
path_name = os.path.dirname(__file__)

# Create the class for red car
class Player(pygame.sprite.Sprite):
    def __init__(self, x=0, y=0):
        super().__init__()

        # Create path to image
        self.image = pygame.image.load(
            os.path.join(path_name, "..", "assets", "player.png")
        )

        # Define block size
        self.rect = self.image.get_rect()

        # Set starting coordinates
        self.rect.x = x
        self.rect.y = y