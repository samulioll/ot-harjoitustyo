import os
import pygame as pg
from . import engine

pg.init()


caption = "RUSH HOUR"
screen_size = (1200, 1200)
screen_rect = pg.Rect((0,0), screen_size)

pg.display.set_caption(caption)
_screen = pg.display.set_mode(screen_size)
