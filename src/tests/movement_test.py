import unittest
from ui.gui import Screen

level_matrix = [[0,0,0,0,0,0],
                [0,0,0,0,0,0],
                [0,"Red",0,"Yellow",0,0],
                [0,0,0,0,0,0],
                [0,0,0,0,0,0],
                [0,0,0,"Blue",0,0]]

class TestMovement(unittest.TestCase):
    def setUp(self):
        pass