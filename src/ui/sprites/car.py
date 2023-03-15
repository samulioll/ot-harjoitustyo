import pygame, os

# Path to this file's directory
path_name = os.path.dirname(__file__)

# Create the class for red car
class Car(pygame.sprite.Sprite):
    def __init__(self, image_file, x=0, y=0):
        super(Car, self).__init__()

        # Create path to image
        self.image = pygame.image.load(
            os.path.join(path_name, "..", "assets", image_file+".png")
        )

        # Define block size
        self.rect = self.image.get_rect()

        # Set starting coordinates
        self.rect.x = x
        self.rect.y = y

        # Set other relevant info
        self.name = image_file
        self.height = self.rect.h
