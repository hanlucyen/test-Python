# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 07:19:16 2021

@author: ASUS
"""

import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

#nhap toa do dinh
verticies=(
    (1,-1,-1),
    (1,1,-1),
    (-1,1,-1),
    (-1,-1,-1),
    (1,-1,1),
    (1,1,1,),
    (-1,-1,1),
    (-1,1,1)
    )
#nhap toa do canh
edges=(
       (0,1),
       (0,3),
       (0,4),
       (2,1),
       (2,3),
       (2,7),
       (6,3),
       (6,4),
       (6,7),
       (5,1),
       (5,4),
       (5,7)
       )
#mau
colors=(
        (1,0,0),
        (0,1,0),
        (0,0,1),
        (0,1,0),
        (1,1,1),
        (0,1,1),
        (1,0,0),
        (0,1,0),
        (0,0,1),
        (1,0,0),
        (1,1,1),
        (0,1,1)
        )

def Cube():
    glBegin(GL_QUADS)
    for surface in surface:
        x=0
        for vertex in surface:
            x+=1
            glColor3fv(colors[x])
            glVertex3fx(verticies[vertex])
    glEnd()
    
    glBegin(Gl_LINES)
    for edge in edge:
        for vertex in edge:
            glVertex3fv(verticies[vertex])
    glEnd()
    
    

#be mat
surfaces=((0,1,2,3),(3,2,7,6),(6,7,5,4),(4,5,1,0),(1,5,7,2),(4,0,3,6))

def main():
    pygame.init()
    display=(800,600)
    pygame.display.set_mode(display,DOUBLEBUF|OPENGL)
    
    gluPerspective(45,(display[0]/display[1]),0.1,50.0)
    
    glTranslatef(0,0,-10)
    
    glRotatef(25,2,1,0)
    
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
                
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    glTranslatef(-0.5,0,0)
                if event.key==pygame.K_RIGHT:
                    glTranslatef(0.5,0,0)
                    
                if event.key==pygame.K_UP:
                    glTranslatef(0,1,0)
                if event.key==pygame.K_DOWN:
                    glTranslatef(0,-1,0)
            
            if event.type==pygame.MOUSEBUTTONDOWN:
                if envent.button==4:
                    glTranslatef(0,0,1.0)
                    
                if event.button==5:
                    glTranslatef(0,0,-1.0)
                
        #glRtatef(1,3,1,1)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        Cube()
        pygame.display.flip()
        pygame.time.wait(10)



main()