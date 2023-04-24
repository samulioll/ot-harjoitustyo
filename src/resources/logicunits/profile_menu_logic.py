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

    def get_user_for_del(self, mouse_pos):
        """ Gets the user slot and username of the clicked profile"""
        all_profiles = profile_manager.AllProfiles()
        if 620 <= mouse_pos[0] <= 950 and 455 <= mouse_pos[1] <= 1010:
            user = str((mouse_pos[1] - 350) // 100)
            if all_profiles.profiles[user] is not None:
                return(user, all_profiles.profiles[user].username)
        return None

    def delete_user(self,  user):
        """ Deletes a profile. """
        all_profiles = profile_manager.AllProfiles()
        all_profiles.delete_profile(user)

    def confirm_delete(self,mouse_pos):
        """ Return the clicked option of the delete confirm """
        if 490 <= mouse_pos[0] <= 580 and 650 <= mouse_pos[1] <= 695:
            return "YES"
        if 620 <= mouse_pos[0] <= 670 and 650 <= mouse_pos[1] <= 695:
            return "NO"
