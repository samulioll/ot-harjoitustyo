from .engine import Engine
from . import initialize
from .views import mainmenu, levelselect, game, postgame, highscores, profileselect
from .components import profile_manager

def main():
    """
    The main function which starts the game engine and the view manager.
    """
    app = Engine(initialize.caption)
    views = {"PROFILESELECT"     : profileselect.ProfileSelect(),
             "MAINMENU"    : mainmenu.MainMenu(),
             "LEVELSELECT" : levelselect.LevelSelect(),
             "GAME"        : game.Game(),
             "POSTGAME"    : postgame.PostGame(),
             "HIGHSCORES"  : highscores.HighScores()}
    app.view_manager.initialize_views(views, "PROFILESELECT")
    app.main()