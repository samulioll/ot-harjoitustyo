from resources.services import tools


class LevelsMenuLogic():
    """ Handles the logic tasks of the level select menu. """

    def __init__(self):
        pass

    def get_clicked_button(self, mouse_pos: tuple, profile):
        """ Returns the necessary information to switch game views 
            according to which button is pressed or level information
            if a level is clicked.

        Args:
            mouse_pos (tuple): Mouse coordinates.
            profile (Profile): Active profile.

        Returns:
            Information about the next view, if the current view is done
            and the selected level.
        """
        if 430 <= mouse_pos[0] <= 770 and 1050 <= mouse_pos[1] <= 1100:
            next_view = "MAINMENU"
            done = True
            level = None
            return (next_view, done, level)
        selected_level = self.select_level(mouse_pos, profile)
        if selected_level and selected_level <= 40:
            if selected_level > 40:
                print("Level not yet available")
                return ("MAINMENU", False, None)
            next_view = "GAME"
            done = True
            level = selected_level
            return (next_view, done, level)
        print("Unsolved level")
        return ("MAINMENU", False, None)

    def select_level(self, mouse_pos: tuple, profile):
        """ Gets the numerical value of the clicked level.

        Args:
            mouse_pos (tuple): Mouse coordinates.
            profile (Profile): Active profile.

        Returns:
            level: Value of the clicked level if one is clicked.
        """

        return tools.select_level(mouse_pos, profile)
