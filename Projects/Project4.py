# ###############################################
# ### SETUP ###
import turtle
# ###############################################

# Section 1 - Helper functions (DON'T CHANGE!!)
import turtle, math, time, random
turtle.Screen().bgcolor("black")
def set_background(image_filename):
    screen = turtle.Screen()
    try:
        screen.bgpic(f"/workspaces/Computational-Thinking-8/Backgrounds/{image_filename}.png")
    except:
        screen.bgpic(f"/workspaces/Computational-Thinking-8/Backgrounds/{image_filename}.gif")


#I added the 6-7 because the 6-7 arts are getting the most votes.
#I changed the coordinates of the 6-7 due to the feedback.
#I got rid of the 6-7 due to feedback.



t = turtle.Turtle()
t1 = turtle.Turtle()
t2 = turtle.Turtle()
t3 = turtle.Turtle()
t.penup()
t1.penup()
t2.penup()
t3.penup()
t.goto(-30,-30)
t1.goto(-35,-35)
t2.goto(-40,-40)
t3.goto(-45,-45)
t.color("blue")
t1.color("DeepSkyBlue")
t2.color("fuchsia")
t3.color("lime")
t.pendown()
t1.pendown()
t2.pendown()
t3.pendown()
t.speed(1000000)
t1.speed(1000000)
t2.speed(1000000)
t3.speed(1000000)
#changed the speed to 1000000 due to feedback
for i in range(100000):
    t.forward(.67 + i * 0.5)
    t1.forward(.67 + i * 0.5)
    t2.forward(.67 + i * 0.5)
    t3.forward(.67 + i * 0.5)
    t.left(67.676767)
    t1.left(67.676767)
    t2.left(67.676767)
    t3.left(67.676767)






# ###############################################
# ### ENDING ###
turtle.exitonclick()
# ###############################################
