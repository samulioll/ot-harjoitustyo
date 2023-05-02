class PostGameLogic():
    """ Handles the logic tasks of the post game menu. """

    def __init__(self):
        pass

    def get_next(self, mouse_pos: tuple, play_level: int):
        """ Returns the necessary information to switch game views 
            according to which button is pressed.

        Args:
            mouse_pos (tuple): Mouse coordinates.
            play_level (int): The level that was just solved.

        Returns:
            Information about the next view, next level to be played and
            if the current view is done.
        """
        if 450 <= mouse_pos[0] <= 580 and 650 <= mouse_pos[1] <= 690:
            next_view = "GAME"
            play_level += 1
            done = True
            return (next_view, play_level, done)
        if 620 <= mouse_pos[0] <= 725 and 650 <= mouse_pos[1] <= 690:
            next_view = "MAINMENU"
            play_level = None
            done = True
            return (next_view, play_level, done)
        next_view = None
        done = False
        return (next_view, play_level, done)
