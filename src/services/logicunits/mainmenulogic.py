class MainMenuLogic():
    """
    A class that contains the main menu logic.
    """
    def __init__(self):
        pass

    def get_clicked(self, mouse_pos):
        if 270 <= mouse_pos[0] <= 565 and 450 <= mouse_pos[1] <= 500:
            return ("GAME", True)
        if 380 <= mouse_pos[0] <= 565 and 600 <= mouse_pos[1] <= 650:
            return ("LEVELSELECT", True)
        if 180 <= mouse_pos[0] <= 565 and 755 <= mouse_pos[1] <= 805:
            print("")
            print("!! HIGHSCORES NOT YET FUNCTIONAL !!")
            print("")
            #return ("HIGHSCORES", True)
        if 200 <= mouse_pos[0] <= 565 and 905 <= mouse_pos[1] <= 955:
            return ("PROFILESELECT", True)
        return (None, False)
