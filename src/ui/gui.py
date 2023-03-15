import pygame
from ui.board import Board

class Screen:
    """
    A class to determine what is shown on screen. For every possible screen there is a method to draw it.
    """

    def __init__(self, score_service, game_logic):
        self.score_service = score_service
        self.game_logic = game_logic
        self.display = pygame.display.set_mode((1200,1200))
        pygame.display.set_caption("RUSH HOUR")
        pygame.init()
    

    def game_view(self, player):
        """
        Main game view. Inputs are inspected and sent to game logic to check validity. Then the screen is updated.
        """
        self.running = True
        self.started = False
        level_matrix = [[0,0,0,0,0,0],
                        [0,0,0,0,0,0],
                        [0,"Red",0,"Yellow",0,0],
                        [0,0,0,0,0,0],
                        [0,0,0,0,0,0],
                        [0,0,0,0,0,0]]
        board = Board(level_matrix)

        # Game loop
        while self.running:
            # Player inputs
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.started = True
                    selected = self.game_logic.selected(pygame.mouse.get_pos())


            # Draw screen
            self.display.fill((255,255,255))
            board.all_sprites.draw(self.display)

            pygame.display.update()




if __name__ == "__main__":
    test = Screen("score", "logic")
    test.game_view("sam")
