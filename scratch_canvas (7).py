import random
import turtle

turtle.speed(0)
turtle.Screen().bgcolor('black')
def pen(colour):
    (turtle.color(colour))

pen('red')
def firework1(size):
    for num in range(20):
        turtle.forward(size)
        turtle.right(180 - 360 / 20)

firework1(45)
def move():
    turtle.penup()
    x = random.randint(-150, 150)
    y = random.randint(-150, 150)
    turtle.goto(x, y)
    turtle.pendown()

move()
pen('yellow')
firework1(78)
move()
pen('blue')
firework1(45)
move()
pen('purple')
firework1(120)
move()
pen('lightblue')
firework1(120)
move()
pen('pink')
firework1(101)
move()
pen('orange')
firework1(54)
move()
pen('violet')
firework1(33)
move()
pen('green')
firework1(29)