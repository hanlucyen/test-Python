from turtle import *
from shapes import *
#create a turtle named Tie:
Tie = Turtle()
Tie.shape("turtle")
Tie.speed(8)

#draw three circles:
draw_circle(Tie,"green",50,25,0)
draw_circle(Tie,"blue",50,0,0)
draw_circle(Tie,"yellow",50,-25,0)

#write a little message:
Tie.penup()
Tie.goto(0.-50)
Tie.color("black")
Tie.write("Teach With Code!",None, "center","16pt bold")
Tie.goto(0,-80)
