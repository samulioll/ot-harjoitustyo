from ui.gui import Screen
from services.game_logic import Game

level_matrix = [[0,0,0,0,0,0],
                [0,0,0,0,0,0],
                [0,"Red",0,"Yellow",0,0],
                [0,0,0,0,0,0],
                [0,0,0,0,0,0],
                [0,0,0,"Blue",0,0]]


game_logic = Game(level_matrix)
screen = Screen("score_service", game_logic)

screen.game_view("samuli", level_matrix)