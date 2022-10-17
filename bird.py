
from game 
from ursina import *
app=Ursina()
Sky()
bird=Animation('assets\img',collider='bax',scale=(2,2,2),y=5)
camera.orthographic=True
camera.fov=20
def update():
    bird.y=bird.y-4*time.dt
    for p in pipes:
        p.x=p.x-2*time.dt
def input(key):
    if key=='space':
        bird.y=bird.y+3


pipe =[]
pipe=Entity(model='quad',color=color.green,texture='white_cubo',position=(20,10),scale=(3,15,1),collider='box')
import random as r
def newPipe():
    y=r.randint(4,12)
    new1=duplicate(pipe,y=y)
    new2=duplicate(pipe,y=y-22)
    pipes.extend((new1,new2))
    invoke(newPipe,delay=5)
newPipe()
app.run()
