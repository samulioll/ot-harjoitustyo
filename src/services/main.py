from .engine import Engine
from . import initialize
from .views import game_view, highscores_view, levelselect_view
from .views import mainmenu_view, postgame_view, profileselect_view


def main():
    """
    The main function which starts the game engine and the view manager.
    """
    app = Engine(initialize.CAPTION)
    views = {"PROFILESELECT": profileselect_view.ProfileSelect(),
             "MAINMENU": mainmenu_view.MainMenu(),
             "LEVELSELECT": levelselect_view.LevelSelect(),
             "GAME": game_view.Game(),
             "POSTGAME": postgame_view.PostGame(),
             "HIGHSCORES": highscores_view.HighScores()}
    app.view_manager.initialize_views(views, "PROFILESELECT")
    app.main()
