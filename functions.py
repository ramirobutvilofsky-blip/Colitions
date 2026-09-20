import numpy as np
import pygame as pg
import itertools as it
from parameters import screen,display, n, e
from mass_creator import mass_n, cellx, celly, cells

# ------------------------------------------ PARAMETERS ----------------------------------------------------

w = screen[0]
h = screen[1]

clock = pg.time.Clock()
dt = clock.tick(1000)/67 #TIME

# ------------------------------------------ FUNCTIONS ----------------------------------------------------

# MOVEMEMENT -------

def dynamics(m):

    old_key = m.cell

    cells[old_key].remove(m)

    m.vel[0] += m.acc[0]*dt
    m.vel[1] += m.acc[1]*dt     #-------------------------
                                #POSITION CHANGER
    m.pos[0] += m.vel[0]*dt     #-------------------------
    m.pos[1] += m.vel[1]*dt

    if m.pos[0] >= (w/2 - m.radius):
        
        m.pos[0] = w/2 - m.radius
        
        m.vel[0] = -m.vel[0]*e

    if m.pos[0] <= (-w/2 + m.radius):
        
        m.pos[0] = -w/2 + m.radius
        
        m.vel[0] = -m.vel[0]*e

    if m.pos[1] >= (h/2 - m.radius):
        
        m.pos[1] = h/2 - m.radius
        
        m.vel[1] = -m.vel[1]*e

    if m.pos[1] <= (-h/2 + m.radius):
        
        m.pos[1] = -h/2 + m.radius
        
        m.vel[1] = -m.vel[1]*e

    m_cellx = int((m.pos[0]+(w/2)) // cellx)
    m_celly = int((m.pos[1]+(h/2)) // celly)

    new_key = f'cell_{int(m_celly)}_{int(m_cellx)}'

    m.cell = new_key

    cells[new_key].append(m)
    
# COLITION -------

def contact(c):

    for k,v in c.items():

        combinations = it.combinations(v,2)

        comb = list(combinations)
            
        for duo in comb:

            m1 = duo[0]
            m2 = duo[1]

            position_m1 = np.array([m1.pos[0], m1.pos[1]])

            position_m2 = np.array([m2.pos[0], m2.pos[1]])       #CALCULATE THE DIFFERENCE VECTOR BETWEEN RADIUS

            diff = position_m2-position_m1

            dist = np.sqrt(diff @ diff) - (m1.radius + m2.radius)
            
            if dist <= 0:

                n = diff/(np.sqrt(diff[0]**2 + diff[1]**2))
                t = np.array([-n[1],n[0]])

                diffspeed = m1.vel - m2.vel
                diffspeed_n = diffspeed @ n   # MINIMUM SPEED FOR COLITION

                if diffspeed_n > 0:

                    vi1x = m1.vel[0]
                    vi1y = m1.vel[1]

                    V1_n = vi1x*n[0]+vi1y*n[1]
                    V1_t = vi1x*t[0]+vi1y*t[1]

                    vi2x = m2.vel[0]
                    vi2y = m2.vel[1]

                    V2_n = vi2x*n[0]+vi2y*n[1]
                    V2_t = vi2x*t[0]+vi2y*t[1]

                    V1_nf = (((m1.mass - m2.mass)/(m1.mass + m2.mass)) * V1_n + (2*m2.mass/(m1.mass + m2.mass)) * V2_n)  
                    V1_tf = V1_t  

                    V2_nf = ((2*m1.mass/(m1.mass + m2.mass) * V1_n) + ((m2.mass - m1.mass)/(m1.mass + m2.mass)) * V2_n)
                    V2_tf = V2_t

                    m1.vel[0] = (V1_nf*n[0]+V1_tf*t[0])*e
                    m1.vel[1] = (V1_nf*n[1]+V1_tf*t[1])*e

                    m2.vel[0] = (V2_nf*n[0]+V2_tf*t[0])*e
                    m2.vel[1] = (V2_nf*n[1]+V2_tf*t[1])*e

                #POSITION CORRECTION FOR OVERLAPING

                correction = -dist
                
                m1.pos[0] -= n[0]*correction/2
                m1.pos[1] -= n[1]*correction/2

                m2.pos[0] += n[0]*correction/2
                m2.pos[1] += n[1]*correction/2
