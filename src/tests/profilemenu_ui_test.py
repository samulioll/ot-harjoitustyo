import unittest
from resources.logicunits.profile_menu_logic import ProfileMenuLogic


class TestMainenuUI(unittest.TestCase):
    def setUp(self):
        self.logic = ProfileMenuLogic()

    # Menu buttons activation tests

    def test_activate_select_profile(self):
        self.assertEqual(self.logic.get_clicked((400, 500), None), "SELECT")

    def test_activate_new_profile(self):
        self.assertEqual(self.logic.get_clicked((400, 700), None), "NEW")

    def test_activate_delete_profile(self):
        self.assertEqual(self.logic.get_clicked((400, 900), None), "DELETE")

    def test_keep_selected(self):
        self.assertEqual(self.logic.get_clicked((700, 900), "SELECT"), "SELECT")

    def test_reset_selected(self):
        self.assertEqual(self.logic.get_clicked((200, 100), "SELECT"), None)