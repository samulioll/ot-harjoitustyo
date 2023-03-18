import pygame

class Game:
    def __init__(self, level_matrix):
        self.matrix = level_matrix

    def selected(self, mouse_coords):
        # If clicked on the board
        if 300 <= mouse_coords[0] <= 900 and 300 <= mouse_coords[1] <= 900:
            clicked_x = (mouse_coords[0] - 300) // 100
            clicked_y = (mouse_coords[1] - 300) // 100
            return self.matrix[clicked_y][clicked_x]

    def check_movement(self, car):
        colliding = pygame.sprite.spritecollide(car)
            

