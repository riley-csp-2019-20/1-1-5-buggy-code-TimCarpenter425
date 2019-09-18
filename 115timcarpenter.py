#  a115_ladybug.py
import turtle as trtl

# create ladybug head
ladybug = trtl.Turtle()
ladybug.hideturtle()
ladybug.speed(0)
ladybug.pensize(40)
ladybug.circle(5)

# legs setup
ladybug.penup()
legs = 3
length = 55
angle = 135 / legs
ladybug.pensize(4)
lleg = 0
rleg = 0
#draw legs
while (lleg < legs):
  ladybug.goto(0,-35)
  ladybug.pendown()
  ladybug.setheading(angle*lleg-45)
  ladybug.forward(length)
  lleg = lleg + 1
while (rleg < legs):
  ladybug.goto(0,-35)
  ladybug.setheading(angle*rleg+135)
  ladybug.forward(length)
  rleg = rleg + 1

# create ladybug head again for positioning because I don't feel like going through and fixing all of that when I could just do this
ladybug = trtl.Turtle()
ladybug.hideturtle()
ladybug.speed(0)
ladybug.pensize(40)
ladybug.circle(5)

# and body
ladybug.penup()
ladybug.goto(0, -55) 
ladybug.color("red")
ladybug.pendown()
ladybug.pensize(40)
ladybug.circle(20)
ladybug.setheading(270)
ladybug.color("black")
ladybug.penup()
ladybug.goto(0, 5)
ladybug.pensize(2)
ladybug.pendown()
ladybug.forward(79)

# config dots
num_dots = 1
xpos = -20
ypos = -55
ladybug.pensize(10)

# draw two sets of dots
while (num_dots <= 2 ):
  ladybug.penup()
  ladybug.goto(xpos, ypos)
  ladybug.pendown()
  ladybug.circle(3)
  ladybug.penup()
  ladybug.goto(xpos + 30, ypos + 20)
  ladybug.pendown()
  ladybug.circle(2)
  num_dots = num_dots + 1

  # position next dots
  xpos = ypos + 40
  ypos = xpos - 15
  num_dot = num_dots + 1




wn = trtl.Screen()
wn.mainloop()