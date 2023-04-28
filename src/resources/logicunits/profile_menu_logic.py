class ProfileMenuLogic():
    """ Handles the logic tasks of the select profile menu. """

    def __init__(self):
        pass

    def get_clicked(self, mouse_pos: tuple, prev: str):
        """ Returns the information of the current menu state.

        Args:
            mouse_pos (tuple): Mouse coordinates.
            prev (str): Currently active state.

        Returns:
            The new menu state if a button is pressed or the previous state if
            the profile area is clicked to preserve menu visibility. Else
            clear the state.
        """
        if 305 <= mouse_pos[0] <= 560 and 440 <= mouse_pos[1] <= 560:
            return "SELECT"
        if 305 <= mouse_pos[0] <= 560 and 640 <= mouse_pos[1] <= 760:
            return "NEW"
        if 305 <= mouse_pos[0] <= 560 and 840 <= mouse_pos[1] <= 960:
            return "DELETE"
        if 620 <= mouse_pos[0] <= 950 and 455 <= mouse_pos[1] <= 1010:
            return prev
        return None

    def select_user(self, mouse_pos: tuple, all_profiles):
        """ Returns the clicked profile. 

        Args:
            mouse_pos (tuple): Mouse coordinates.
            all_profiles (AllProfiles): An AllProfiles class object with information
                                        about all the profile slots.

        Returns:
            Selected user if clicked slot has one.
        """
        if 620 <= mouse_pos[0] <= 950 and 455 <= mouse_pos[1] <= 1010:
            user = str(int((mouse_pos[1] - 350) // 100))
            if all_profiles.profiles[user] is not None:
                return all_profiles.profiles[user]
        return None

    def confirm_delete(self, mouse_pos: tuple):
        """ Return the clicked option of the delete confirm.

        Args:
            mouse_pos (tuple): Mouse coordinates.

        Returns:
            Clicked option.
        """
        if 490 <= mouse_pos[0] <= 580 and 650 <= mouse_pos[1] <= 695:
            return "YES"
        if 620 <= mouse_pos[0] <= 710 and 650 <= mouse_pos[1] <= 695:
            return "NO"
        return None
