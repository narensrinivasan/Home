import time
import turtle

screen = turtle.Screen()
screen.title("Clair D'Ombre Demo")
screen.bgcolor("Gray")

room = turtle.Turtle()


room.shape("square")
room.color("Blue")

room.setx(0-(screen.canvwidth/2))
room.sety(0)


screen.mainloop()
