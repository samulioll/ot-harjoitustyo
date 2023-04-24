import unittest
from resources.logicunits.lvl_menu_logic import LevelsMenuLogic
from resources.services.profile_manager import Profile

class TestMainenuUI(unittest.TestCase):
    def setUp(self):
        self.logic = LevelsMenuLogic()
        self.profile = Profile("1", "Test", {"1": 4, "2": 5})

    def test_back_to_mainmenu(self):
        mouse_pos = (450, 1075)
        self.assertEqual(
            self.logic.get_clicked_button(mouse_pos, self.profile), ("MAINMENU", True, None)
            )

    def test_can_select_solved_level(self):
        mouse_pos= (350, 400)
        self.assertEqual(
            self.logic.get_clicked_button(mouse_pos, self.profile), ("GAME", True, 2)
            )

    def test_cant_select_unsolved_level(self):
        mouse_pos= (350, 530)
        self.assertEqual(
            self.logic.get_clicked_button(mouse_pos, self.profile), ("MAINMENU", False, None)
            )

    def test_returns_correct_level_if_already_solved(self):
        mouse_pos= (350, 400)
        self.assertEqual(
            self.logic.select_level(mouse_pos, self.profile), 2
            )

    def test_doesnt_return_level_if_not_solved(self):
        mouse_pos= (350, 530)
        self.assertEqual(
            self.logic.select_level(mouse_pos, self.profile), None
            )

    def test_doesnt_return_level_if_clicked_elsewhere(self):
        mouse_pos= (160, 400)
        self.assertEqual(
            self.logic.select_level(mouse_pos, self.profile), None
            )