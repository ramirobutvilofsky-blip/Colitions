import numpy as np
import pygame as pg

#------------------------------------------------------------------------------------
# SCREEN

width = 1500
heigh = 800

screen = pg.display.set_mode((width,heigh))

#-------------------------------------------------------------------------------------
# Clases

class Punto():

    def __init__(self, x, y, vx, vy, ax, ay, color, mass, radius):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.ax = ax
        self.ay = ay
        self.color = color
        self.radius = radius
        self.mass = mass

    def draw(self, screen):
        x = self.x + width/2
        y = self.y + heigh/2
        pg.draw.circle(screen, self.color, (x,y) , self.radius)

punto1 = Punto(-100, 0 , 1200 , 0 , 0 , 2000 , (140,60,60) , 100 , 70)
punto2 = Punto(100 , 0 , -200 , -800 , 0 , 2000 , (200,200,220) , 40 , 30)

#--------------------------------------------------------------------------------------
# BORDES

def colisiones_bordes():

    if (punto1.x >= width/2 - punto1.radius):

        punto1.vx = -punto1.vx

    elif (punto1.x <= -width/2 + punto1.radius):

        punto1.vx = -punto1.vx

    elif (punto2.x >= width/2 - punto2.radius):

        punto2.vx = -punto2.vx

    elif (punto2.x <= -width/2 + punto2.radius):

        punto2.vx = -punto2.vx

    elif (punto1.y >= heigh/2 - punto1.radius):

        punto1.vy = -punto1.vy

    elif (punto1.y <= -heigh/2 + punto1.radius):

        punto1.vy = -punto1.vy

    elif (punto2.y >= heigh/2 - punto2.radius):

        punto2.vy = -punto2.vy

    elif (punto2.y <= -heigh/2 + punto2.radius):

        punto2.vy = -punto2.vy
    
#---------------------------------------------------------------
# CHOQUE ELASTICO

def choque_elastico():

    v01x = punto1.vx
    v02x = punto2.vx

    v01y = punto1.vy
    v02y = punto2.vy

    vector_1 = np.array([punto1.x , punto1.y])
    
    vector_2 = np.array([punto2.x , punto2.y])

    vector_dif = vector_2 - vector_1

    modulo_distancia = np.sqrt(vector_dif[0]**2 + vector_dif[1]**2)

    if modulo_distancia < (punto1.radius + punto2.radius):

        punto1.vx = ((punto1.mass - punto2.mass)/(punto1.mass + punto2.mass)) * v01x + (2*punto2.mass/(punto1.mass + punto2.mass) * v02x)

        punto2.vx = (2*punto1.mass/(punto1.mass + punto2.mass) * v01x) + ((punto2.mass - punto1.mass)/(punto1.mass + punto2.mass)) * v02x

        punto1.vy = ((punto1.mass - punto2.mass)/(punto1.mass + punto2.mass)) * v01y + (2*punto2.mass/(punto1.mass + punto2.mass) * v02y)

        punto2.vy = (2*punto1.mass/(punto1.mass + punto2.mass) * v01y) + ((punto2.mass - punto1.mass)/(punto1.mass + punto2.mass)) * v02y

    