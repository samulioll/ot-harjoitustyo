import unittest
from resources.logicunits.postgame_logic import PostGameLogic


class TestMainenuUI(unittest.TestCase):
    def setUp(self):
        self.logic = PostGameLogic()

    # Menu buttons activation tests

    def test_activate_next_level(self):
        self.assertEqual(self.logic.get_next((500, 675), 10), ("GAME", 11, True))

    def test_activate_back_to_menu(self):
        self.assertEqual(self.logic.get_next((700, 675), 10), ("MAINMENU", None, True))

    def test_dont_click_buttons(self):
        self.assertEqual(self.logic.get_next((300, 475), 10), (None, 10, False))