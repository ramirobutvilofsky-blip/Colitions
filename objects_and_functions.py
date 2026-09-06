import numpy as np
import pygame as pg
import itertools as it

#------------------------------------------------------------------------------------
# SCREEN

width = 500
heigh = 500

screen = (width, heigh)

display = pg.display.set_mode((screen[0],screen[1]))

# ----------------------------------------------------------------------------------------------
# TIEMPO ----------------------------------------------------------------------------------------------

clock = pg.time.Clock()
dt = clock.tick(1000)/1000

#-------------------------------------------------------------------------------------
# CLASES

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

#--------------------------------------------------------------------------------------
# OBJETOS

rng = np.random.default_rng()

punto_m = []

for punto in range(30):

    masa = rng.uniform(1,12)
    radio = masa*1/2

    punto = Punto(rng.uniform((-screen[0]/2) + radio , (screen[0]/2)-radio), rng.uniform((-screen[1]/2) + radio, (screen[1]/2) - radio) , rng.uniform(-2000,2000) , rng.uniform(-2000,2000),0,5000,
    (rng.integers(220,255),rng.integers(220,255),rng.integers(220,255)),masa, radio)

    punto_m.append(punto)

# ----------------------------------------------------------------------------------------------
# COMBINACIONES 1 A 1 ----------------------------------------------------------------------------------------------

combinaciones = it.combinations(punto_m , 2)

comb = list(combinaciones)

#--------------------------------------------------------------------------------------
# BORDES

def colisiones_multiples_bordes(c):

    for i in c:

        if (i.x >= screen[0]/2 - i.radius):

            i.x -= 3
            i.vx = -i.vx

        elif (i.x <= -screen[0]/2 + i.radius):

            i.x += 3
            i.vx = -i.vx

        elif (i.y >= screen[1]/2 - i.radius):

            i.y -= 3
            i.vy = -i.vy

        elif (i.y <= -screen[1]/2 + i.radius):

            i.y += 3
            i.vy = -i.vy
    
#---------------------------------------------------------------
# CHOQUE ELASTICO

def choque_elastico_multiple(c):

    for i in c:

        j = i

        v01x = j[0].vx
        v02x = j[1].vx

        v01y = j[0].vy
        v02y = j[1].vy

        vector_1 = np.array([j[0].x , j[0].y])
        
        vector_2 = np.array([j[1].x , j[1].y])

        vector_dif = vector_2 - vector_1

        modulo_distancia = np.sqrt(vector_dif[0]**2 + vector_dif[1]**2)

        if modulo_distancia < (j[0].radius + j[1].radius):

            j[0].vx = ((j[0].mass - j[1].mass)/(j[0].mass + j[1].mass)) * v01x + (2*j[1].mass/(j[0].mass + j[1].mass) * v02x)

            j[1].vx = (2*j[0].mass/(j[0].mass + j[1].mass) * v01x) + ((j[1].mass - j[0].mass)/(j[0].mass + j[1].mass)) * v02x

            j[0].vy = ((j[0].mass - j[1].mass)/(j[0].mass + j[1].mass)) * v01y + (2*j[1].mass/(j[0].mass + j[1].mass) * v02y)

            j[1].vy = (2*j[0].mass/(j[0].mass + j[1].mass) * v01y) + ((j[1].mass - j[0].mass)/(j[0].mass + j[1].mass)) * v02y

# ----------------------------------------------------------------------------------------------
# DIBUJOS EN PANTALLA ----------------------------------------------------------------------------------------------

def plasmar():

    for punto in punto_m:

        punto.draw(display)

def movimiento():

    for punto in punto_m:

        punto.vx += punto.ax*dt # aceleracion en x
        punto.vy += punto.ay*dt # aceleracion en y

        punto.x += punto.vx*dt  
        punto.y += punto.vy*dt

