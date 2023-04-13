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
        """ Handles events and sets active profile. """
        # print(pg.mouse.get_pos())
        if event.type == pg.MOUSEBUTTONDOWN:
            mouse_pos = pg.mouse.get_pos()
            self.input_box = None

            if self.clicked == "SELECT":
                if self.menu.select_user(mouse_pos):
                    self.profile = self.menu.select_user(mouse_pos)
                    self.done = True
                    self.clicked = None

            elif self.clicked == "DELETE":
                self.menu.delete_user(mouse_pos)
                self.clicked = None

            clicked = self.menu.get_clicked(mouse_pos)
            if clicked == "CLEAR":
                self.clicked = None
            elif clicked != "KEEP":
                self.clicked = clicked

            if self.clicked == "NEW":
                self.all_profiles = profile_manager.AllProfiles()
                empty = None
                for slot, profile in self.all_profiles.profiles.items():
                    if not profile and not empty:
                        empty = int(slot)
                        print(empty)
                if empty:
                    self.selected_slot = empty
                    self.input_box = profile_manager.InputBox(
                        620, (353 + 100 * empty), 330, 50)

        elif self.input_box:
            username = self.input_box.input_handler(event)
            if username:
                self.profile = self.all_profiles.add_profile(username)
                self.input_box = None
                self.done = True

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
