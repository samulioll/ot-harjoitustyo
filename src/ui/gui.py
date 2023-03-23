import pygame
from ui.board import Board
from ui.menus import Menus

class Screen:
    """
    Runs the core game loop. For every possible screen there is a method to draw it.
    """
    def __init__(self, score_service, game_logic):
        self.score_service = score_service
        self.game_logic = game_logic
        self.menu = Menus()

        self.active_profile = None
        self.view = "profile"

        self.display = pygame.display.set_mode((1200,1200))
        pygame.display.set_caption("RUSH HOUR")
        pygame.init()
    

    def main_loop(self):
        """
        Main loop responsible for running the game.
        """
        # Loop
        while True:
            if self.view == "profile":
                self.select_profile_view()
            elif self.view == "main":
                self.main_menu_view()
            elif self.view == "game":
                self.game_view(self.active_profile)

            # Draw screen
            pygame.display.update()
    

    def select_profile_view(self):
        """
        Screen where you select the active player profile.
        """
        while self.view == "profile":
            # Player inputs
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    self.active_profile = self.game_logic.select_profile(mouse_pos)
                    if self.active_profile:
                        self.view = "main"

            # Draw screen
            self.menu.profile_menu_items.draw(self.display)
            pygame.display.update()

    
    def main_menu_view(self):
        """
        Main menu.
        """
        # Loop
        while self.view == "main":
            # Player inputs
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    print(mouse_pos)
                    if self.game_logic.main_menu_continue_game(mouse_pos):
                        self.view = "game"
                    elif self.game_logic.main_menu_level_selector(mouse_pos):
                        pass
                    elif self.game_logic.main_menu_high_scores(mouse_pos):
                        pass

            # Draw screen
            self.menu.main_menu_items.draw(self.display)
            pygame.display.update()


    def level_selector_view(self):
        """
        Level selector screen.
        """
        pass


    def game_view(self, profile):
        """
        Main game view. Inputs are inspected and sent to game logic to check validity. Then the screen is updated.
        """
        self.running = True
        self.started = False
        self.solved = False
        self.dragging = False
        self.selected = None
        self.offset = 0
        level_matrix = [[0,0,0,"Yellow",0,0],
                        [0,0,0,"Yellow-1",0,0],
                        [0,"Red","Red-1","Yellow-2",0,0],
                        [0,0,0,0,0,0],
                        [0,0,0,0,0,0],
                        [0,0,0,"Blue","Blue-1",0]]
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
