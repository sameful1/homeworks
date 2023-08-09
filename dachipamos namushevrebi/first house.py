from turtle import *

#we want to paint a house

#step 1: draw a square
speed(10)
width(7)
color("purple")

forward(200) 
left(90)

forward(200)
left(90)

forward(200) 
left(90)

forward(200)
left(90)
#end of square

#drawing a door

forward (70)
color("yellow")
begin_fill()
left(90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)
end_fill()

penup()
goto(200, 200)
pendown()

color("Red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

#drawing windows
penup()
goto(0, 140)
pendown()
left(210)
right(90)
width("5")
color("white")
forward(70)
color("cyan")
forward(60)
left(90)
forward(40)
left(90)
forward(60)
left(90)
forward(40)
left(90)
forward(30)
left(90)
forward(40)
left(180)
forward(20)
right(90)
forward(30)
left(180)
forward(60)

penup()
goto(0, 180)
pendown()
left(270)
color("purple")
width("7")
forward(60)
penup()
goto(0, 0)
pendown()
left(90)
forward(200)
width("5")
right(90)
color("lightgreen")
forward(5)
right(90)
forward(2000)
right(180)
forward(4000)
penup()
goto(0, 0)
pendown()
color("purple")
forward(200)















exitonclick()
