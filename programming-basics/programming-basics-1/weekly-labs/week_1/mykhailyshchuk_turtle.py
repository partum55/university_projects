from turtle import *
from random import *

#start
speed(0)
penup()
bgcolor("lightcyan")

#grass_ground
goto(-480, -300)
pendown()
color("green", "green")
begin_fill()
forward(1000)
right(90)
forward(100)
right(90)
forward(1000)
right(90)
forward(100)
right(90)
end_fill()
penup()

#grass
pendown()
color("darkgreen")
for i in range (50):
    forward(20)
    left(90)
    a = randint(10, 20)
    forward(a)
    right(180)
    forward(a)
    left(90)
    a = 0
penup()

#sun
goto(430, 250)
pendown()
color("yellow")
begin_fill()
circle(200)
end_fill()
for i in range (45):
    a = randint(50, 100)
    right(90)
    forward(a)
    right(180)
    forward(a)
    right(90)
    for j in range (8):
        forward(3.44)
        left(1)
    a = 0
penup()

#house

#walls
home()
goto(-300, -300)
pendown()
color("lightsalmon")
begin_fill()
for i in range (2):
    forward(300)
    left(90)
    forward(200)
    left(90)
end_fill()

#door
goto(-250, -300)
color("tan4")
begin_fill()
for i in range (2):
    forward(80)
    left(90)
    forward(150)
    left(90)
end_fill()
penup()

#door_handle
goto(-191, -260)
pendown()
color("gray0")
begin_fill()
circle(10)
end_fill()
penup()

#window
goto(-130, -200)
pendown()
color("black", "white")
begin_fill()
for i in range (4):
    forward(50)
    left(90)
end_fill()
right(90)
forward(50)
left(90)
begin_fill()
for i in range (4):
    forward(50)
    left(90)
end_fill()
forward(50)
begin_fill()
for i in range (4):
    forward(50)
    left(90)
end_fill()
left(90)
forward(50)
right(90)
begin_fill()
for i in range (4):
    forward(50)
    left(90)
end_fill()
penup()

#roof
goto(-330, -100)
pendown()
color("indianred1")
begin_fill()
forward(362)
left(135)
forward(255)
left(90)
forward(255)
end_fill()
penup()

#cloud
home()
goto(-400, 350)
color("white")
begin_fill()
circle(randint(60, 120))
goto(-350+i, 350)
circle(randint(60, 120))
end_fill()

done()