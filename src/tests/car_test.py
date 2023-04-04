import unittest
from data.components.board import Board

basic_level = [[0,0,0,0, 0,0],
               [0,0,0,0, 0,0],
               [0,"Red","Red-1",0, 0,0],
               [0,0,0,0,0,0],
               [0,0,0,0,0,0],
               [0,0,0,0,0,0]]

class TestCar(unittest.TestCase):
    def setUp(self):
        # 300 pixels before game grid on both sides, grid cell size 100px
        self.board = Board(basic_level)

    def test_move_right(self):
        mouse_pos_x, mouse_pos_y = 450, 550
        offset = (50, 50)
        for i in range(2):
            mouse_pos_x += 50
            self.board.move_car("Red", (mouse_pos_x, mouse_pos_y), offset)
        
        self.assertEqual(self.board.red2x1.rect.x, 500)
