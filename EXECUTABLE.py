import numpy as np
import pygame as pg
from objects_and_functions import punto1, punto2
from objects_and_functions import screen
from objects_and_functions import choque_elastico, colisiones_bordes

#-------------------------------------------------------------------------------
# INICIO

pg.init()

screen

# Simulacion --------------------------------------------------------------------
#--------------------------------------------------------------------------------

running = True

clock = pg.time.Clock()

while running:

    # SISTEMA ------------------------------------------------

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    dt = clock.tick(1000)/1000

    screen.fill((1, 1, 1))

    # OBJETOS EN PANTALLA ------------------------------------

    punto1.draw(screen)
    punto2.draw(screen)

    # MOVIMIENTO ---------------------------------------------

    punto1.vx += punto1.ax*dt # aceleracion en x
    punto1.vy += punto1.ay*dt # aceleracion en y

    punto1.x += punto1.vx*dt  
    punto1.y += punto1.vy*dt

    punto2.vx += punto2.ax*dt # aceleracion en y
    punto2.vy += punto2.ay*dt # aceleracion en y

    punto2.x += punto2.vx*dt 
    punto2.y += punto2.vy*dt

    # CHOQUES ----------------------------------------------------------

    choque_elastico()

    colisiones_bordes()

    # ACTUALIZAR IMAGEN ---------------------------------------------------------

    pg.display.update()

pg.quit()


