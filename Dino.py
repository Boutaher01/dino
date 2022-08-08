import pygame as pg
from time import sleep

pg.init()

red = 255,0,0
yellow = 255,255,0
pink = 0,255,255

sc = pg.display.set_mode((800,600))
sc.fill(yellow)

sq = pg.Rect(400,550,50,50)
pg.draw.rect(sc,red,sq)

pg.display.flip()

while True:
  pass
