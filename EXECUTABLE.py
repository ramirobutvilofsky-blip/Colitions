import numpy as np
import pygame as pg
import itertools as it

from objects_and_functions import Punto
from objects_and_functions import screen, display, punto_m, comb, dt
from objects_and_functions import choque_elastico_multiple, colisiones_multiples_bordes, plasmar, movimiento

#-------------------------------------------------------------------------------
# INICIO

pg.init()

# Simulacion --------------------------------------------------------------------
#--------------------------------------------------------------------------------

running = True

while running:

    # SISTEMA ------------------------------------------------

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    display.fill((1, 1, 1))

    # OBJETOS EN PANTALLA ------------------------------------

    plasmar()
    
    movimiento()

    # CHOQUES ----------------------------------------------------------

    choque_elastico_multiple(comb)

    colisiones_multiples_bordes(punto_m)

    # ACTUALIZAR IMAGEN ---------------------------------------------------------

    pg.display.update()

pg.quit()
