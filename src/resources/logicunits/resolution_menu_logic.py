class ResolutionMenuLogic():
    """
    A class that contains the main menu logic.
    """

    def __init__(self):
        pass

    def get_clicked(self, mouse_pos, profile):
        if 50 <= mouse_pos[0] <= 240 and 180 <= mouse_pos[1] <= 260:
            scale = 1
            if profile:
                return ("MAINMENU", True, scale)
            return ("PROFILESELECT", True, scale)
        if 270 <= mouse_pos[0] <= 455 and 180 <= mouse_pos[1] <= 260:
            scale = 0.5
            if profile:
                return ("MAINMENU", True, scale)
            return ("PROFILESELECT", True, scale)
        return None
