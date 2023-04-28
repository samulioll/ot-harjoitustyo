import pygame as pg

pg.init()

CAPTION = "RUSH HOUR"
screen_size = (505, 305)
screen_rect = pg.Rect((0, 0), screen_size)

pg.display.set_caption(CAPTION)
_screen = pg.display.set_mode(screen_size)
