from resources.services import profile_manager, tools


class HighscoresMenuLogic():
    """ Handles the logic tasks of the high scores menu. """

    def __init__(self):
        self.all_profiles = profile_manager.AllProfiles()

    def update_scores(self):
        """ Updates the self.all_profiles attribute. """

        self.all_profiles = profile_manager.AllProfiles()

    def handle_show_level(self, mouse_pos: tuple, selected_level: int):
        """ Clears the selected level if the back button is clicked.

        Args:
            mouse_pos (tuple): Mouse coordinates.
            selected_level (int): Currently selected level.

        Returns:
            Selected level if the back button is not pressed.
        """

        if 220 <= mouse_pos[0] <= 380 and 805 <= mouse_pos[1] <= 850:
            return None
        return selected_level

    def get_selected_level(self, mouse_pos: tuple, profile):
        """ returns the selected level or necessary information to switch 
            back to the main menu if the main menu button is clicked.

        Args:
            mouse_pos (tuple): Mouse coordinates.
            profile (Profile): Active profile.

        Returns:
            The selected level or information about the next view 
            if the current view is done.
        """

        if 430 <= mouse_pos[0] <= 770 and 1050 <= mouse_pos[1] <= 1100:
            return ("MAINMENU", True, None)
        return (None, False, self.select_level(mouse_pos, profile))

    def select_level(self, mouse_pos: tuple, profile):
        """ Gets the numerical value of the clicked level.

        Args:
            mouse_pos (tuple): Mouse coordinates.
            profile (Profile): Active profile.

        Returns:
            level: Value of the clicked level if one is clicked.
        """

        return tools.select_level(mouse_pos, profile)

    def level_scores(self, level: int):
        """ Return the highscores for the selected level.

        Args:
            level (int): Selected level

        Returns:
            A list of all users' scores for the selected level
            in ascending order.
        """

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
