import unittest
from data.components.board import Board

basic_level = [[0,0,0,0, 0,0],
               [0,0,0,0, 0,0],
               [0,"Red","Red-1",0, 0,0],
               [0,0,0,0,0,"Black"],
               [0,0,0,0,0,"Black-1"],
               [0,0,0,0,0,0]]

class TestCar(unittest.TestCase):
    def setUp(self):
        # 300 pixels before game grid on both sides, grid cell size 100px
        self.board = Board(basic_level)
    

    # Horizontal car tests
    def test_move_right(self):
        mouse_pos_x, mouse_pos_y = 450, 550
        offset = (50, 50)
        for i in range(2):
            mouse_pos_x += 50
            self.board.move_car("Red", (mouse_pos_x, mouse_pos_y), offset)
        self.assertEqual(self.board.red2x1.rect.x, 500)

    def test_move_left(self):
        mouse_pos_x, mouse_pos_y = 450, 550
        offset = (50, 50)
        for i in range(2):
            mouse_pos_x -= 50
            self.board.move_car("Red", (mouse_pos_x, mouse_pos_y), offset) 
        self.assertEqual(self.board.red2x1.rect.x, 300)

    def test_cant_move_down(self):
        mouse_pos_x, mouse_pos_y = 450, 550
        offset = (50, 50)
        for i in range(2):
            mouse_pos_y += 50
            self.board.move_car("Red", (mouse_pos_x, mouse_pos_y), offset) 
        self.assertEqual(self.board.red2x1.rect.y, 500)

    def test_cant_move_up(self):
        mouse_pos_x, mouse_pos_y = 450, 550
        offset = (50, 50)
        for i in range(2):
            mouse_pos_y -= 50
            self.board.move_car("Red", (mouse_pos_x, mouse_pos_y), offset) 
        self.assertEqual(self.board.red2x1.rect.y, 500)

    def test_cant_move_right_more_than_one_cell(self):
        mouse_pos_x, mouse_pos_y = 450, 550
        offset = (50, 50)
        for i in range(2):
            mouse_pos_x += 100
            self.board.move_car("Red", (mouse_pos_x, mouse_pos_y), offset)
        self.assertEqual(self.board.red2x1.rect.x, 400)

    def test_move_left_more_than_one_cell(self):
        mouse_pos_x, mouse_pos_y = 450, 550
        offset = (50, 50)
        for i in range(2):
            mouse_pos_x -= 100
            self.board.move_car("Red", (mouse_pos_x, mouse_pos_y), offset) 
        self.assertEqual(self.board.red2x1.rect.x, 400)


    # Vertical car tests
    def test_cant_move_right(self):
        mouse_pos_x, mouse_pos_y = 850, 650
        offset = (50, 50)
        for i in range(2):
            mouse_pos_x += 50
            self.board.move_car("Black", (mouse_pos_x, mouse_pos_y), offset)
        self.assertEqual(self.board.black1x2.rect.x, 800)

    def test_cant_move_left(self):
        mouse_pos_x, mouse_pos_y = 850, 650
        offset = (50, 50)
        for i in range(2):
            mouse_pos_x -= 50
            self.board.move_car("Black", (mouse_pos_x, mouse_pos_y), offset)       
        self.assertEqual(self.board.black1x2.rect.x, 800)

    def test_move_down(self):
        mouse_pos_x, mouse_pos_y = 850, 650
        offset = (50, 50)
        for i in range(2):
            mouse_pos_y += 50
            self.board.move_car("Black", (mouse_pos_x, mouse_pos_y), offset)  
        self.assertEqual(self.board.black1x2.rect.y, 700)

    def test_move_up(self):
        mouse_pos_x, mouse_pos_y = 850, 650
        print(self.board.black1x2.rect.y)
        offset = (50, 50)
        for i in range(2):
            mouse_pos_y -= 50
            self.board.move_car("Black", (mouse_pos_x, mouse_pos_y), offset)
            print("move", i, self.board.black1x2.rect.y)
        self.assertEqual(self.board.black1x2.rect.y, 500)

    def test_move_down_more_than_one_cell(self):
        mouse_pos_x, mouse_pos_y = 850, 650
        offset = (50, 50)
        for i in range(2):
            mouse_pos_y += 100
            self.board.move_car("Black", (mouse_pos_x, mouse_pos_y), offset)  
        self.assertEqual(self.board.black1x2.rect.y, 600)

    def test_move_up_more_than_one_cell(self):
        mouse_pos_x, mouse_pos_y = 850, 650
        print(self.board.black1x2.rect.y)
        offset = (50, 50)
        for i in range(2):
            mouse_pos_y -= 100
            self.board.move_car("Black", (mouse_pos_x, mouse_pos_y), offset)
            print("move", i, self.board.black1x2.rect.y)
        self.assertEqual(self.board.black1x2.rect.y, 600)