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
        level_matrix = level
        board = Board(level_matrix)

        # Game loop
        while self.running:
            # Player inputs
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.started = True
                    self.dragging = True
                    self.selected = self.game_logic.selected(pygame.mouse.get_pos())
                    print("Dragging:", self.dragging, self.selected)
                if event.type == pygame.MOUSEBUTTONUP:
                    self.dragging = False
                    self.selected = None
                    print("Dragging:", self.dragging, self.selected)
                
                if self.dragging and event.type == pygame.MOUSEMOTION:
                    print("moving")
                    board.move_car(self.selected, pygame.mouse.get_pos())



            # Draw screen
            self.display.fill((255,255,255))
            board.background.draw(self.display)
            board.cars.draw(self.display)

            pygame.display.update()

