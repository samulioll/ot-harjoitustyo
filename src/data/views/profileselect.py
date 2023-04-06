import pygame as pg
from .. import view_manager
from ..components import menus
from ..components import profile_manager

class ProfileSelect(view_manager._View):
    """ The view for the profile selection state."""
    def __init__(self):
        view_manager._View.__init__(self)
        self.menu = menus.Menus()
        self.next = "MAINMENU"
        self.clicked = None
        self.all_profiles = profile_manager.AllProfiles()

    def input_handler(self, event):
        """ Handles events and sets active profile. """
        #print(pg.mouse.get_pos())
        if event.type == pg.MOUSEBUTTONDOWN:
            mouse_pos = pg.mouse.get_pos()
            if 305 <= mouse_pos[0] <= 560 and 440 <= mouse_pos[1] <= 560:
                self.clicked = "SELECT"
            elif 305 <= mouse_pos[0] <= 560 and 640 <= mouse_pos[1] <= 760:
                self.clicked = "NEW"
            elif 305 <= mouse_pos[0] <= 560 and 840 <= mouse_pos[1] <= 960:
                self.clicked = "DELETE"

            if self.clicked == "SELECT":
                if 620 <= mouse_pos[0] <= 950 and 455 <= mouse_pos[1] <= 510:
                    if self.all_profiles.profiles[1] != None:
                        self.profile = self.all_profiles.profiles[1]
                        self.done = True
                elif 620 <= mouse_pos[0] <= 950 and 555 <= mouse_pos[1] <= 610:
                    if self.all_profiles.profiles[2]:
                        self.profile = self.all_profiles.profiles[2]
                        self.done = True
                elif 620 <= mouse_pos[0] <= 950 and 655 <= mouse_pos[1] <= 710:
                    if self.all_profiles.profiles[3]:
                        self.profile = self.all_profiles.profiles[3]
                        self.done = True
                elif 620 <= mouse_pos[0] <= 950 and 755 <= mouse_pos[1] <= 810:
                    if self.all_profiles.profiles[4]:
                        self.profile = self.all_profiles.profiles[4]
                        self.done = True
                elif 620 <= mouse_pos[0] <= 950 and 855 <= mouse_pos[1] <= 910:
                    if self.all_profiles.profiles[5]:
                        self.profile = self.all_profiles.profiles[5]
                        self.done = True
                elif 620 <= mouse_pos[0] <= 950 and 955 <= mouse_pos[1] <= 1010:
                    if self.all_profiles.profiles[6]:
                        self.profile = self.all_profiles.profiles[6]
                        self.done = True

    
    def draw(self, surface):
        """ Draws the menu on the surface given. """
        self.menu.select_profile.draw(surface)

        if self.clicked == "SELECT":
            for user in self.all_profiles.draw_users(0, 150):
                surface.blit(user[0], user[1])
        elif self.clicked == "NEW":
            for user in self.all_profiles.draw_users(150, 0):
                surface.blit(user[0], user[1])
        elif self.clicked == "DELETE":
            for user in self.all_profiles.draw_users(0, 150):
                surface.blit(user[0], user[1])
        else:
            for user in self.all_profiles.draw_users(150, 150):
                surface.blit(user[0], user[1])