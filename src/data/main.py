from .engine import Engine
from . import initialize
from .views import mainmenu, profile, levelselect, game, postgame

def main():
    """
    The main function which starts the game engine.
    """
    app = Engine(initialize.caption)
    views = {"PROFILE"     : profile.Profile(),
             "MAINMENU"    : mainmenu.Menu(),
             "LEVELSELECT" : levelselect.LevelSelect(),
             "GAME"        : game.Game(),
             "POSTGAME"    : postgame.PostGame()}
    app.view_manager.initialize_views(views, "MAINMENU")
    app.main()