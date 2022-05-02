from turtle import *
import turtle

turtle.title("Arendain Mandala Art")
turtle.bgcolor("#ffffff")

def FlowerBG():
    div1 = turtle.Turtle()
    div1.hideturtle()
    div1.pensize(5)
    div1.speed(0)
    div1.fillcolor('#121212')
    div1.penup()
    div1.goto(0,-225)
    div1.begin_fill()
    div1.pendown()
    div1.circle(225)
    div1.end_fill()

def FlowerCenter():
    div1 = turtle.Turtle()
    div1.hideturtle()
    div1.pensize(5)
    div1.speed(0)
    div1.fillcolor('#ffffff')
    div1.begin_fill()
    div1.penup()
    div1.goto(0,-25)
    div1.pendown()
    div1.circle(25)
    div1.end_fill()

def Flower1():
    flower1 = turtle.Turtle()
    flower1.speed(0)
    flower1.hideturtle()
    flower1.pencolor('#ffffff')
    for i in range (100):
        flower1.circle(150-i,90)
        flower1.left(90)
        flower1.circle(150-i,90)
        flower1.left(18)

def Spiro1():
    spiro = turtle.Turtle()
    spiro.speed(0)
    spiro.hideturtle()
    spiro.pensize(2)
    spiro.pencolor('#121212')
    spiro.penup()
    spiro.goto(105,-200)
    spiro.pendown()
    for i in range (100):
        spiro.circle(200,180)
        spiro.right(56)

def Border1():
    div1 = turtle.Turtle()
    div1.hideturtle()
    div1.pensize(5)
    div1.speed(0)
    div1.penup()
    div1.goto(0,-308)
    div1.pendown()
    div1.circle(308)
    div1.end_fill()

def Spiro2():
    spiro2 = turtle.Turtle()
    spiro2.speed(0) 
    spiro2.hideturtle()
    spiro2.pensize(3)
    spiro2.pencolor('#121212')
    for i in range (100):
        spiro2.penup()
        spiro2.goto(0,0)
        spiro2.forward (310)
        spiro2.pendown()
        spiro2.circle(20,180)
        spiro2.right(8) 
    
    for i in range (100):
        spiro2.penup()
        spiro2.goto(0,0)
        spiro2.forward (330)
        spiro2.pendown()
        spiro2.circle(20,180)
        spiro2.right(16) 

def Border2():
    div1 = turtle.Turtle()
    div1.hideturtle()
    div1.pensize(5)
    div1.speed(0)
    div1.penup()
    div1.goto(0,-355)
    div1.pendown()
    div1.circle(355)
    div1.end_fill()

def Flower2():
    flower2 = turtle.Turtle()
    flower2.speed(0)
    flower2.hideturtle()
    flower2.pencolor('#121212')
    flower2.penup()
    flower2.goto(-202.5,280)
    flower2.pendown()
    flower2.pensize(3)
    for i in range (287):
        flower2.penup()
        flower2.forward(407)
        flower2.pendown()
        flower2.circle(50,90)
        flower2.left(91)
        flower2.circle(50,90)
        flower2.left(18)

def Border3():
    div1 = turtle.Turtle()
    div1.hideturtle()
    div1.pensize(5)
    div1.speed(0)
    div1.penup()
    div1.goto(0,-430)
    div1.pendown()
    div1.circle(425)
    div1.end_fill()

def CircleBorder():
    r = turtle.Turtle()
    r.pensize(3)
    r.speed(0)
    r.hideturtle()
    r.pencolor('#121212')
    for i in range (91):
        r.penup()
        r.goto(0,0)
        r.right(91)
        r.forward(460)
        r.pendown()
        r.circle(30)
        
def FinalBorder():
    border = turtle.Turtle()
    border.speed(0)
    border.hideturtle()
    border.pensize(3)
    border.pencolor("#121212")
    for i in range (200):
        border.penup()
        border.goto(0,0)
        border.forward(490)
        border.pendown()
        border.forward(20)
        border.left(12)
        border.circle(100,160)

FlowerBG()
FlowerCenter()
Flower1()
Spiro1()
Border1()
Spiro2()
Border2()
Flower2()
Border3()
CircleBorder()
FinalBorder()

turtle.exitonclick()