import turtle

t = turtle.Turtle()
t.penup()
t.color("cyan")
t.pendown()

for i in range(6):
    t.forward(100)
    t.left(60)

turtle.exitonclick()