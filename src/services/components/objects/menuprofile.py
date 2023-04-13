import pygame as pg
from .ui_element import UiElement


class MenuProfile():
    """
    A class for the select profile menu.
    """

    def __init__(self):
        self.menu_items = pg.sprite.Group()
        self.menu_items.add(UiElement("full_select_profile_2", 0, 0))
        self.font = pg.font.SysFont("Arial", 50)

    def sub_menu(self, mouse_pos):
        if 305 <= mouse_pos[0] <= 560 and 440 <= mouse_pos[1] <= 560:
            return "SELECT"
        if 305 <= mouse_pos[0] <= 560 and 640 <= mouse_pos[1] <= 760:
            return "NEW"
        if 305 <= mouse_pos[0] <= 560 and 840 <= mouse_pos[1] <= 960:
            return "DELETE"
        return None

    def draw_users(self, profiles, active):
        """ Returns a list of pygame text objects of all profiles and empty slots. """
        usernames = []
        y_coord = 450
        p_col = 0 if active in ("SELECT", "DELETE") else 150
        e_col = 0 if active == "NEW" else 150
        for profile in profiles.values():
            if profile is None:
                text = self.font.render("EMPTY SLOT", True,(e_col,e_col,e_col), None)
                text_rect = text.get_rect()
                text_rect.x = 625
                text_rect.y = y_coord
                usernames.append((text, text_rect))
            else:
                text = self.font.render(profile.username, True, (p_col,p_col,p_col), None)
                text_rect = text.get_rect()
                text_rect.x = 625
                text_rect.y = y_coord
                usernames.append((text, text_rect))
            y_coord += 100
        return usernames
