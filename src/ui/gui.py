import pygame
from ui.board import Board
from ui.menus import Menus

class Screen:
    """
    A class to determine what is shown on screen. For every possible screen there is a method to draw it.
    """

    def __init__(self, score_service, game_logic):
        self.score_service = score_service
        self.game_logic = game_logic
        self.display = pygame.display.set_mode((1200,1200))
        self.menu = Menus()
        self.active_profile = None
        pygame.display.set_caption("RUSH HOUR")
        pygame.init()
    

    def main_loop(self):
        """
        Main loop responsible for running the game.
        """
        # Loop
        while True:
            if not self.active_profile:
                self.select_profile_view()

            self.main_menu_view()


            # Draw screen
            self.display.fill((255,255,255))
            pygame.draw.rect(self.display, (0,150,0), (300,300,600,600))
            pygame.display.update()
    

    def select_profile_view(self):
        """
        Screen where you select the active player profile.
        """
        while not self.active_profile:
            for event in pygame.event.get():
                # Player inputs
                if event.type == pygame.QUIT:
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    self.active_profile = self.game_logic.select_profile(mouse_pos)
                # Draw screen
                self.display.fill((255,255,255))
                pygame.draw.rect(self.display, (100,100,200), (300,300,600,600))
                font = pygame.font.SysFont("Arial", 35)
                text = font.render("Profile", True, (0,0,0))
                self.display.blit(text, (300,300))
                pygame.display.update()

    
    def main_menu_view(self):
        """
        Main menu.
        """
        level_matrix = [[0,0,0,"Yellow",0,0],
                [0,0,0,"Yellow-1",0,0],
                [0,"Red","Red-1","Yellow-2",0,0],
                [0,0,0,0,0,0],
                [0,0,0,0,0,0],
                [0,0,0,"Blue","Blue-1",0]]

        # Loop
        while True:
            # Player inputs
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if self.game_logic.main_menu_continue_game(mouse_pos):
                        self.game_view("Sam", level_matrix)
                    elif self.game_logic.main_menu_level_selector(mouse_pos):
                        pass
                    elif self.game_logic.main_menu_high_scores(mouse_pos):
                        pass

            # Draw screen
            self.display.fill((255,255,255))
            pygame.draw.rect(self.display, (0,0,0), (300,300,600,600))
            pygame.display.update()


    def level_selector_view(self):
        """
        Level selector screen.
        """
        pass


    def game_view(self, player, level_matrix):
        """
        Main game view. Inputs are inspected and sent to game logic to check validity. Then the screen is updated.
        """
        self.running = True
        self.started = False
        self.solved = False
        self.dragging = False
        self.selected = None
        self.offset = 0
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
                    self.selected = self.game_logic.selected(mouse_pos, board.level_layout)
                    self.offset = (mouse_pos[0] % 100, mouse_pos[1] % 100)

                if event.type == pygame.MOUSEBUTTONUP:
                    if self.selected:
                        self.solved = board.drop_car(self.selected)
                    self.selected = None
                    self.offset = 0
                    print(board.level_layout)
                
                if self.selected and event.type == pygame.MOUSEMOTION:
                    board.move_car(self.selected, pygame.mouse.get_pos(), self.offset)
                    
            # Draw screen
            self.display.fill((255,255,255))
            board.background.draw(self.display)
            board.cars.draw(self.display)
            pygame.display.update()

            # Check status
            if self.solved:
                self.running = False
                print("Solved")
                self.solved_view()

    
    def solved_view(self):
        """ 
        Screen shown after solving a puzzle.
        """
        self.running = True

        # Loop
        while self.running:
            # Player inputs
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            # Draw screen
            self.display.fill((255,255,255))
            pygame.draw.rect(self.display, (0,0,0), (300,300,600,600))

            pygame.display.update()
