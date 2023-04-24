class PostGameLogic():
    """
    A class for the post game menu.
    """

    def __init__(self):
        pass

    def get_next(self, mouse_pos, play_level):
        if 450 <= mouse_pos[0] <= 580 and 650 <= mouse_pos[1] <= 690:
            if play_level < 37:
                next_view = "GAME"
                play_level += 1
                done = True
                return (next_view, play_level, done)
            print("!! All levels solved !!")
            return (None, play_level, False)
        if 620 <= mouse_pos[0] <= 725 and 650 <= mouse_pos[1] <= 690:
            next_view = "MAINMENU"
            play_level = None
            done = True
            return (next_view, play_level, done)
        next_view = None
        done = False
        return (next_view, play_level, done)
