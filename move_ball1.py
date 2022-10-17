from graphics import *
import random
from math import *

def distance( P1, P2 ):
     # computes distance for ball-on-ball collisions
     x = sqrt(pow(P1.getX() - P2.getX(), 2) + pow(P1.getY() - P2.getY(), 2))
     return x

def isInside(c, r, P1, P2, cr):
     # calculates whether a ball is inside a black box
     xc = c.getCenter().getX()
     yc = c.getCenter().getY()
     x1 = P1.getX()
     y1 = P1.getY()
     x2 = P2.getX()
     y2 = P2.getY()
     if (x1 + cr <= xc <= x2 - cr) and (y1 + cr <= yc <= y2 - cr):
          return 0
     
def bounce(c, r, P1, P2, cr):
     # calculates if outside edges of ball are touching white box
     xc = c.getCenter().getX()
     yc = c.getCenter().getY()
     x1 = P1.getX()
     y1 = P1.getY()
     x2 = P2.getX()
     y2 = P2.getY()
     if (x1 - cr <= xc <= x2 + cr) and (y1 - cr <= yc <= y2 + cr):
          return 0
 
def main():
    # opens a graphics window
    W = 600
    H = 400
    win = GraphWin("111a-be's billiard program", W, H)
    win.setBackground(color_rgb(25, 25, 112))

    # defines colors balls can be
    colors = ["red", "blue", "green", "yellow", "black", "white"]
 
    # draw 1st ball at random place with random velocity and random color
    c1r = random.randrange(10, 20)
    c1 = Circle(Point(random.randrange(50, W//2 - 50),      # random X
                        random.randrange(50, H//2 - 50)),   # random Y
                        c1r)                                # random radius
    c1color = colors[random.randrange(5)]                   # random color
    c1.setFill(c1color)
    c1.setOutline(c1color)
    dirX1 = random.randrange(-5, 5)                         # random X speed
    if dirX1 == 0:                                          # X can't be 0
         dirX1 = dirX1 + 1
    dirY1 = random.randrange(-5, 5)                         # random Y speed
    c1.draw(win)
 
    # draw 2nd ball at random place with random velocity and random color
    c2r = random.randrange(10, 20)
    c2 = Circle(Point(random.randrange(W//2, W-50),         # random X
                        random.randrange(H//2, H-50)),      # random Y
                       c2r)                                 # random radius
    c2color = colors[random.randrange(5)]                   # random color
    c2.setFill(c2color)
    c2.setOutline(c2color)
    dirX2 = random.randrange(-5, 5)                         # random X speed
    if dirX2 == 0:                                          # X can't be 0
         dirX2 = dirX2 + 1
    dirY2 = random.randrange(-5, 5)                         # random Y speed
    c2.draw(win)

    # define sizes for boxes
    s1 = 70
    s2 = 80
    s3 = 60

    # define random coordinates for black boxes
    p1a = random.randrange(10, W//3 - (s1 + 20))
    p1b = random.randrange(10, H//2 - (s1 + 20))
    P1 = Point(p1a, p1b)
    P2 = Point(p1a + s1, p1b + s1)
    p3a = random.randrange(W//3 + 10, (2 * W // 3) - (s2 + 20))
    p3b = random.randrange(H//3 + 10, (2 * H // 3) - (s2 + 20))
    P3 = Point(p3a, p3b)
    P4 = Point(p3a + s2, p3b + s2)
    p5a = random.randrange((2 * W // 3) + 20, W - (s3 + 20))
    p5b = random.randrange((2 * H // 3) + 20, H - (s3 + 20))
    P5 = Point(p5a, p5b)
    P6 = Point(p5a + s3, p5b + s3)

    # arranges points in rectangles
    boxes = []
    r = Rectangle( P1, P2 )
    boxes.append(r)
    r = Rectangle( P3, P4 )
    boxes.append(r)
    r = Rectangle( P5, P6 )
    boxes.append(r)

    # draws black boxes
    for i in range(len(boxes)):
         boxes[i].setFill("black")
         boxes[i].draw(win)

    # define size of white box
    ws1 = 50

    # define random coordinates for white box
    wp1a = random.randrange(10, W//3 - (ws1 + 20))
    wp1b = random.randrange(H//2 + 40, H - 40)
    WP1 = Point(wp1a, wp1b)
    WP2 = Point(wp1a + ws1, wp1b + ws1)

    # draw white box
    wr = Rectangle(WP1, WP2)
    wr.setFill("white")
    wr.setWidth(3)
    wr.draw(win)

    # moving balls and collisions
    for i in range(1000):
         
         stuck = 0
         
         # moves balls at velocities given
         c1.move(dirX1, dirY1)
         c2.move(dirX2, dirY2)

         # make c1 bounce off of walls
         if c1.getCenter().getX() < c1r + 4 or c1.getCenter().getX() > W - c1r:
              dirX1 = -dirX1
         if c1.getCenter().getY() < c1r + 4 or c1.getCenter().getY() > H - c1r:
              dirY1 = -dirY1

         # make c2 bounce off of walls
         if c2.getCenter().getX() < c2r + 4 or c2.getCenter().getX() > W - c2r:
              dirX2 = -dirX2
         if c2.getCenter().getY() < c2r + 4 or c2.getCenter().getY() > H - c2r:
              dirY2 = -dirY2

         # make balls reverse direction when they collide
         if distance(c1.getCenter(), c2.getCenter()) <= (c1r + c2r):
              dirX1 = -dirX1
              dirY1 = -dirY1
              dirX2 = -dirX2
              dirY2 = -dirY2
              
         # make ball 1 bounce off of white box
         if bounce(c1, wr, WP1, WP2, c1r) == 0:
              dirX1 = -dirX1
              dirY1 = -dirY1
              
         # make ball 2 bounce off of white box
         if bounce(c2, wr, WP1, WP2, c2r) == 0:
              dirX2 = -dirX2
              dirY2 = -dirY2

         # make ball 1 catch in black boxes
         if isInside(c1, r, P1, P2, c1r) == 0:
              dirX1 = 0
              dirY1 = 0
         if isInside(c1, r, P3, P4, c1r) == 0:
              dirX1 = 0
              dirY1 = 0
         if isInside(c1, r, P5, P6, c1r) == 0:
              dirX1 = 0
              dirY1 = 0

         # make ball 2 catch in black boxes
         if isInside(c2, r, P1, P2, c2r) == 0:
              dirX2 = 0
              dirY2 = 0
         if isInside(c2, r, P3, P4, c2r) == 0:
              dirX2 = 0
              dirY2 = 0
         if isInside(c2, r, P5, P6, c2r) == 0:
              dirX2 = 0
              dirY2 = 0

         # end program if both balls are stuck in black boxes
         if (dirX1 == 0 and dirY1 == 0) and (dirX2 == 0 and dirY2 == 0):
              t = Text(Point(W//2, H//2), "Click me to quit")
              t.setFill("white")
              t.draw(win)
              win.getMouse()
              win.close()
              stuck = 1
              break
     
    # wait for one more click and close up window
    if stuck != 1:
         t1 = Text(Point(W//2, H//2), "Click me to quit")
         t1.setFill("white")
         t1.draw(win)
         win.getMouse()
         win.close()
 
main()
