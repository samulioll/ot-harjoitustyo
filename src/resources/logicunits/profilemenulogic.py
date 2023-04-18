from resources.services import profile_manager

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

    def select_user(self, mouse_pos):
        """ Returns the clicked profile. """
        all_profiles = profile_manager.AllProfiles()
        if 620 <= mouse_pos[0] <= 950 and 455 <= mouse_pos[1] <= 1010:
            user = str((mouse_pos[1] - 350) // 100)
            if all_profiles.profiles[user] is not None:
                return all_profiles.profiles[user]
        return None

    def select_username(self, mouse_pos):
        """ Returns the username of selected profile. """
        all_profiles = profile_manager.AllProfiles()
        if 620 <= mouse_pos[0] <= 950 and 455 <= mouse_pos[1] <= 1010:
            user = str((mouse_pos[1] - 350) // 100)
            if all_profiles.profiles[user] is not None:
                return all_profiles.profiles[user][0]
        return None

    def delete_user(self,  mouse_pos):
        """ Deletes a profile. """
        all_profiles = profile_manager.AllProfiles()
        if 620 <= mouse_pos[0] <= 950 and 455 <= mouse_pos[1] <= 1010:
            user = str((mouse_pos[1] - 350) // 100)
            if all_profiles.profiles[user] is not None:
                all_profiles.delete_profile(user)
