import pygame as pg
from resources.logicunits import game_logic
from resources.services import level_manager
from resources.services.view_manager import View


class Game(View):
    """
    The view for the game state.
    """

    def __init__(self):
        View.__init__(self)
        self.selected = False
        self.offset = 0
        self.next = "POSTGAME"
        self.logic = None
        self.moves = 0

    def initiate_level(self):
        """ Gets the next level and sets the board. """
        levels = level_manager.Levels()
        self.moves = 0
        self.next = "POSTGAME"
        if self.profile:
            curr_level = str(self.play_level)
            level_matrix = levels.levels[curr_level]
            print("Level:", curr_level)
            self.logic = game_logic.Board(level_matrix)

    def input_handler(self, event):
        """ Handles events and sends commands to the board instance. """
        #print(pg.mouse.get_pos())
        if event.type == pg.MOUSEBUTTONDOWN:
            mouse_pos = pg.mouse.get_pos()
            if self.logic.get_clicked_button(mouse_pos, self.play_level) == "RESET":
                self.initiate_level()
            else:
                info = self.logic.get_clicked_button(mouse_pos, self.play_level)
                self.next, self.done, self.play_level = info[0], info[1], info[2]
                self.selected = self.logic.get_selected(
                    mouse_pos)
                self.offset = (mouse_pos[0] % 100, mouse_pos[1] % 100)
        elif self.selected and event.type == pg.MOUSEMOTION:
            self.logic.move_car(self.selected, pg.mouse.get_pos(), self.offset)
        elif event.type == pg.MOUSEBUTTONUP:
            if self.selected:
                moved, self.done = self.logic.drop_car(self.selected)
                self.moves += moved
                print("Moves:", self.moves)
                if self.done:
                    self.profile.update_scores(
                        str(self.play_level), self.moves)
            self.selected, self.offset = None, 0

    def draw(self, surface):
        """ Draws the board on the surface given. """
        self.logic.background.draw(surface)
        self.logic.cars.draw(surface)
        self.draw_level_info(surface)

    def draw_level_info(self, surface):
        """ Draws move count, time, and level info. """
        font = pg.font.SysFont("Arial", 50)
        text_moves = font.render(str(self.moves), True, (0, 0, 0), None)
        moves_text = font.render("MOVES", True, (0, 0, 0), None)
        text_level = font.render(str(self.play_level), True, (0, 0, 0), None)
        surface.blit(text_moves, (725, 918))
        surface.blit(moves_text, (775, 918))
        surface.blit(text_level, (450, 918))
