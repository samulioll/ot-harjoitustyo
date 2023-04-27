from resources.services.engine import Engine
from resources.services import initialize
# , resolution_view
from resources.ui.views import game_view, highscores_view, levelselect_view
from resources.ui.views import mainmenu_view, postgame_view, profileselect_view


def main():
    """ The main function which starts the game engine and the view manager. """

    app = Engine(initialize.CAPTION)
    views = {"PROFILESELECT": profileselect_view.ProfileSelect(),
             "MAINMENU": mainmenu_view.MainMenu(),
             "LEVELSELECT": levelselect_view.LevelSelect(),
             "GAME": game_view.Game(),
             "POSTGAME": postgame_view.PostGame(),
             "HIGHSCORES": highscores_view.HighScores()
             # "RESOLUTION": resolution_view.Resolution()
             }
    app.view_manager.initialize_views(views, "PROFILESELECT")
    app.main()
