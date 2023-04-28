import unittest
from resources.logicunits.scores_menu_logic import HighscoresMenuLogic
from resources.services import profile_manager


class TestHighscoresMenuUI(unittest.TestCase):
    def setUp(self):
        self.logic = HighscoresMenuLogic()
        self.profile1 = profile_manager.Profile(
            1, "TestUser", {"1": 4, "2": 6})
        self.profile2 = profile_manager.Profile(
            2, "TestUser2", {"1": 5, "2": 4})
        self.all_profiles = profile_manager.AllProfiles()
        self.all_profiles.profiles = {"1": self.profile1, "2": self.profile2}

    # First level input tests

    def test_returns_correct_level_int(self):
        self.assertEqual(self.logic.select_level((260, 390)), 1)

    def test_doesnt_return_level_int_if_not_clicked(self):
        self.assertEqual(self.logic.select_level(
            (100, 390)), None)

    def test_returns_to_main_menu(self):
        self.assertEqual(self.logic.get_selected_level(
            (440, 1075)), ("MAINMENU", True, None))

    def test_returns_correct_level_info(self):
        self.assertEqual(self.logic.get_selected_level(
            (260, 390)), (None, False, 1))

    def test_returns_to_level_select(self):
        self.assertEqual(self.logic.handle_show_level((260, 840), 2), None)

    def test_doesnt_return_to_level_select(self):
        self.assertEqual(self.logic.handle_show_level((200, 100), 2), 2)
