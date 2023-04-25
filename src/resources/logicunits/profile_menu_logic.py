class ProfileMenuLogic():
    """
    A class for the select profile menu.
    """

    def __init__(self):
        pass

    def get_clicked(self, mouse_pos, prev):
        if 305 <= mouse_pos[0] <= 560 and 440 <= mouse_pos[1] <= 560:
            return "SELECT"
        if 305 <= mouse_pos[0] <= 560 and 640 <= mouse_pos[1] <= 760:
            return "NEW"
        if 305 <= mouse_pos[0] <= 560 and 840 <= mouse_pos[1] <= 960:
            return "DELETE"
        if 620 <= mouse_pos[0] <= 950 and 455 <= mouse_pos[1] <= 1010:
            return prev
        return None

    def select_user(self, mouse_pos, all_profiles):
        """ Returns the clicked profile. """
        if 620 <= mouse_pos[0] <= 950 and 455 <= mouse_pos[1] <= 1010:
            user = str((mouse_pos[1] - 350) // 100)
            if all_profiles.profiles[user] is not None:
                return all_profiles.profiles[user]
        return None

    def confirm_delete(self, mouse_pos):
        """ Return the clicked option of the delete confirm """
        if 490 <= mouse_pos[0] <= 580 and 650 <= mouse_pos[1] <= 695:
            return "YES"
        if 620 <= mouse_pos[0] <= 710 and 650 <= mouse_pos[1] <= 695:
            return "NO"
        return None
