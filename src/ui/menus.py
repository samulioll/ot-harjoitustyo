import pygame
from ui.sprites.menu_items import Menu_item

class Menus():
    def __init__(self):
        self.profiles = pygame.sprite.Group()
        self.main_menu_items = pygame.sprite.Group()
        self.profile_menu_items = pygame.sprite.Group()
        self.profiles = pygame.sprite.Group()

        self.initialize_main_menu()
        self.initialize_profile_selector()


    def initialize_profile_selector(self):
        #self.backdrop = Menu_item("backdrop_1", 0, 0)
        #self.title = Menu_item("Menu_title_1", 340, 100)
        self.full_profile_slector = Menu_item("full_select_profile_1", 0, 0)


        self.profile_menu_items.add(self.full_profile_slector)      



    def initialize_main_menu(self):
        #self.backdrop = Menu_item("backdrop_1", 0, 0)
        #self.title = Menu_item("Menu_title_1", 340, 100)
        self.full_main_menu = Menu_item("full_main_menu_1", 0, 0)

        self.main_menu_items.add( self.full_main_menu)

