import unittest
from resources.logicunits.mainmenu_logic import MainMenuLogic


class TestMainenuUI(unittest.TestCase):
    def setUp(self):
        self.logic = MainMenuLogic()

    # Menu buttons activation tests

    def test_activate_continue(self):
        self.assertEqual(self.logic.get_clicked((300, 475)), ("GAME", True))

    def test_activate_levels(self):
        self.assertEqual(self.logic.get_clicked(
            (390, 625)), ("LEVELSELECT", True))

    def test_activate_highscores(self):
        self.assertEqual(self.logic.get_clicked(
            (300, 800)), ("HIGHSCORES", True))

    def test_activate_profile_menu(self):
        self.assertEqual(self.logic.get_clicked(
            (300, 925)), ("PROFILESELECT", True))

    def test_click_outside_buttons(self):
        self.assertEqual(self.logic.get_clicked((200, 125)), (None, False))
