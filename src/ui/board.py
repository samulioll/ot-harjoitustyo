import pygame
from ui.sprites.car import Car
from ui.sprites.background import Background

class Board:
    def __init__(self, level_layout):
        self.cell_size = 100
        self.offset = 300
        self.level_layout = level_layout

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

        self.background = pygame.sprite.Group()
        self.cars = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()

        self._initialize_sprites(self.level_layout)
    

    def _initialize_sprites(self, level_layout: list):
        """
        Create the collection of sprites and their locations at the start.
        """
        self.board = Background("background", 300, 300)
        self.background.add(self.board)

        for y in range(6):
            for x in range(6):
                cell = self.level_layout[y][x]
                x_coord = x * self.cell_size + self.offset
                y_coord = y * self.cell_size + self.offset

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
        
        for car in self.cars:
            if car.move_axis == "x":
                cells = car.width // 100
                x_cell = (car.rect.x - 300) // 100
                y_cell = (car.rect.y - 300) // 100
                for i in range(cells):
                    if i > 0:
                        self.level_layout[y_cell][x_cell+i] = car.id + "-" + str(i)
                    else:
                        self.level_layout[y_cell][x_cell+i] = car.id
            if car.move_axis == "y":
                cells = car.height // 100
                x_cell = (car.rect.x - 300) // 100
                y_cell = (car.rect.y - 300) // 100
                for i in range(cells):
                    if i > 0:
                        self.level_layout[y_cell+i][x_cell] = car.id + "-" + str(i)
                    else:
                        self.level_layout[y_cell+i][x_cell] = car.id



    def move_car(self, selected: str, mouse_pos: tuple, offset: int):
        """
        Arguments:
            selected:   ID of selected car
            mouse_pos:  tuple of current mouse coordinates
            offset:     difference between clicked position and the original position of the selected car
        """
        others = pygame.sprite.Group()
        # Get car id from matrix
        if "-" in selected:
            parts = selected.split("-")
            id = parts[0]
        else:
            id = selected
        # add all of the cars that are ont selected to a group to detect collisions with
        for car in self.cars:
            if car.id != id:
                others.add(car)
            else:
                sel = car
        # Handle movement for Red car
        if "Red" in sel.id:
            if "1" in selected:
                diff = offset[0] + 100
            else:
                diff = offset[0]
            new_pos = mouse_pos[0] - diff
            old_pos = sel.rect.x
            if 300 <= new_pos <= (900):
                if new_pos >= old_pos + 50:
                    return
                sel.rect.x = new_pos
                colliding = pygame.sprite.spritecollide(sel, others, False)
                if colliding:
                    sel.rect.x = old_pos
        # Handle movement for cars that move on x-axis
        elif sel.move_axis == "x":
            if "1" in selected:
                diff = offset[0] + 100
            elif "2" in selected:
                diff = offset[0] + 200
            else:
                diff = offset[0]
            new_pos = mouse_pos[0] - diff
            old_pos = sel.rect.x
            if 300 <= new_pos<= (900 - sel.width):
                if new_pos >= old_pos + 50:
                    return
                sel.rect.x = new_pos
                colliding = pygame.sprite.spritecollide(sel, others, False)
                if colliding:
                    sel.rect.x = old_pos
        # Handle movement for cars that move on y-axis
        elif sel.move_axis == "y":
            if "1" in selected:
                diff = offset[1] + 100
            elif "2" in selected:
                diff = offset[1] + 200
            else:
                diff = offset[1]
            new_pos = mouse_pos[1] - diff
            old_pos = sel.rect.y
            if 300 <= new_pos <= (900 - sel.height):
                if new_pos >= old_pos + 50:
                    return
                sel.rect.y = new_pos
                colliding = pygame.sprite.spritecollide(sel, others, False)
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
        for y in range(6):
            for x in range(6):
                cell = self.level_layout[y][x]
                if cell == id:
                    cell = 0
                    if sel.move_axis == "x":
                        for i in range(cells):
                            self.level_layout[y][x+i] = 0
                    elif sel.move_axis == "y":
                        for i in range(cells):
                            self.level_layout[y+i][x] = 0
        # Add new car position info to matrix
        x_cell = sel.rect.x // 100 - 3
        y_cell = sel.rect.y // 100 - 3
        if id == "Red":
            try:
                for i in range(cells):
                    if i > 0:
                        self.level_layout[y_cell][x_cell+i] = sel.id + "-" + str(i)
                    else:
                        self.level_layout[y_cell][x_cell+i] = sel.id
            except:
                print("LEVEL SOLVED")
        elif sel.move_axis == "x":
            for i in range(cells):
                if i > 0:
                    self.level_layout[y_cell][x_cell+i] = sel.id + "-" + str(i)
                else:
                    self.level_layout[y_cell][x_cell+i] = sel.id
        elif sel.move_axis == "y":
            for i in range(cells):
                if i > 0:
                    self.level_layout[y_cell+i][x_cell] = sel.id + "-" + str(i)
                else:
                    self.level_layout[y_cell+i][x_cell] = sel.id


