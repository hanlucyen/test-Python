"""
from turtle import *
color('cyan')
bgcolor('black')
hideturtle()
speed(11)
n=1
while True:
    circle(n,88)
    n=n+1
    left(179)
"""
from turtle import *
bgcolor('black')
hideturtle()
speed(11)
for i in range(120):
    if i % 2==0:
        color('cyan')
    else:
        color('magenta')
    forward(i*3)
    left(91)
done()
