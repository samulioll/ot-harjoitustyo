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
        if self.input_box:
            username = self.input_box.input_handler(event)
            if username:
                self.profile = self.all_profiles.add_profile(username)
                self.input_box = None
                self.done = True

        elif event.type == pg.MOUSEBUTTONDOWN:
            mouse_pos = pg.mouse.get_pos()
            if self.clicked == "NEW":
                empty = None
                for slot, profile in self.all_profiles.profiles.items():
                    if not profile and not empty:
                        empty = int(slot)
                if empty:
                    self.selected_slot = empty
                    self.input_box = profile_manager.InputBox(
                        620, (353 + 100 * empty), 330, 50)

            if self.clicked == "SELECT":
                if 620 <= mouse_pos[0] <= 950 and 455 <= mouse_pos[1] <= 510:
                    if self.all_profiles.profiles["1"] is not None:
                        self.profile = self.all_profiles.profiles["1"]
                        self.done = True
                elif 620 <= mouse_pos[0] <= 950 and 555 <= mouse_pos[1] <= 610:
                    if self.all_profiles.profiles["2"]:
                        self.profile = self.all_profiles.profiles["2"]
                        self.done = True
                elif 620 <= mouse_pos[0] <= 950 and 655 <= mouse_pos[1] <= 710:
                    if self.all_profiles.profiles["3"]:
                        self.profile = self.all_profiles.profiles["3"]
                        self.done = True
                elif 620 <= mouse_pos[0] <= 950 and 755 <= mouse_pos[1] <= 810:
                    if self.all_profiles.profiles["4"]:
                        self.profile = self.all_profiles.profiles["4"]
                        self.done = True
                elif 620 <= mouse_pos[0] <= 950 and 855 <= mouse_pos[1] <= 910:
                    if self.all_profiles.profiles["5"]:
                        self.profile = self.all_profiles.profiles["5"]
                        self.done = True
                elif 620 <= mouse_pos[0] <= 950 and 955 <= mouse_pos[1] <= 1010:
                    if self.all_profiles.profiles["6"]:
                        self.profile = self.all_profiles.profiles["6"]
                        self.done = True

            elif self.clicked == "DELETE":
                if 620 <= mouse_pos[0] <= 950 and 455 <= mouse_pos[1] <= 510:
                    if self.all_profiles.profiles["1"] is not None:
                        self.all_profiles.delete_profile("1")
                elif 620 <= mouse_pos[0] <= 950 and 555 <= mouse_pos[1] <= 610:
                    if self.all_profiles.profiles["2"]:
                        self.all_profiles.delete_profile("2")
                elif 620 <= mouse_pos[0] <= 950 and 655 <= mouse_pos[1] <= 710:
                    if self.all_profiles.profiles["3"]:
                        self.all_profiles.delete_profile("3")
                elif 620 <= mouse_pos[0] <= 950 and 755 <= mouse_pos[1] <= 810:
                    if self.all_profiles.profiles["4"]:
                        self.all_profiles.delete_profile("4")
                elif 620 <= mouse_pos[0] <= 950 and 855 <= mouse_pos[1] <= 910:
                    if self.all_profiles.profiles["5"]:
                        self.all_profiles.delete_profile("5")
                elif 620 <= mouse_pos[0] <= 950 and 955 <= mouse_pos[1] <= 1010:
                    if self.all_profiles.profiles["6"]:
                        self.all_profiles.delete_profile("6")
            
            self.clicked = self.menu.sub_menu(mouse_pos)
            print(self.clicked)

    def draw(self, surface):
        """ Draws the menu on the surface given. """
        self.menu.menu_items.draw(surface)
        
        mouse_pos = pg.mouse.get_pos()
        show = False
        if 305 <= mouse_pos[0] <= 560 and 440 <= mouse_pos[1] <= 600:
            show = True
        elif 305 <= mouse_pos[0] <= 560 and 600 <= mouse_pos[1] <= 800:
            show = True
        elif 305 <= mouse_pos[0] <= 560 and 800 <= mouse_pos[1] <= 960:
            show = True
        if show or self.clicked:
            for user in self.menu.draw_users(self.all_profiles.profiles, self.clicked):
                surface.blit(user[0], user[1])

