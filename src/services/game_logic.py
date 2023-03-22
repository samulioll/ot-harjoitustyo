import pygame

class Game:
    def __init__(self):
        pass

    def selected(self, mouse_coords, level_layout):
        # If clicked on the board
        if 300 <= mouse_coords[0] <= 900 and 300 <= mouse_coords[1] <= 900:
            clicked_x = (mouse_coords[0] - 300) // 100
            clicked_y = (mouse_coords[1] - 300) // 100
            return level_layout[clicked_y][clicked_x]

    def check_movement(self, car):
        colliding = pygame.sprite.spritecollide(car)
    
    def select_profile(self, mouse_coords):
        if 300 <= mouse_coords[0] <= 900 and 300 <= mouse_coords[1] <= 900:
            return "Samuli"
        else:
            return None

            
    def main_menu_continue_game(self, mouse_coords):
        if 300 <= mouse_coords[0] <= 900 and 300 <= mouse_coords[1] <= 900:
            return True
        else:
            return False
