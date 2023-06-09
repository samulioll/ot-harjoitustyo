import unittest
from resources.logicunits.game_logic import Board

basic_level = [["Magenta", "Magenta-1", 0, 0, 0, 0],
               [0, "Blue", "Blue-1", 0, 0, 0],
               [0, "Red", "Red-1", 0, 0, 0],
               ["Lime", 0, 0, 0, 0, "Black"],
               ["Lime-1", "Orange", "Orange-1", 0, 0, "Black-1"],
               ["Brown", "Brown-1", 0, 0, 0, 0]]

test_level = [[0, "White", "White-1", "White-2", 0, 0],
              [0, 0, 0, 0, 0, 0],
              [0, "Purple", 0, "Grey", "Green", "Yellow"],
              [0, "Purple-1", 0, "Grey-1", "Green-1", "Yellow-1"],
              [0, 0, 0, "Grey-2", "Green-2", "Yellow-2"],
              [0, 0, 0, 0, 0, 0]]


class TestCar(unittest.TestCase):
    def setUp(self):
        self.board = Board(basic_level)

    # Horizontal car movement tests

    def test_move_right(self):
        mouse_pos_x, mouse_pos_y = 450, 550
        offset = (50, 50)
        for i in range(2):
            mouse_pos_x += 50
            self.board.move_car("Red", (mouse_pos_x, mouse_pos_y), offset)
        for car in self.board.cars:
            if car.car_id == "Red":
                self.assertEqual(car.rect.x, 500)

    def test_move_left(self):
        mouse_pos_x, mouse_pos_y = 550, 550
        offset = (50, 50)
        for i in range(4):
            mouse_pos_x -= 50
            self.board.move_car("Red-1", (mouse_pos_x, mouse_pos_y), offset)
        for car in self.board.cars:
            if car.car_id == "Red":
                self.assertEqual(car.rect.x, 300)

    def test_cant_move_down(self):
        mouse_pos_x, mouse_pos_y = 450, 550
        offset = (50, 50)
        for i in range(2):
            mouse_pos_y += 50
            self.board.move_car("Red", (mouse_pos_x, mouse_pos_y), offset)
        for car in self.board.cars:
            if car.car_id == "Red":
                self.assertEqual(car.rect.x, 400)

    def test_cant_move_up(self):
        mouse_pos_x, mouse_pos_y = 450, 550
        offset = (50, 50)
        for i in range(2):
            mouse_pos_y -= 50
            self.board.move_car("Red", (mouse_pos_x, mouse_pos_y), offset)
        for car in self.board.cars:
            if car.car_id == "Red":
                self.assertEqual(car.rect.x, 400)

    def test_cant_move_right_more_than_one_cell(self):
        mouse_pos_x, mouse_pos_y = 450, 550
        offset = (50, 50)
        for i in range(2):
            mouse_pos_x += 100
            self.board.move_car("Red", (mouse_pos_x, mouse_pos_y), offset)
        for car in self.board.cars:
            if car.car_id == "Red":
                self.assertEqual(car.rect.x, 400)

    def test_move_left_more_than_one_cell(self):
        mouse_pos_x, mouse_pos_y = 450, 550
        offset = (50, 50)
        for i in range(2):
            mouse_pos_x -= 100
            self.board.move_car("Red", (mouse_pos_x, mouse_pos_y), offset)
        for car in self.board.cars:
            if car.car_id == "Red":
                self.assertEqual(car.rect.x, 400)

    def test_cant_get_outside_right(self):
        mouse_pos_x, mouse_pos_y = 450, 450
        offset = (50, 50)
        for i in range(8):
            mouse_pos_x += 50
            self.board.move_car("Blue", (mouse_pos_x, mouse_pos_y), offset)
        for car in self.board.cars:
            if car.car_id == "Blue":
                self.assertEqual(car.rect.x, 700)

    def test_cant_get_outside_left(self):
        mouse_pos_x, mouse_pos_y = 450, 550
        offset = (50, 50)
        for i in range(4):
            mouse_pos_x -= 50
            self.board.move_car("Blue", (mouse_pos_x, mouse_pos_y), offset)
        for car in self.board.cars:
            if car.car_id == "Blue":
                self.assertEqual(car.rect.x, 300)

    def test_collide_right(self):
        mouse_pos_x, mouse_pos_y = 450, 750
        offset = (50, 50)
        for i in range(6):
            mouse_pos_x += 50
            self.board.move_car("Orange", (mouse_pos_x, mouse_pos_y), offset)
        for car in self.board.cars:
            if car.car_id == "Orange":
                self.assertEqual(car.rect.x, 600)

    def test_collide_left(self):
        mouse_pos_x, mouse_pos_y = 450, 750
        offset = (50, 50)
        for i in range(2):
            mouse_pos_x -= 50
            self.board.move_car("Orange", (mouse_pos_x, mouse_pos_y), offset)
        for car in self.board.cars:
            if car.car_id == "Orange":
                self.assertEqual(car.rect.x, 400)

    # Vertical car movement tests

    def test_cant_move_right(self):
        mouse_pos_x, mouse_pos_y = 850, 650
        offset = (50, 50)
        for i in range(2):
            mouse_pos_x += 50
            self.board.move_car("Black", (mouse_pos_x, mouse_pos_y), offset)
        for car in self.board.cars:
            if car.car_id == "Black":
                self.assertEqual(car.rect.x, 800)

    def test_cant_move_left(self):
        mouse_pos_x, mouse_pos_y = 850, 750
        offset = (50, 50)
        for i in range(2):
            mouse_pos_x -= 50
            self.board.move_car("Black-1", (mouse_pos_x, mouse_pos_y), offset)
        for car in self.board.cars:
            if car.car_id == "Black":
                self.assertEqual(car.rect.x, 800)

    def test_move_down(self):
        mouse_pos_x, mouse_pos_y = 850, 650
        offset = (50, 50)
        for i in range(2):
            mouse_pos_y += 50
            self.board.move_car("Black", (mouse_pos_x, mouse_pos_y), offset)
        for car in self.board.cars:
            if car.car_id == "Black":
                self.assertEqual(car.rect.y, 700)

    def test_move_up(self):
        mouse_pos_x, mouse_pos_y = 850, 650
        offset = (50, 50)
        for i in range(2):
            mouse_pos_y -= 50
            self.board.move_car("Black", (mouse_pos_x, mouse_pos_y), offset)
        for car in self.board.cars:
            if car.car_id == "Black":
                self.assertEqual(car.rect.y, 500)

    def test_move_down_more_than_one_cell(self):
        mouse_pos_x, mouse_pos_y = 850, 650
        offset = (50, 50)
        for i in range(2):
            mouse_pos_y += 100
            self.board.move_car("Black", (mouse_pos_x, mouse_pos_y), offset)
        for car in self.board.cars:
            if car.car_id == "Black":
                self.assertEqual(car.rect.y, 600)

    def test_move_up_more_than_one_cell(self):
        mouse_pos_x, mouse_pos_y = 850, 650
        offset = (50, 50)
        for i in range(2):
            mouse_pos_y -= 100
            self.board.move_car("Black", (mouse_pos_x, mouse_pos_y), offset)
        for car in self.board.cars:
            if car.car_id == "Black":
                self.assertEqual(car.rect.y, 600)

    def test_collide_down(self):
        mouse_pos_x, mouse_pos_y = 450, 750
        offset = (50, 50)
        for i in range(2):
            mouse_pos_y += 50
            self.board.move_car("Lime", (mouse_pos_x, mouse_pos_y), offset)
        for car in self.board.cars:
            if car.car_id == "Lime":
                self.assertEqual(car.rect.y, 600)

    def test_collide_up(self):
        mouse_pos_x, mouse_pos_y = 350, 650
        offset = (50, 50)
        for i in range(6):
            mouse_pos_y -= 50
            self.board.move_car("Lime", (mouse_pos_x, mouse_pos_y), offset)
        for car in self.board.cars:
            if car.car_id == "Lime":
                self.assertEqual(car.rect.y, 400)

    # Car drop tests

    def test_drop_horizontal(self):
        test_board = Board(test_level)
        mouse_pos_x, mouse_pos_y = 650, 350
        offset = (50, 50)
        for i in range(2):
            mouse_pos_x += 50
            test_board.move_car("White-2", (mouse_pos_x, mouse_pos_y), offset)
            moved, done = test_board.drop_car("White-2")
        self.assertEqual(test_board.layout[0][2], "White")

    def test_drop_vertical(self):
        test_board = Board(test_level)
        mouse_pos_x, mouse_pos_y = 850, 750
        offset = (50, 50)
        for i in range(2):
            mouse_pos_y += 50
            test_board.move_car("Yellow-2", (mouse_pos_x, mouse_pos_y), offset)
            moved, done = test_board.drop_car("Yellow-2")
        self.assertEqual(test_board.layout[3][5], "Yellow")

    # Test selection

    def test_selected(self):
        mouse_pos = (450, 450)
        offset = (50, 50)
        self.assertEqual(self.board.get_selected(mouse_pos), "Blue")

    def test_none_selected(self):
        mouse_pos = (50, 550)
        offset = (50, 50)
        self.assertEqual(self.board.get_selected(mouse_pos), None)

    # Test red outside board

    def test_move_right(self):
        mouse_pos_x, mouse_pos_y = 450, 550
        offset = (50, 50)
        for i in range(10):
            mouse_pos_x += 50
            self.board.move_car("Red", (mouse_pos_x, mouse_pos_y), offset)
        moved, solved = self.board.drop_car("Red")
        self.assertEqual((moved, solved), (True, True))
