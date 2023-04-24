from resources.services import profile_manager
from resources.logicunits.lvl_menu_logic import LevelsMenuLogic


class HighscoresMenuLogic():
    """
    A class for the high scores menu.
    """

    def __init__(self):
        self.all_profiles = profile_manager.AllProfiles()

    def update_scores(self):
        self.all_profiles = profile_manager.AllProfiles()

    def handle_show_level(self, mouse_pos, selected_level):
        if 220 <= mouse_pos[0] <= 380 and 805 <= mouse_pos[1] <= 850:
            return None
        return selected_level

    def get_selected_level(self, mouse_pos, profile):
        if 430 <= mouse_pos[0] <= 770 and 1050 <= mouse_pos[1] <= 1100:
            return ("MAINMENU", True, None)
        return ("MAINMENU", False, self.select_level(mouse_pos, profile))

    def select_level(self, mouse_pos, profile):
        """
        Returns the numerical value of the clicked level.
        """
        return LevelsMenuLogic().select_level(mouse_pos, profile)

    def level_scores(self, level):
        self.update_scores()
        scores = []
        for user in self.all_profiles.profiles.values():
            if user:
                try:
                    score = user.scores[str(level)]
                    scores.append((user.username, score))
                except KeyError:
                    pass
        scores.sort(key=lambda a: a[1])
        return scores
