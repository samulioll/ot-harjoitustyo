import pygame as pg
from .. import view_manager
from ..components import menus
from ..components import profile

class ProfileSelect(view_manager._View):
    def __init__(self):
        view_manager._View.__init__(self)
        self.menu = menus.Menus()
        self.next = "MAINMENU"
        self.clicked = None
        self.all_profiles = profile.AllProfiles()

    def input_handler(self, event, profile):
        print(pg.mouse.get_pos())
        if event.type == pg.MOUSEBUTTONDOWN:
            mouse_pos = pg.mouse.get_pos()
            if 305 <= mouse_pos[0] <= 565 and 545 <= mouse_pos[1] <= 670:
                self.clicked = "SELECT"
            else:
                self.clicked = None

            if self.clicked == "SELECT":
                pass

    
    def draw(self, surface, profile):
        """
        Argument:
            surface: pygame surface
        """
        self.menu.select_profile.draw(surface)

        if self.clicked == "SELECT":
            for user in self.all_profiles.draw_users(0):
                surface.blit(user[0], user[1])
        else:
            for user in self.all_profiles.draw_users(150):
                surface.blit(user[0], user[1])