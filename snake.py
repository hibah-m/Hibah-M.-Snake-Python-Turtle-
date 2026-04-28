from turtle import *
import random

def generate_color():
    return f"#{random.randint(0, 0xFFFFFF):06x}"

def playing_area():
    pen = Turtle()
    pen.ht()
    pen.speed(0)
    pen.color('light blue')
    pen.penup()
    pen.goto(-240,240)
    pen.pendown()    
    pen.begin_fill()
    pen.goto(240,240)
    pen.goto(240,-240)
    pen.goto(-240,-240)
    pen.goto(-240,240)
    pen.end_fill()
    
class Head(Turtle):
  def __init__(self, screen, body):
    super().__init__()
    self.ht()
    self.speed(0)
    self.color("green")
    self.shape("square")
    self.penup()
    self.goto(0,0)
    self.direction = "stop"
    self.screen = screen
    self.body = body
    self.alive = True

    self.screen.onkey(self.up, "Up")
    self.screen.onkey(self.down, "Down")
    self.screen.onkey(self.left, "Left")
    self.screen.onkey(self.right, "Right")

  def up(self):
    if self.direction != "down":
      self.setheading(90)
      self.direction = "up"
    
  def down(self):
    if self.direction != "up":
      self.setheading(180)
      self.direction = "down"

  def left(self):
    if self.direction != "right":
      self.setheading(180)
      self.direction = "left"

  def right(self):
    if self.direction != "left":
      self.setheading(0)
      self.direction = "right"

  def move(self):
    if not self.alive:
      return

    self.forward(20)

    if self.xcor() > 240 or self.xcor() < -240 or self.ycor > 240 or self.ycor <-240:
      self.die()

    
  def die(self):
    self.hideturtle()
    self.alive = False


class Segment(Turtle):
  def __init__(self, other):
    super().__init__()
    pass

  def move(self, other):
    pass

class Apple(Turtle):
  def __init__(self):
    super().__init__()
    self.shape("circle")
    self.color("red")
    self.penup()
    self.relocate

  def relocate(self):
    x = random.randint(-230,230)
    y = random.randint(-230,230)
    self.goto(x,y)

screen = Screen()
screen.bgcolor("black")
screen.setup(520,520)
# Key Binding. Connects key presses and mouse clicks with function calls
screen.listen()

body = []
playing_area()

screen.exitonclick()






screen.exitonclick()
