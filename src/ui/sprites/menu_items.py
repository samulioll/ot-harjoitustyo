import pygame, os

path_name = os.path.dirname(__file__)

class Menu_item(pygame.sprite.Sprite):
    """
    A class for all the UI elements.
    """

    def __init__(self, image_file, x=0, y=0):
        super().__init__()

        # Create path to image
        self.image = pygame.image.load(
            os.path.join(path_name, "..", "assets", image_file+".png")
        )

        # Define block size
        self.rect = self.image.get_rect()

        # Set starting coordinates
        self.rect.x = x
        self.rect.y = y