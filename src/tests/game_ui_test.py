import unittest
from resources.logicunits.game_logic import Board

test_level = [[0, "White", "White-1", "White-2", 0, 0],
              [0, 0, 0, 0, 0, 0],
              [0, "Purple", 0, "Grey", "Green", "Yellow"],
              [0, "Purple-1", 0, "Grey-1", "Green-1", "Yellow-1"],
              [0, 0, 0, "Grey-2", "Green-2", "Yellow-2"],
              [0, 0, 0, 0, 0, 0]]
level = 2


class TestGameUI(unittest.TestCase):
    def setUp(self):
        self.board = Board(test_level)

    def test_reset(self):
        mouse_pos = (500, 1075)
        self.assertEqual(self.board.get_clicked_button(
            mouse_pos, level), "RESET")

    def test_back_to_mainmenu(self):
        mouse_pos = (700, 1075)
        self.assertEqual(self.board.get_clicked_button(
            mouse_pos, level), ("MAINMENU", True, None))

    def test_didnt_click_button(self):
        mouse_pos = (400, 1075)
        self.assertEqual(self.board.get_clicked_button(
            mouse_pos, level), ("POSTGAME", False, level))
