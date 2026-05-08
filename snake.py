from turtle import *

screen = Screen()
import random

def playing_area():
    pen = Turtle()
    pen.ht()
    pen.speed(0)
    pen.color('light blue')
    pen.penup()
    pen.goto(-240, 240)
    pen.pendown()
    pen.begin_fill()
    pen.goto(240, 240)
    pen.goto(240, -240)
    pen.goto(-240, -240)
    pen.goto(-240, 240)
    pen.end_fill()


class Head(Turtle):
    def __init__(self):
        super().__init__()
        self.speed(0)
        self.color("black")
        self.shape("square")
        self.penup()
        self.goto(0, 0)
        self.direction = "right"
        self.setheading(0)
        self.alive = True

    def up(self):
        if self.direction != "down":
            self.setheading(90)
            self.direction = "up"

    def down(self):
        if self.direction != "up":
            self.setheading(270)
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

        if self.xcor() > 230 or self.xcor() < -230 or self.ycor() > 230 or self.ycor() < -230:
            self.die()

    def die(self):
        self.hideturtle()
        self.alive = False


class Segment(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.hideturtle()
        self.speed(0)
        self.shape("square")
        self.color("green")
        self.penup()
        self.goto(x, y)
        self.showturtle()


class Apple(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.speed(0)
        self.penup()
        self.relocate()

    def relocate(self):
        x = random.randint(-220, 220)
        y = random.randint(-220, 220)
        self.goto(x, y)


screen.bgcolor("black")
screen.setup(520, 520)
screen.listen()

playing_area()

body = []

head = Head()
body.append(head)

body.append(Segment(head.xcor() - 20, head.ycor()))

screen.onkeypress(head.up, "Up")
screen.onkeypress(head.down, "Down")
screen.onkeypress(head.left, "Left")
screen.onkeypress(head.right, "Right")

apple = Apple()

game_started = [False]

def start_game():
    if not game_started[0]:
        game_started[0] = True
        update()

screen.onkeypress(start_game, "space")


def update():
    if not game_started[0]:
        return

    if not head.alive:
        return

    length = len(body)
    for i in range(length - 1, 0, -1):
        body[i].goto(body[i - 1].xcor(), body[i - 1].ycor())

    head.move()

    if head.distance(apple) < 20:
        apple.relocate()

        last = body[-1]
        
        new_segment = Segment(last.xcor(), last.ycor())

        body.append(new_segment)



    for i in range(1, len(body)):
        if head.distance(body[i]) < 10:
            head.die()

    screen.ontimer(update, 100)


screen.exitonclick()






