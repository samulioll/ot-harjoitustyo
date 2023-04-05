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

    def input_handler(self, event):
        #print(pg.mouse.get_pos())
        if event.type == pg.MOUSEBUTTONDOWN:
            mouse_pos = pg.mouse.get_pos()
            if 305 <= mouse_pos[0] <= 565 and 545 <= mouse_pos[1] <= 670:
                self.clicked = "SELECT"
            else:
                pass

            if self.clicked == "SELECT":
                if 620 <= mouse_pos[0] <= 950 and 455 <= mouse_pos[1] <= 510:
                    try:
                        self.profile = self.all_profiles.profiles[0]
                        self.done = True
                    except:
                        pass
                elif 620 <= mouse_pos[0] <= 950 and 555 <= mouse_pos[1] <= 610:
                    selected_profile = self.all_profiles.profiles[1]
                elif 620 <= mouse_pos[0] <= 950 and 655 <= mouse_pos[1] <= 710:
                    selected_profile = self.all_profiles.profiles[2]
                elif 620 <= mouse_pos[0] <= 950 and 755 <= mouse_pos[1] <= 810:
                    selected_profile = self.all_profiles.profiles[3]
                elif 620 <= mouse_pos[0] <= 950 and 855 <= mouse_pos[1] <= 910:
                    selected_profile = self.all_profiles.profiles[4]
                elif 620 <= mouse_pos[0] <= 950 and 955 <= mouse_pos[1] <= 1010:
                    selected_profile = self.all_profiles.profiles[5]
    
    def draw(self, surface):
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