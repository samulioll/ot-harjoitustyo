import pygame as pg
from .car import Car
from .ui_element import UiElement

class Board:
    """
    Simulates the board and keeps track of all pieces.
    """

    def __init__(self, level):
        self.cell_size = 100
        self.board_offset = 300
        self.layout = [[0,0,0,"Yellow",0,0],
                        [0,0,0,"Yellow-1",0,0],
                        [0,"Red","Red-1","Yellow-2",0,0],
                        [0,0,0,0,0,0],
                        [0,0,0,0,0,0],
                        [0,0,0,"Blue","Blue-1",0]]

        self.red2x1 = None
        self.blue2x1 = None
        self.orange2x1 = None
        self.magenta2x1 = None
        self.brown2x1 = None
        self.white3x1 = None
        self.purple1x2 = None
        self.black1x2 = None
        self.lime1x2 = None
        self.grey1x3 = None
        self.green1x3 = None
        self.yellow1x3 = None

        self.background = pg.sprite.Group()
        self.cars = pg.sprite.Group()
        self.all_sprites = pg.sprite.Group()

        self._initialize_sprites()
    

    def _initialize_sprites(self):
        """
        Create the collection of sprites and their locations at the start.
        """
        self.backdrop = UiElement("backdrop_1", 0, 0)
        self.board = UiElement("Board_1", 298, 294)
        self.full_game_view = UiElement("full_game_view_1", 0, 0)
        self.background.add(self.full_game_view)

        for y in range(6):
            for x in range(6):
                cell = self.layout[y][x]
                x_coord = x * self.cell_size + self.board_offset
                y_coord = y * self.cell_size + self.board_offset

                if cell == "Red":
                    self.red2x1 = Car("red2x1", x_coord, y_coord)
                    self.cars.add(self.red2x1)
                elif cell == "Blue":
                    self.blue2x1 = Car("blue2x1", x_coord, y_coord)
                    self.cars.add(self.blue2x1)
                elif cell == "Orange":
                    self.orange2x1 = Car("orange2x1", x_coord, y_coord)
                    self.cars.add(self.orange2x1)
                elif cell == "Magenta":
                    self.magenta2x1 = Car("blue2x1", x_coord, y_coord)
                    self.cars.add(self.blue2x1)
                elif cell == "Brown":
                    self.brown2x1 = Car("brown2x1", x_coord, y_coord)
                    self.cars.add(self.brown2x1)
                elif cell == "White":
                    self.white3x1 = Car("white3x1", x_coord, y_coord)
                    self.cars.add(self.white3x1)
                elif cell == "Purple":
                    self.purple1x2 = Car("purple1x2", x_coord, y_coord)
                    self.cars.add(self.purple1x2)
                elif cell == "Black":
                    self.black1x2 = Car("black1x2", x_coord, y_coord)
                    self.cars.add(self.black1x2)
                elif cell == "Lime":
                    self.lime1x2 = Car("lime1x2", x_coord, y_coord)
                    self.cars.add(self.lime1x2)
                elif cell == "Grey":
                    self.grey1x3 = Car("grey1x3", x_coord, y_coord)
                    self.cars.add(self.grey1x3)
                elif cell == "Green":
                    self.green1x3 = Car("green1x3", x_coord, y_coord)
                    self.cars.add(self.green1x3)
                elif cell == "Yellow":
                    self.yellow1x3 = Car("yellow1x3", x_coord, y_coord)
                    self.cars.add(self.yellow1x3)


    def move_car(self, selected: str, mouse_pos: tuple, board_offset: int):
        """
        Arguments:
            selected:   ID of selected car
            mouse_pos:  tuple of current mouse coordinates
            board_offset:     difference between clicked position and the original position of the selected car
        """

        # Get car id from matrix
        if "-" in selected:
            parts = selected.split("-")
            id = parts[0]
        else:
            id = selected
        # add all of the cars that are ont selected to a group to detect collisions with
        others = pg.sprite.Group()
        for car in self.cars:
            if car.id != id:
                others.add(car)
            else:
                sel = car
        # Handle movement for cars that move on x-axis
        if sel.move_axis == "x":
            red_bonus = 200 if "Red" in sel.id else 0
            if "1" in selected:
                diff = board_offset[0] + 100
            elif "2" in selected:
                diff = board_offset[0] + 200
            else:
                diff = board_offset[0]
            new_pos = mouse_pos[0] - diff
            old_pos = sel.rect.x
            if 300 <= new_pos<= (900 - sel.width + red_bonus):
                if new_pos >= old_pos + 99 or new_pos <= old_pos - 99:
                    return
                sel.rect.x = new_pos
                colliding = pg.sprite.spritecollide(sel, others, False)
                if colliding:
                    sel.rect.x = old_pos
        # Handle movement for cars that move on y-axis
        elif sel.move_axis == "y":
            if "1" in selected:
                diff = board_offset[1] + 100
            elif "2" in selected:
                diff = board_offset[1] + 200
            else:
                diff = board_offset[1]
            new_pos = mouse_pos[1] - diff
            old_pos = sel.rect.y
            if 300 <= new_pos <= (900 - sel.height):
                if new_pos >= old_pos + 50 or new_pos <= old_pos - 50:
                    return
                sel.rect.y = new_pos
                colliding = pg.sprite.spritecollide(sel, others, False)
                if colliding:
                    sel.rect.y = old_pos
    


    def drop_car(self, selected: str):
        """
        Arguments:
            selected:   ID of selected car
        """
        if "-" in selected:
            parts = selected.split("-")
            id = parts[0]
        else:
            id = selected
        for car in self.cars:
            if car.id == id:
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
        elif sel.move_axis == "y":
            cells = sel.height // 100
            old_pos = sel.rect.y
            diff = old_pos % 100
            if diff < 50:
                sel.rect.y = old_pos - diff
            else:
                sel.rect.y = old_pos + (100 - diff)
        # Clear old car position info from matrix
        old_pos = []
        for y in range(6):
            for x in range(6):
                cell = self.layout[y][x]
                if cell == id:
                    old_pos.append((x,y))
                    cell = 0
                    if sel.move_axis == "x":
                        for i in range(cells):
                            self.layout[y][x+i] = 0
                    elif sel.move_axis == "y":
                        for i in range(cells):
                            self.layout[y+i][x] = 0
        # Add new car position info to matrix
        x_cell = sel.rect.x // 100 - 3
        y_cell = sel.rect.y // 100 - 3
        if sel.move_axis == "x":
            try:
                for i in range(cells):
                    if i > 0:
                        self.layout[y_cell][x_cell+i] = sel.id + "-" + str(i)
                    else:
                        self.layout[y_cell][x_cell+i] = sel.id
            except:
                return (True, True)
        elif sel.move_axis == "y":
            for i in range(cells):
                if i > 0:
                    self.layout[y_cell+i][x_cell] = sel.id + "-" + str(i)
                else:
                    self.layout[y_cell+i][x_cell] = sel.id
        # Check if move happened
        changed = False
        new_pos = []
        for y in range(6):
            for x in range(6):
                cell = self.layout[y][x]
                if cell == id:
                    new_pos.append((x,y))
        if new_pos != old_pos:
            changed = True
        return (changed, False)
    
    def get_selected(self, mouse_pos):
        x = (mouse_pos[0] - self.board_offset) // 100
        y = (mouse_pos[1] - self.board_offset) // 100
        if 0 <= x <= 5 and 0 <= y <= 5:
            return self.layout[y][x] if self.layout[y][x] != 0 else None
    



