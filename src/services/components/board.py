from copy import deepcopy
import pygame as pg
from services.components.objects.car import Car
from services.components.objects.ui_element import UiElement

class Board:
    """
    Simulates the board and keeps track of all pieces.
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
                        "Yellow": "yellow1x3"}
        self.background = pg.sprite.Group()
        self.cars = pg.sprite.Group()
        self.font = pg.font.SysFont("Arial", 50)
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

    def move_car(self, selected: str, mouse_pos: tuple, board_offset: int):
        """ Handles the movement of cars. """
        # Get car id from matrix
        if "-" in selected:
            parts = selected.split("-")
            car_id = parts[0]
        else:
            car_id = selected
        # add all of the non-selected cars to a group to detect collisions with
        others = pg.sprite.Group()
        for car in self.cars:
            if car.car_id != car_id:
                others.add(car)
            else:
                sel = car
        # Handle movement for cars that move on x-axis
        if sel.move_axis == "x":
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
        # Handle movement for cars that move on y-axis
        else:
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
        """ Handles the matrix changes of moving a car. """
        if "-" in selected:
            parts = selected.split("-")
            car_id = parts[0]
        else:
            car_id = selected
        for car in self.cars:
            if car.car_id == car_id:
                sel = car
        # Get car info
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
        # Clear old car position info from matrix
        old_pos = []
        for row in range(6):
            for column in range(6):
                cell = self.layout[row][column]
                if cell == car_id:
                    old_pos.append((column, row))
                    cell = 0
                    if sel.move_axis == "x":
                        for i in range(cells):
                            self.layout[row][column+i] = 0
                    else:
                        for i in range(cells):
                            self.layout[row+i][column] = 0
        # Add new car position info to matrix
        x_cell = sel.rect.x // 100 - 3
        y_cell = sel.rect.y // 100 - 3
        if sel.move_axis == "x":
            try:
                for i in range(cells):
                    if i > 0:
                        self.layout[y_cell][x_cell+i] = sel.car_id + "-" + str(i)
                    else:
                        self.layout[y_cell][x_cell+i] = sel.car_id
            except:
                print("SOLVED")
                return (True, True)
        else:
            for i in range(cells):
                if i > 0:
                    self.layout[y_cell+i][x_cell] = sel.car_id + "-" + str(i)
                else:
                    self.layout[y_cell+i][x_cell] = sel.car_id
        # Check if move happened
        changed = False
        new_pos = []
        for row in range(6):
            for column in range(6):
                cell = self.layout[row][column]
                if cell == car_id:
                    new_pos.append((column, row))
        if new_pos != old_pos:
            changed = True
        return (changed, False)

    def get_selected(self, mouse_pos):
        """ Returns the car id of clicked cell. """
        column = (mouse_pos[0] - self.board_offset) // 100
        row = (mouse_pos[1] - self.board_offset) // 100
        if 0 <= column <= 5 and 0 <= row <= 5:
            return self.layout[row][column] if self.layout[row][column] != 0 else None
    
    def draw_score(self, moves, time):
        text_moves = self.font.render(str(moves), True, (0,0,0), None)
        text_time = self.font.render(time, True, (0,0,0), None)
        return text_moves, text_time
