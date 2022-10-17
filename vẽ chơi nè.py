"""
import turtle
t = turtle.Pen()
turtle.bgcolor("black")
colors = ["red", "yellow", "blue", "green"]
for x in range(200):
    t.pencolor(colors[x%4])
    t.forward(x)
    t.left(91)
####
import turtle as t
import time as ti
def rectangle(hor,ver,col):
    t.pendown() #tạo con trỏ
    t.pensize(1) #kích cỡ
    t.color(col)
    t.begin_fill()
    for counter in range(1,3): #đây là một vòng lặp (loop)
        t.forward(hor)
        t.right(90)
        t.forward(ver)
        t.right(90)
    t.end_fill()
    t.penup()
t.penup()
t.speed('slow') #Tốc độ vẽ của con trỏ
t.bgcolor('Dodger blue')
ti.sleep(10)
t.hideturtle()

#Vẽ bàn chân

t.goto(-100,-150)
rectangle(50,20,'blue')
t.goto(-30,-150)
rectangle(50,20,'blue')

#Vẽ chân

t.goto(-25,-50)
rectangle(15,100,'grey')
t.goto(-55,-50)
rectangle(-15,100,'grey')

#Vẽ thân

t.goto(-90,100)
rectangle(100,150,'red')

#Vẽ tay

t.goto(-150,70)
rectangle(60,15,'grey')
t.goto(-150,110)
rectangle(15,40,'grey')
t.goto(10,70)
rectangle(60,15,'grey')
t.goto(55,110)
rectangle(15,40,'grey')

#Vẽ cổ

t.goto(-50,120)
rectangle(15,20,'grey')

#Vẽ đầu

t.goto(-85,170)
rectangle(80,50,'red')
t.goto(-60,160)

#Vẽ mắt miệng:
rectangle(30,10,'white')
t.goto(-60,160)
rectangle(5,5,'black')
t.goto(-45,155)
rectangle(5,5,'black')
t.goto(-65,135)
t.right(5)
rectangle(40,5,'black')

#Vẽ bàn tay:

t.goto(-155,130)
rectangle(25,25,'green')
t.goto(-147,130)
rectangle(10,15,t.bgcolor())
t.goto(50,130)
rectangle(25,25,'green')
t.goto(58,130)
rectangle(10,15,t.bgcolor())


import turtle as t
import time as ti

def rectangle(hor,ver,col):
    t.pendown() #tạo con trỏ
    t.pensize(1)
    t.color(col)
    t.begin_fill()
    for counter in range(1,3):
        t.forward(hor)
        t.right(90)
        t.forward(ver)
        t.right(90)
    t.end_fill()
    t.penup()
t.penup()
t.speed('slow')
t.bgcolor('Dodger blue')

t.goto(-100,-150)
rectangle(50,20,'blue')
t.goto(-30,-150)
rectangle(50,20,'blue')

t.goto(-25,-50)
rectangle(15,100,'grey')
t.goto(-55,-50)
rectangle(-15,100,'grey')

t.goto(-90,100)
rectangle(100,150,'red')

t.goto(-150,70)
rectangle(60,15,'grey')
t.goto(-150,110)
rectangle(15,40,'grey')
t.goto(10,70)
rectangle(60,15,'grey')
t.goto(55,110)
rectangle(15,40,'grey')

t.goto(-50,120)
rectangle(15,20,'grey')
t.goto(-85,170)
rectangle(80,50,'red')
t.goto(-60,160)
rectangle(30,10,'white')
t.goto(-60,160)
rectangle(5,5,'black')
t.goto(-45,155)
rectangle(5,5,'black')
t.goto(-65,135)
t.right(5)
rectangle(40,5,'black')
t.goto(-155,130)
rectangle(25,25,'green')
t.goto(-147,130)
rectangle(10,15,t.bgcolor())
t.goto(50,130)
rectangle(25,25,'green')
t.goto(58,130)
rectangle(10,15,t.bgcolor())
t.hideturtle()
ti.sleep(10)
t.hideturtle()
###
from turtle import *
import turtle
wn = turtle.Screen()
wn.setup(width=1000, height=800)

def my_goto(x, y):
    penup()
    goto(x, y)
    pendown()


def eyes():
    fillcolor("#ffffff")
    begin_fill()

    tracer(False)
    a = 2.5
    for i in range(120):
        if 0 <= i < 30 or 60 <= i < 90:
            a -= 0.05
            lt(3)
            fd(a)
        else:
            a += 0.05
            lt(3)
            fd(a)
    tracer(True)
    end_fill()



def beard():
    my_goto(-32, 135)
    seth(165)
    fd(60)

    my_goto(-32, 125)
    seth(180)
    fd(60)

    my_goto(-32, 115)
    seth(193)
    fd(60)

    my_goto(37, 135)
    seth(15)
    fd(60)

    my_goto(37, 125)
    seth(0)
    fd(60)

    my_goto(37, 115)
    seth(-13)
    fd(60)


def mouth():
    my_goto(5, 148)
    seth(270)
    fd(100)
    seth(0)
    circle(120, 50)
    seth(230)
    circle(-120, 100)


def scarf():
    fillcolor('#e70010')
    begin_fill()
    seth(0)
    fd(200)
    circle(-5, 90)
    fd(10)
    circle(-5, 90)
    fd(207)
    circle(-5, 90)
    fd(10)
    circle(-5, 90)
    end_fill()


def nose():
    my_goto(-10, 158)
    seth(315)
    fillcolor('#e70010')
    begin_fill()
    circle(20)
    end_fill()


def black_eyes():
    seth(0)
    my_goto(-20, 195)
    fillcolor('#000000')
    begin_fill()
    circle(13)
    end_fill()

    pensize(6)
    my_goto(20, 205)
    seth(75)
    circle(-10, 150)
    pensize(3)

    my_goto(-17, 200)
    seth(0)
    fillcolor('#ffffff')
    begin_fill()
    circle(5)
    end_fill()
    my_goto(0, 0)




def face():

    fd(183)
    lt(45)
    fillcolor('#ffffff')
    begin_fill()
    circle(120, 100)
    seth(180)
    # print(pos())
    fd(121)
    pendown()
    seth(215)
    circle(120, 100)
    end_fill()
    my_goto(63.56,218.24)
    seth(90)
    eyes()
    seth(180)
    penup()
    fd(60)
    pendown()
    seth(90)
    eyes()
    penup()
    seth(180)
    fd(64)


def head():
    penup()
    circle(150, 40)
    pendown()
    fillcolor('#00a0de')
    begin_fill()
    circle(150, 280)
    end_fill()


def Doraemon():
    head()
    scarf()
    face()
    black_eyes()
    nose()
    mouth()
    beard()
    my_goto(0, 0)
    seth(0)
    penup()
    circle(150, 50)
    pendown()
    seth(30)
    fd(40)
    seth(70)
    circle(-30, 270)


    fillcolor('#00a0de')
    begin_fill()

    seth(230)
    fd(80)
    seth(90)
    circle(1000, 1)
    seth(-89)
    circle(-1000, 10)

    # print(pos())

    seth(180)
    fd(70)
    seth(90)
    circle(30, 180)
    seth(180)
    fd(70)

    # print(pos())
    seth(100)
    circle(-1000, 9)

    seth(-86)
    circle(1000, 2)
    seth(230)
    fd(40)

    # print(pos())


    circle(-30, 230)
    seth(45)
    fd(81)
    seth(0)
    fd(203)
    circle(5, 90)
    fd(10)
    circle(5, 90)
    fd(7)
    seth(40)
    circle(150, 10)
    seth(30)
    fd(40)
    end_fill()

    seth(70)
    fillcolor('#ffffff')
    begin_fill()
    circle(-30)
    end_fill()

    my_goto(103.74, -182.59)
    seth(0)
    fillcolor('#ffffff')
    begin_fill()
    fd(15)
    circle(-15, 180)
    fd(90)
    circle(-15, 180)
    fd(10)
    end_fill()

    my_goto(-96.26, -182.59)
    seth(180)
    fillcolor('#ffffff')
    begin_fill()
    fd(15)
    circle(15, 180)
    fd(90)
    circle(15, 180)
    fd(10)
    end_fill()

    my_goto(-133.97, -91.81)
    seth(50)
    fillcolor('#ffffff')
    begin_fill()
    circle(30)
    end_fill()

    my_goto(-103.42, 15.09)
    seth(0)
    fd(38)
    seth(230)
    begin_fill()
    circle(90, 260)
    end_fill()

    my_goto(5, -40)
    seth(0)
    fd(70)
    seth(-90)
    circle(-70, 180)
    seth(0)
    fd(70)

    my_goto(-103.42, 15.09)
    fd(90)
    seth(70)
    fillcolor('#ffd200')
    # print(pos())
    begin_fill()
    circle(-20)
    end_fill()
    seth(170)
    fillcolor('#ffd200')
    begin_fill()
    circle(-2, 180)
    seth(10)
    circle(-100, 22)
    circle(-2, 180)
    seth(180-10)
    circle(100, 22)
    end_fill()
    goto(-13.42, 15.09)
    seth(250)
    circle(20, 110)
    seth(90)
    fd(15)
    dot(10)
    my_goto(0, -150)



if __name__ == '__main__':
    pensize(3)
    speed(9)
    Doraemon()
    my_goto(100, -300)
    write('@python.for.fun', font=("Bradley Hand ITC", 30, "bold"))
    mainloop()
###
import turtle

def getPosition(x, y):
    turtle.setx(x)
    turtle.sety(y)
    print(x, y)

class Pikachu:

    def __init__(self):
        self.t = turtle.Turtle()
        t = self.t
        t.pensize(3)
        t.speed(9)
        t.ondrag(getPosition)

    def noTrace_goto(self, x, y):
        self.t.penup()
        self.t.goto(x, y)
        self.t.pendown()

    def leftEye(self, x, y):
        self.noTrace_goto(x, y)
        t = self.t
        t.seth(0)
        t.fillcolor('#333333')
        t.begin_fill()
        t.circle(22)
        t.end_fill()

        self.noTrace_goto(x, y + 10)
        t.fillcolor('#000000')
        t.begin_fill()
        t.circle(10)
        t.end_fill()

        self.noTrace_goto(x + 6, y + 22)
        t.fillcolor('#ffffff')
        t.begin_fill()
        t.circle(10)
        t.end_fill()

    def rightEye(self, x, y):
        self.noTrace_goto(x, y)
        t = self.t
        t.seth(0)
        t.fillcolor('#333333')
        t.begin_fill()
        t.circle(22)
        t.end_fill()

        self.noTrace_goto(x, y + 10)
        t.fillcolor('#000000')
        t.begin_fill()
        t.circle(10)
        t.end_fill()

        self.noTrace_goto(x - 6, y + 22)
        t.fillcolor('#ffffff')
        t.begin_fill()
        t.circle(10)
        t.end_fill()

    def mouth(self, x, y):
        self.noTrace_goto(x, y)
        t = self.t

        t.fillcolor('#88141D')
        t.begin_fill()

        # Lower Lip
        l1 = []
        l2 = []
        t.seth(190)
        a = 0.7
        for i in range(28):
            a += 0.1
            t.right(3)
            t.fd(a)
            l1.append(t.position())

        self.noTrace_goto(x, y)

        t.seth(10)
        a = 0.7
        for i in range(28):
            a += 0.1
            t.left(3)
            t.fd(a)
            l2.append(t.position())

        # Upper Lip
        t.seth(10)
        t.circle(50, 15)
        t.left(180)
        t.circle(-50, 15)

        t.circle(-50, 40)
        t.seth(233)
        t.circle(-50, 55)
        t.left(180)
        t.circle(50, 12.1)
        t.end_fill()

        # Tongue
        self.noTrace_goto(17, 54)
        t.fillcolor('#DD716F')
        t.begin_fill()
        t.seth(145)
        t.circle(40, 86)
        t.penup()
        for pos in reversed(l1[:20]):
            t.goto(pos[0], pos[1] + 1.5)
        for pos in l2[:20]:
            t.goto(pos[0], pos[1] + 1.5)
        t.pendown()
        t.end_fill()

        # Nose
        self.noTrace_goto(-17, 94)
        t.seth(8)
        t.fd(4)
        t.back(8)

    # Red Cheeks
    def leftCheek(self, x, y):
        turtle.tracer(False)
        t = self.t
        self.noTrace_goto(x, y)
        t.seth(300)
        t.fillcolor('#DD4D28')
        t.begin_fill()
        a = 2.3
        for i in range(120):
            if 0 <= i < 30 or 60 <= i < 90:
                a -= 0.05
                t.lt(3)
                t.fd(a)
            else:
                a += 0.05
                t.lt(3)
                t.fd(a)
        t.end_fill()
        turtle.tracer(True)

    def rightCheek(self, x, y):
        t = self.t
        turtle.tracer(False)
        self.noTrace_goto(x, y)
        t.seth(60)
        t.fillcolor('#DD4D28')
        t.begin_fill()
        a = 2.3
        for i in range(120):
            if 0 <= i < 30 or 60 <= i < 90:
                a -= 0.05
                t.lt(3)
                t.fd(a)
            else:
                a += 0.05
                t.lt(3)
                t.fd(a)
        t.end_fill()
        turtle.tracer(True)

    def colorLeftEar(self, x, y):
        t = self.t
        self.noTrace_goto(x, y)
        t.fillcolor('#000000')
        t.begin_fill()
        t.seth(330)
        t.circle(100, 35)
        t.seth(219)
        t.circle(-300, 19)
        t.seth(110)
        t.circle(-30, 50)
        t.circle(-300, 10)
        t.end_fill()

    def colorRightEar(self, x, y):
        t = self.t
        self.noTrace_goto(x, y)
        t.fillcolor('#000000')
        t.begin_fill()
        t.seth(300)
        t.circle(-100, 30)
        t.seth(35)
        t.circle(300, 15)
        t.circle(30, 50)
        t.seth(190)
        t.circle(300, 17)
        t.end_fill()

    def body(self):
        t = self.t

        t.fillcolor('#F6D02F')
        t.begin_fill()
        # Right face contour
        t.penup()
        t.circle(130, 40)
        t.pendown()
        t.circle(100, 105)
        t.left(180)
        t.circle(-100, 5)

        # Right ear
        t.seth(20)
        t.circle(300, 30)
        t.circle(30, 50)
        t.seth(190)
        t.circle(300, 36)

        # Upper profile
        t.seth(150)
        t.circle(150, 70)

        # Left ear
        t.seth(200)
        t.circle(300, 40)
        t.circle(30, 50)
        t.seth(20)
        t.circle(300, 35)
        #print(t.pos())

        # Left face contour
        t.seth(240)
        t.circle(105, 95)
        t.left(180)
        t.circle(-105, 5)

        # Left hand
        t.seth(210)
        t.circle(500, 18)
        t.seth(200)
        t.fd(10)
        t.seth(280)
        t.fd(7)
        t.seth(210)
        t.fd(10)
        t.seth(300)
        t.circle(10, 80)
        t.seth(220)
        t.fd(10)
        t.seth(300)
        t.circle(10, 80)
        t.seth(240)
        t.fd(12)
        t.seth(0)
        t.fd(13)
        t.seth(240)
        t.circle(10, 70)
        t.seth(10)
        t.circle(10, 70)
        t.seth(10)
        t.circle(300, 18)

        t.seth(75)
        t.circle(500, 8)
        t.left(180)
        t.circle(-500, 15)
        t.seth(250)
        t.circle(100, 65)

        # Left foot
        t.seth(320)
        t.circle(100, 5)
        t.left(180)
        t.circle(-100, 5)
        t.seth(220)
        t.circle(200, 20)
        t.circle(20, 70)

        t.seth(60)
        t.circle(-100, 20)
        t.left(180)
        t.circle(100, 20)
        t.seth(300)
        t.circle(10, 70)

        t.seth(60)
        t.circle(-100, 20)
        t.left(180)
        t.circle(100, 20)
        t.seth(10)
        t.circle(100, 60)

        # Horizontal
        t.seth(180)
        t.circle(-100, 10)
        t.left(180)
        t.circle(100, 10)
        t.seth(5)
        t.circle(100, 10)
        t.circle(-100, 40)
        t.circle(100, 35)
        t.left(180)
        t.circle(-100, 10)

        # Right foot
        t.seth(290)
        t.circle(100, 55)
        t.circle(10, 50)

        t.seth(120)
        t.circle(100, 20)
        t.left(180)
        t.circle(-100, 20)

        t.seth(0)
        t.circle(10, 50)

        t.seth(110)
        t.circle(100, 20)
        t.left(180)
        t.circle(-100, 20)

        t.seth(30)
        t.circle(20, 50)

        t.seth(100)
        t.circle(100, 40)

        # Right body contour
        t.seth(200)
        t.circle(-100, 5)
        t.left(180)
        t.circle(100, 5)
        t.left(30)
        t.circle(100, 75)
        t.right(15)
        t.circle(-300, 21)
        t.left(180)
        t.circle(300, 3)

        # Right hand
        t.seth(43)
        t.circle(200, 60)

        t.right(10)
        t.fd(10)

        t.circle(5, 160)
        t.seth(90)
        t.circle(5, 160)
        t.seth(90)

        t.fd(10)
        t.seth(90)
        t.circle(5, 180)
        t.fd(10)

        t.left(180)
        t.left(20)
        t.fd(10)
        t.circle(5, 170)
        t.fd(10)
        t.seth(240)
        t.circle(50, 30)

        t.end_fill()
        self.noTrace_goto(130, 125)
        t.seth(-20)
        t.fd(5)
        t.circle(-5, 160)
        t.fd(5)

        # Fingers
        self.noTrace_goto(166, 130)
        t.seth(-90)
        t.fd(3)
        t.circle(-4, 180)
        t.fd(3)
        t.seth(-90)
        t.fd(3)
        t.circle(-4, 180)
        t.fd(3)

        # Tail
        self.noTrace_goto(168, 134)
        t.fillcolor('#F6D02F')
        t.begin_fill()
        t.seth(40)
        t.fd(200)
        t.seth(-80)
        t.fd(150)
        t.seth(210)
        t.fd(150)
        t.left(90)
        t.fd(100)
        t.right(95)
        t.fd(100)
        t.left(110)
        t.fd(70)
        t.right(110)
        t.fd(80)
        t.left(110)
        t.fd(30)
        t.right(110)
        t.fd(32)

        t.right(106)
        t.circle(100, 25)
        t.right(15)
        t.circle(-300, 2)
        #print(t.pos())
        t.seth(30)
        t.fd(40)
        t.left(100)
        t.fd(70)
        t.right(100)
        t.fd(80)
        t.left(100)
        t.fd(46)
        t.seth(66)
        t.circle(200, 38)
        t.right(10)
        t.fd(10)
        t.end_fill()

        # Tail Pattern
        t.fillcolor('#923E24')
        self.noTrace_goto(126.82, -156.84)
        t.begin_fill()

        t.seth(30)
        t.fd(40)
        t.left(100)
        t.fd(40)
        t.pencolor('#923e24')
        t.seth(-30)
        t.fd(30)
        t.left(140)
        t.fd(20)
        t.right(150)
        t.fd(20)
        t.left(150)
        t.fd(20)
        t.right(150)
        t.fd(20)
        t.left(130)
        t.fd(18)
        t.pencolor('#000000')
        t.seth(-45)
        t.fd(67)
        t.right(110)
        t.fd(80)
        t.left(110)
        t.fd(30)
        t.right(110)
        t.fd(32)
        t.right(106)
        t.circle(100, 25)
        t.right(15)
        t.circle(-300, 2)
        t.end_fill()

        # Hat, Eye, Mouth, Cheek
        self.cap(-134.07, 147.81)
        self.mouth(-5, 25)
        self.leftCheek(-126, 32)
        self.rightCheek(107, 63)
        self.colorLeftEar(-250, 100)
        self.colorRightEar(140, 270)
        self.leftEye(-85, 90)
        self.rightEye(50, 110)
        t.hideturtle()

    def cap(self, x, y):
        self.noTrace_goto(x, y)
        t = self.t
        t.fillcolor('#CD0000')
        t.begin_fill()
        t.seth(200)
        t.circle(400, 7)
        t.left(180)
        t.circle(-400, 30)
        t.circle(30, 60)
        t.fd(50)
        t.circle(30, 45)
        t.fd(60)
        t.left(5)
        t.circle(30, 70)
        t.right(20)
        t.circle(200, 70)
        t.circle(30, 60)
        t.fd(70)
        #print(t.pos())
        t.right(35)
        t.fd(50)
        t.circle(8, 100)
        t.end_fill()
        self.noTrace_goto(-168.47, 185.52)
        t.seth(36)
        t.circle(-270, 54)
        t.left(180)
        t.circle(270, 27)
        t.circle(-80, 98)

        t.fillcolor('#444444')
        t.begin_fill()
        t.left(180)
        t.circle(80, 197)
        t.left(58)
        t.circle(200, 45)
        t.end_fill()

        self.noTrace_goto(-58, 270)
        t.pencolor('#228B22')
        t.dot(35)

        self.noTrace_goto(-30, 280)
        t.fillcolor('#228B22')
        t.begin_fill()
        t.seth(100)
        t.circle(30, 180)
        t.seth(190)
        t.fd(15)
        t.seth(100)
        t.circle(-45, 180)
        t.right(90)
        t.fd(15)
        t.end_fill()
        t.pencolor('#000000')

    def start(self):
        self.body()


def main():
    print('Painting the Pikachu... ')
    wn = turtle.Screen()
    wn.setup(width=600, height=800)
    pikachu = Pikachu()
    pikachu.start()
    turtle.mainloop()


if __name__ == '__main__':
    main()
###
import pygame
pygame.init()
screen = pygame.display.set_mode((500, 500))
done = False
x=60
y=60
while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        pygame.draw.rect(screen, (0,128,255), pygame.Rect(x, y, 90, 90))        
        pygame.display.flip()
"""
"""
import pygame        # Setup
pygame.init()
screen = pygame.display.set_mode([800,600]) # màn hình để vẽ 800 x 600
keep_going = True # Boolean
pic = pygame.image.load("C:\Users\ASUS\Downloads\UnripeBoilingEeve-size_restricted") # Ảnh ta load vào biến pic cho gọn cái tên CrazySmile.bmp dài quá
picx = 0
picy = 0
BLACK = (0,0,0)
timer = pygame.time.Clock()
speedx = 5  # vận tốc di chuyển hoành độ
speedy = 5  # vận tốc di chuyển tung độ
while keep_going:    # Game loop
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: # khi event là nhấn nút X đỏ ở góc hình thì cho:
            keep_going = False
    picx += speedx
    picy += speedy
    
    if picx <= 0 or picx + pic.get_width() >= 800:
        speedx = -speedx # cho hình dội lại
    if picy <= 0 or picy + pic.get_height() >= 600:
        speedy = -speedy # cho hình dội lại
    #screen.fill(BLACK)    
    screen.blit(pic, (picx, picy))
    pygame.display.update()
    timer.tick(60)
    
pygame.quit()
"""
