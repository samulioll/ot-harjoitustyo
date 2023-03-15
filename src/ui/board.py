import pygame
from ui.sprites.car import Car
from ui.sprites.background import Background

class Board:
    def __init__(self, level_layout):
        self.cell_size = 100
        self.offset = 300

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

        self._initialize_sprites(level_layout)
    
    def _initialize_sprites(self, level_layout):
        """
        Create the collection of sprites and their locations at the start.
        """
        self.board = Background("background", 300, 300)
        self.background.add(self.board)

        for y in range(6):
            for x in range(6):
                cell = level_layout[y][x]
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



    def move_car(self, selected, mouse_pos, offset):
        """
        Arguments:
            selected:   ID of selected car
            mouse_pos:  tuple of current mouse coordinates
            offset:     difference between clicked position and the original position of the selected car
        """
        others = pygame.sprite.Group()
        for car in self.cars:
            if car.id != selected:
                others.add(car)
            else:
                sel = car
        # Handle movement for Red car
        if sel.id == "Red":
            new_pos = mouse_pos[0] - offset[0]
            if 300 <= new_pos <= (900):
                old_pos = sel.rect.x
                sel.rect.x = mouse_pos[0] - offset[0]
                colliding = pygame.sprite.spritecollide(sel, others, False)
                if colliding:
                    sel.rect.x = old_pos
        # Handle movement for cars that move on x-axis
        elif sel.move_axis == "x":
            new_pos = mouse_pos[0] - offset[0]
            if 300 <= new_pos <= (900 - sel.width):
                old_pos = sel.rect.x
                sel.rect.x = mouse_pos[0] - offset[0]
                colliding = pygame.sprite.spritecollide(sel, others, False)
                if colliding:
                    sel.rect.x = old_pos
        # Handle movement for cars that move on y-axis
        else:
            new_pos = mouse_pos[1] - offset[1]
            if 300 <= new_pos <= (900 - sel.height):
                old_pos = sel.rect.y
                sel.rect.y = mouse_pos[1] - offset[1]
                colliding = pygame.sprite.spritecollide(sel, others, False)
                if colliding:
                    sel.rect.y = old_pos