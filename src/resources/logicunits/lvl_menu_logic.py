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
        selected_level = tools.select_level(mouse_pos, profile)
        if selected_level:
            next_view = "GAME"
            done = True
            level = selected_level
            return (next_view, done, level)
        return ("MAINMENU", False, None)
