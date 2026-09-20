import numpy as np
import pygame as pg
from mass_creator import mass_n, cells
from parameters import screen, display
from functions import dynamics, contact

# ------------------------------------------ SIMULATION ----------------------------------------------------

pg.init()

running = True

while running:

    # SYSTEM ------------------------------------------------

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    display.fill((1, 1, 1))

    # OBJECTS ------------------------------------

    for mass in mass_n:

        dynamics(mass)
        mass.draw(display)

    contact(cells)

    # REFRESH IMAGE ---------------------------------------------------------

    pg.display.update()

pg.quit()