import unittest
from resources.logicunits.profile_menu_logic import ProfileMenuLogic
from resources.services import profile_manager


class TestProfileMenuUI(unittest.TestCase):
    def setUp(self):
        self.logic = ProfileMenuLogic()
        self.all_profiles = {}

    # First level menu buttons activation tests

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
    
    # Select profile menu buttons activation tests

    #def test_activate_first_slot(self):
    #    self.assertEqual(self.logic.select_user((650, 460), None), "DELETE")