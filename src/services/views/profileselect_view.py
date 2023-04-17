import pygame as pg
from services.components.objects.menuprofile import MenuProfile
from ..view_manager import View
from ..components import profile_manager


class ProfileSelect(View):
    """ The view for the profile selection state."""
    def __init__(self):
        View.__init__(self)
        self.menu = MenuProfile()
        self.next = "MAINMENU"
        self.clicked = None
        self.all_profiles = profile_manager.AllProfiles()
        self.input_box = None

    def input_handler(self, event):
        """ Handles profile selection, creation and deletion. """
        # print(pg.mouse.get_pos())
        if event.type == pg.MOUSEBUTTONDOWN:
            mouse_pos = pg.mouse.get_pos()
            self.input_box = None

            selected_profile = self.menu.select_user(mouse_pos)
            if self.clicked == "SELECT" and selected_profile:
                self.profile, self.done, self.clicked = selected_profile, True, None

            if self.clicked == "DELETE":
                self.menu.delete_user(mouse_pos)
                self.clicked = None

            clicked = self.menu.get_clicked(mouse_pos, self.clicked)
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
        self.menu.menu_items.draw(surface)

        mouse_pos = pg.mouse.get_pos()
        show = False
        if 305 <= mouse_pos[0] <= 560 and 440 <= mouse_pos[1] <= 960:
            show = True
        if show or self.clicked:
            for user in self.menu.draw_users(self.clicked):
                surface.blit(user[0], user[1])
        if self.input_box:
            self.input_box.draw(surface)
