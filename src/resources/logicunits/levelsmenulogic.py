class LevelsMenuLogic():
    """
    A class for the levels logic menu.
    """

    def __init__(self):
        pass

    def get_clicked_button(self, mouse_pos, profile):
        if 430 <= mouse_pos[0] <= 770 and 1050 <= mouse_pos[1] <= 1100:
            next_view = "MAINMENU"
            done = True
            level = None
            return (next_view, done, level)
        selected_level = self.select_level(mouse_pos, profile)
        if selected_level and selected_level <= 37:
            if selected_level > 37:
                print("Level not yet available")
                return ("MAINMENU", False, None)
            next_view = "GAME"
            done = True
            level = selected_level
            return (next_view, done, level)
        print("Unsolved level")
        return ("MAINMENU", False, None)

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