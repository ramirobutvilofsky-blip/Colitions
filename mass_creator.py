import numpy as np
import pygame as pg
import itertools as it
from parameters import screen, display, g, n

w = screen[0]
h = screen[1]

class Ball():

    def __init__(self, mass, radius, color, pos, vel, acc):
        
        self.mass = mass
        self.radius = radius
        self.color = color
        self.pos = np.array(pos).astype(float)
        self.vel = np.array(vel).astype(float)
        self.acc = np.array(acc).astype(float)
        self.cell = None

        self.pos[1] = self.pos[1]*(-1)
        self.vel[1] = self.vel[1]*(-1)
        self.acc[1] = self.acc[1]*(-1)

    def draw(self,screen):

        pg.draw.circle(screen,self.color, (w/2 + self.pos[0], h/2 + self.pos[1]), radius=self.radius, width=0)

# ------------------------------------------ MASS CREATOR ----------------------------------------------------

rng = np.random.default_rng()

mass_n = []

cellx = w/n
celly = h/n

cells = {}

j = 0

while j < n:

    for i in range(n):

        cells[f'cell_{j}_{i}'] = []

    j +=1

for punto in range(10000):

    mass = rng.uniform(1.9,1.9)

    radius = mass*1

    mass_i = Ball(mass , radius, (rng.uniform(180,220),rng.uniform(1,180),rng.uniform(180,220)), (rng.uniform(-w/2+radius,w/2-radius),rng.uniform(-h/2+radius,h/2-radius)), (rng.uniform(-300,300) , rng.uniform(-300,300)),(0,g))

    mass_n.append(mass_i)

    m_cellx = int((mass_i.pos[0]+(w/2)) // cellx)
    m_celly = int((mass_i.pos[1]+(h/2)) // celly)

    mass_i.cell = f'cell_{str(m_celly)}_{str(m_cellx)}'

    cells[f'cell_{str(m_celly)}_{str(m_cellx)}'].append(mass_i)
