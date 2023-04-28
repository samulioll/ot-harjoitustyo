from copy import deepcopy
import pygame as pg
from resources.ui.sprites.car import Car
from resources.ui.sprites.ui_element import UiElement


class Board:
    """ Simulates the board and handles the logic tasks of the game.

        Attributes:
            level: Selected level to be played.
    """

    def __init__(self, level):
        self.cell_size = 100
        self.board_offset = 300
        self.layout = deepcopy(level)
        self.car_ids = {"Red": "red2x1",
                        "Blue": "blue2x1",
                        "Orange": "orange2x1",
                        "Magenta": "magenta2x1",
                        "Brown": "brown2x1",
                        "White": "white3x1",
                        "Purple": "purple1x2",
                        "Black": "black1x2",
                        "Lime": "lime1x2",
                        "Grey": "grey1x3",
                        "Green": "green1x3",
                        "Yellow": "yellow1x3",
                        "Sky": "sky1x3",
                        "Tropic": "tropic3x1",
                        "Beige": "beige2x1",
                        "Ocean": "ocean1x2"}
        self.background = pg.sprite.Group()
        self.cars = pg.sprite.Group()
        self._initialize_sprites()

    def _initialize_sprites(self):
        """ Create the collection of sprites and their locations at the start. """

        self.full_game_view = UiElement("full_game_view_2", 0, 0)
        self.background.add(self.full_game_view)
        for row in range(6):
            for column in range(6):
                cell = self.layout[row][column]
                x_coord = column * self.cell_size + self.board_offset
                y_coord = row * self.cell_size + self.board_offset
                if cell != 0 and "-" not in cell:
                    car = Car(self.car_ids[cell], x_coord, y_coord)
                    self.cars.add(car)

    def get_clicked_button(self, mouse_pos, level):
        """ Returns the necessary information to switch game views 
            according to which button is pressed.

        Args:
            mouse_pos (tuple): Mouse coordinates.
            level (int): Current level.

        Returns:
            Tuple with information about next view, if the current view 
            is done and the current level.
        """
        if 430 <= mouse_pos[0] <= 565 and 1050 <= mouse_pos[1] <= 1100:
            return "RESET"
        if 615 <= mouse_pos[0] <= 720 and 1050 <= mouse_pos[1] <= 1100:
            next_view = "MAINMENU"
            done = True
            play_level = None
            return (next_view, done, play_level)
        next_view = "POSTGAME"
        done = False
        play_level = level
        return (next_view, done, play_level)

    def move_car(self, selected: str, mouse_pos: tuple, board_offset: int):
        """Handles the movement of cars.

        Args:
            selected (str): Name of the selected car.
            mouse_pos (tuple): Mouse coordinates.
            board_offset (int): Distance from original mouse position when the 
                                car was first clicked to the cell corner.
        """
        car_id = self.get_car_id(selected)
        others, sel = self.create_collision_group(car_id)
        if sel.move_axis == "x":
            self.handle_x_axis_move(
                selected, sel, mouse_pos, board_offset, others)
        else:
            self.handle_y_axis_move(
                selected, sel, mouse_pos, board_offset, others)

    def get_car_id(self, selected: str):
        """ Return the id of the clicked car.

        Args:
            selected (str): Name of the selected car cell.

        Returns:
            _type_: _description_
        """
        if "-" in selected:
            parts = selected.split("-")
            return parts[0]
        return selected

    def create_collision_group(self, car_id: str):
        """ Creates a collision group and returns selected car.

        Args:
            car_id (str): Name of the selected car.

        Returns:
            Tuple with sprite group of other cars and the selected Car object.
        """
        others = pg.sprite.Group()
        for car in self.cars:
            if car.car_id != car_id:
                others.add(car)
            else:
                sel = car
        return others, sel

    def handle_x_axis_move(self, selected: str, sel: Car,
                           mouse_pos: tuple, board_offset: int, others):
        """ Handles movement for x-axis cars.

        Args:
            selected (str): Name of the selected car cell.
            sel (Car): Selected car.
            mouse_pos (tuple): Mouse coordinates.
            board_offset (int): Distance from original mouse position when the
                                car was first clicked to the cell corner.
            others: Sprite group of every other car.
        """
        red_bonus = 200 if "Red" in sel.car_id else 0
        if "1" in selected:
            diff = board_offset[0] + 100
        elif "2" in selected:
            diff = board_offset[0] + 200
        else:
            diff = board_offset[0]
        new_pos = mouse_pos[0] - diff
        old_pos = sel.rect.x
        if 300 <= new_pos <= (900 - sel.width + red_bonus):
            if new_pos >= old_pos + 99 or new_pos <= old_pos - 99:
                return
            sel.rect.x = new_pos
            colliding = pg.sprite.spritecollide(sel, others, False)
            if colliding:
                sel.rect.x = old_pos

    def handle_y_axis_move(self, selected: str, sel: Car,
                           mouse_pos: tuple, board_offset: int, others):
        """ Handles movement for y-axis cars.

        Args:
            selected (str): Name of the selected car cell.
            sel (Car): Selected car.
            mouse_pos (tuple): Mouse coordinates.
            board_offset (int): Distance from original mouse position when the
                                car was first clicked to the cell corner.
            others: Sprite group of every other car.
        """
        if "1" in selected:
            diff = board_offset[1] + 100
        elif "2" in selected:
            diff = board_offset[1] + 200
        else:
            diff = board_offset[1]
        new_pos = mouse_pos[1] - diff
        old_pos = sel.rect.y
        if 300 <= new_pos <= (900 - sel.height):
            if new_pos >= old_pos + 99 or new_pos <= old_pos - 99:
                return
            sel.rect.y = new_pos
            colliding = pg.sprite.spritecollide(sel, others, False)
            if colliding:
                sel.rect.y = old_pos

    def drop_car(self, selected: str):
        """ Handles the dropping of a car that is being dragged.

        Args:
            selected (str): Name of the selected car cell.

        Returns:
            Tuple with move count and solved status.
        """
        car_id = self.get_car_id(selected)
        sel = self.create_collision_group(car_id)[1]
        cells = self.get_new_car_position(sel)
        old_pos = None
        for row in range(6):
            for column in range(6):
                position = self.clear_cell(row, column, car_id, sel, cells)
                if position:
                    old_pos = position
        if self.add_car_position(cells, sel):
            return (1, True)
        return (self.check_for_move(car_id, old_pos), False)

    def clear_cell(self, row: int, column: int, car_id: str, sel: Car, cells: int):
        """ Clears the old cells of the selected car.

        Args:
            row (int): Row of the first cell of the car.
            column (int): Column of the first cell of the car.
            car_id (str): Name of car.
            sel (Car): Selected car.
            cells (int): Number of cells in the car.

        Returns:
            old_pos: Tuple of old position of the first cell.
        """
        cell = self.layout[row][column]
        old_pos = None
        if cell == car_id:
            print("Cell", cell, "Car_id", car_id)
            old_pos = (row, column)
            cell = 0
            if sel.move_axis == "x":
                for i in range(cells):
                    self.layout[row][column+i] = 0
            else:
                for i in range(cells):
                    self.layout[row+i][column] = 0
        return old_pos

    def get_new_car_position(self, sel: Car):
        """ Calculates the correct cell for the car and changes its
            coordinates to match it.

        Args:
            sel (Car): Selected car.

        Returns:
            cells: Number of cells in the car.
        """
        if sel.move_axis == "x":
            cells = sel.width // 100
            old_pos = sel.rect.x
            diff = old_pos % 100
            if diff < 50:
                sel.rect.x = old_pos - diff
            else:
                sel.rect.x = old_pos + (100 - diff)
        else:
            cells = sel.height // 100
            old_pos = sel.rect.y
            diff = old_pos % 100
            if diff < 50:
                sel.rect.y = old_pos - diff
            else:
                sel.rect.y = old_pos + (100 - diff)
        return cells

    def add_car_position(self, cells: int, sel: Car):
        """ Adds car info to level matrix.

        Args:
            cells (int): Number of cells in the car.
            sel (Car): Selected car.

        Returns:
            True if level is solved else False.
        """
        x_cell = sel.rect.x // 100 - 3
        y_cell = sel.rect.y // 100 - 3
        if sel.move_axis == "x":
            try:
                for i in range(cells):
                    bonus = "-" + str(i) if i > 0 else ""
                    self.layout[y_cell][x_cell+i] = sel.car_id + bonus
            except IndexError:
                print("SOLVED")
                return True
        else:
            for i in range(cells):
                bonus = "-" + str(i) if i > 0 else ""
                self.layout[y_cell+i][x_cell] = sel.car_id + bonus
        return False

    def check_for_move(self, car_id: str, old_pos: tuple):
        """ Checks if the selected car is in a different location.

        Args:
            car_id (str): Name of car.
            old_pos (tuple): Tuple of old matrix location of the first cell.

        Returns:
            changed (int): 1 if move happened else 0.
        """
        changed = 0
        new_pos = None
        for row in range(6):
            for column in range(6):
                cell = self.layout[row][column]
                if cell == car_id:
                    new_pos = (row, column)
        if new_pos != old_pos:
            changed = 1
        return changed

    def get_selected(self, mouse_pos: tuple):
        """ Returns the selected car matrix cell name.

        Args:
            mouse_pos (tuple): Mouse coordinates.

        Returns:
            Car cell name in the clicked level layout matrix cell if possible.
        """
        column = int((mouse_pos[0] - self.board_offset) // 100)
        row = int((mouse_pos[1] - self.board_offset) // 100)
        if 0 <= column <= 5 and 0 <= row <= 5 and self.layout[row][column] != 0:
            return self.layout[row][column]
        return None
