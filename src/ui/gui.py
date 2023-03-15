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
    

    def game_view(self, player, level):
        """
        Main game view. Inputs are inspected and sent to game logic to check validity. Then the screen is updated.
        """
        self.running = True
        self.started = False
        self.solved = False
        self.dragging = False
        self.selected = None
        self.offset = 0
        level_matrix = level
        board = Board(level_matrix)

        # Game loop
        while self.running:
            # Player inputs
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    self.started = True
                    self.dragging = True
                    self.selected = self.game_logic.selected(mouse_pos)
                    self.offset = (mouse_pos[0] % 100, mouse_pos[1] % 100)

                if event.type == pygame.MOUSEBUTTONUP:
                    self.dragging = False
                    self.selected = None
                    self.offset = 0
                
                if self.dragging and event.type == pygame.MOUSEMOTION:
                    board.move_car(self.selected, pygame.mouse.get_pos(), self.offset, self.game_logic)



            # Draw screen
            self.display.fill((255,255,255))
            board.background.draw(self.display)
            board.cars.draw(self.display)

            pygame.display.update()

