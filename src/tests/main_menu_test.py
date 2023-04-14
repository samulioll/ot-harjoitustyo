import unittest
import pygame as pg
from services.components.objects.menumain import MenuMain

pg.init()

class TestMainMenu(unittest.TestCase):
    def setUp(self):
        self.menu = MenuMain()

    def test_activate_continue(self):
        self.assertEqual(self.menu.get_clicked((300, 475)), ("GAME", True))

    def test_activate_levels(self):
        self.assertEqual(self.menu.get_clicked((390, 625)), ("LEVELSELECT", True))

    #def test_activate_highscores(self):
    #    self.assertEqual(self.menu.get_clicked((300, 800)), ("HIGHSCORES", True))

    def test_activate_profile_menu(self):
        self.assertEqual(self.menu.get_clicked((300, 925)), ("PROFILESELECT", True))
    
    def test_click_outside_buttons(self):
        self.assertEqual(self.menu.get_clicked((200, 125)), (None, False))
