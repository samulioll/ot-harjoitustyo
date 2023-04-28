def select_level(mouse_pos: tuple, profile=None):
    """ Gets the numerical value of the clicked level.

    Args:
        mouse_pos (tuple): Mouse coordinates.
        profile (Profile): Active profile.

    Returns:
        level: Value of the clicked level if one is clicked.
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
        if profile:
            if level <= len(profile.scores) + 1:
                return level
            return None
        return level
    return None


def scale_mouse_pos(coords: tuple, scale: float):
    """ Scales the mouse_coordinates for hte current game scale

    Args:
        coords (tuple): Actual mouse coordinates
        scale (float): Current game scale

    Returns:
        A tuple with scaled coordinates
    """
    return (coords[0] / scale, coords[1] / scale)
