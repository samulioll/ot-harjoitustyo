import pygame as pg
from resources.logicunits.profile_menu_logic import ProfileMenuLogic
from resources.ui.sprites.ui_element import UiElement
from resources.services import profile_manager
from resources.services.view_manager import View


class ProfileSelect(View):
    """ The view for the profile selection state."""

    def __init__(self):
        View.__init__(self)
        self.logic = ProfileMenuLogic()
        self.next = "MAINMENU"
        self.clicked = None
        self.all_profiles = profile_manager.AllProfiles()
        self.input_box = None
        self.menu_items = pg.sprite.Group()
        self.confirm_box = pg.sprite.Group()
        self.font = pg.font.SysFont("Arial", 50)
        self.user_to_del = None

        self.menu_items.add(UiElement("full_select_profile_2", 0, 0))
        self.confirm_box.add(UiElement("delete_user_box_1", 0, 0))

    def input_handler(self, event):
        """ Handles profile selection, creation and deletion. """
        #print(pg.mouse.get_pos())
        if event.type == pg.MOUSEBUTTONDOWN:
            mouse_pos = pg.mouse.get_pos()
            self.input_box = None
            selected_profile = self.logic.select_user(mouse_pos, self.all_profiles)

            if self.user_to_del:
                if self.logic.confirm_delete(mouse_pos) == "YES":
                    self.all_profiles.delete_profile(self.user_to_del.slot)
                    self.user_to_del = None
                elif self.logic.confirm_delete(mouse_pos) == "NO":
                    self.user_to_del = None
                return

            if self.clicked == "SELECT" and selected_profile:
                self.profile, self.done, self.clicked = selected_profile, True, None

            if self.clicked == "DELETE":
                self.confirm_delete = True
                self.user_to_del = self.logic.select_user(mouse_pos, self.all_profiles)
                self.clicked = None

            clicked = self.logic.get_clicked(mouse_pos, self.clicked)
            self.clicked = clicked

            if self.clicked == "NEW":
                self.handle_clicked_new()

        elif self.input_box:
            username = self.input_box.input_handler(event)
            if username:
                new_profile = self.all_profiles.add_profile(username)
                if new_profile:
                    self.profile, self.input_box, self.done = new_profile, None, True

    def handle_clicked_new(self):
        """ Handles creation of input box for username if clicked new. """
        self.all_profiles = profile_manager.AllProfiles()
        empty_slot = None
        for slot, profile in self.all_profiles.profiles.items():
            if not profile and not empty_slot:
                empty_slot = int(slot)
        if empty_slot:
            self.input_box = profile_manager.InputBox(
                620, (338 + 100 * empty_slot), 330, 80)

    def draw(self, surface):
        """ Draws the menu on the surface given. """
        self.menu_items.draw(surface)

        mouse_pos = pg.mouse.get_pos()
        show = False

        if self.user_to_del:
            for user in self.draw_users():
                surface.blit(user[0], user[1])
            self.draw_delete_confirm(surface)
            return

        if 305 <= mouse_pos[0] <= 560 and 440 <= mouse_pos[1] <= 960:
            show = True
        if show or self.clicked:
            for user in self.draw_users():
                surface.blit(user[0], user[1])
        if self.input_box:
            self.input_box.draw(surface)

    def draw_users(self):
        """ Returns a list of pygame text objects of all profiles and empty slots. """
        all_profiles = profile_manager.AllProfiles()
        usernames = []
        y_coord = 450
        p_col = 0 if self.clicked in ("SELECT", "DELETE") else 150
        d_col = 200 if self.clicked == "DELETE" else p_col
        e_col = 150
        for profile in all_profiles.profiles.values():
            if profile is None:
                text = self.font.render(
                    "EMPTY SLOT", True, (e_col, e_col, e_col), None)
                text_rect = text.get_rect()
                text_rect.x = 625
                text_rect.y = y_coord
                usernames.append((text, text_rect))
            else:
                text = self.font.render(
                    profile.username, True, (d_col, p_col, p_col), None)
                text_rect = text.get_rect()
                text_rect.x = 625
                text_rect.y = y_coord
                usernames.append((text, text_rect))
            y_coord += 100
        return usernames

    def draw_delete_confirm(self, surface):
        self.confirm_box.draw(surface)
        text_user = self.font.render(
            self.user_to_del.username, True, (0, 0, 0), None)
        text_width = text_user.get_width()
        surface.blit(text_user, ((600 - text_width/2), 530))
