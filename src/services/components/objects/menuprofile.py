import pygame as pg
from .ui_element import UiElement
from ...components import profile_manager


class MenuProfile():
    """
    A class for the select profile menu.
    """

    def __init__(self):
        self.menu_items = pg.sprite.Group()
        self.menu_items.add(UiElement("full_select_profile_2", 0, 0))
        self.font = pg.font.SysFont("Arial", 50)

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

    def draw_users(self, active):
        """ Returns a list of pygame text objects of all profiles and empty slots. """
        all_profiles = profile_manager.AllProfiles()
        usernames = []
        y_coord = 450
        p_col = 0 if active in ("SELECT", "DELETE") else 150
        d_col = 200 if active == "DELETE" else p_col
        e_col = 150
        for profile in all_profiles.profiles.values():
            if profile is None:
                text = self.font.render("EMPTY SLOT", True,(e_col,e_col,e_col), None)
                text_rect = text.get_rect()
                text_rect.x = 625
                text_rect.y = y_coord
                usernames.append((text, text_rect))
            else:
                text = self.font.render(profile.username, True, (d_col,p_col,p_col), None)
                text_rect = text.get_rect()
                text_rect.x = 625
                text_rect.y = y_coord
                usernames.append((text, text_rect))
            y_coord += 100
        return usernames

    def select_user(self, mouse_pos):
        """ Returns the clicked profile. """
        all_profiles = profile_manager.AllProfiles()
        if 620 <= mouse_pos[0] <= 950 and 455 <= mouse_pos[1] <= 1010:
            user = str((mouse_pos[1] - 350) // 100)
            if all_profiles.profiles[user] is not None:
                return all_profiles.profiles[user]
        return None

    def delete_user(self,  mouse_pos):
        """ Deletes a profile. """
        all_profiles = profile_manager.AllProfiles()
        if 620 <= mouse_pos[0] <= 950 and 455 <= mouse_pos[1] <= 1010:
            user = str((mouse_pos[1] - 350) // 100)
            if all_profiles.profiles[user] is not None:
                all_profiles.delete_profile(user)
