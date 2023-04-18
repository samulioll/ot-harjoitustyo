from resources.services import profile_manager


class MenuHighscores():
    """
    A class for the high scores menu.
    """

    def __init__(self):
        self.all_profiles = profile_manager.AllProfiles()

    def handle_show_level(self, mouse_pos):
        if 215 <= mouse_pos[0] <= 395 and 740 <= mouse_pos[1] <= 790:
            return "MOVES"
        if 240 <= mouse_pos[0] <= 360 and 810 <= mouse_pos[1] <= 860:
            return "TIME"
        return None

    def get_selected_level(self, mouse_pos, profile):
        if 430 <= mouse_pos[0] <= 770 and 1050 <= mouse_pos[1] <= 1100:
            return ("MAINMENU", True, None)
        return ("MAINMENU", False, self.select_level(mouse_pos, profile))

    def select_level(self, mouse_pos, profile):
        """
        Returns the numerical value of the clicked level.
        """
        rows = {0: (360, 425),
                1: (493, 562),
                2: (632, 702),
                3: (772, 842),
                4: (914, 984)}
        cols = {1: (227, 295),
                2: (302, 370),
                3: (377, 446),
                4: (454, 520),
                5: (528, 596),
                6: (605, 672),
                7: (680, 748),
                8: (755, 824),
                9: (831, 898),
                10: (906, 975)}

        lvl_row, lvl_col = -1, -1
        for row, limits in rows.items():
            if limits[0] <= mouse_pos[1] <= limits[1]:
                lvl_row = row
        for col, limits in cols.items():
            if limits[0] <= mouse_pos[0] <= limits[1]:
                lvl_col = col
        if lvl_row >= 0 and lvl_col >= 0:
            level = (lvl_row * 10) + lvl_col
            if level <= len(profile.scores) + 1:
                return level
            return None
        return None
