from turtle import Screen, Turtle
import time

STARTING_POSITIONS = [(0, 0), (-10, 0), (-20, 0)]
class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]


    def create_snake(self):
        for self.position in STARTING_POSITIONS:
            self.add_segment(self.position)


    def add_segment(self, position):
        name = Turtle("circle")
        name.color("white")
        name.penup()
        name.goto(position)
        self.segments.append(name)

    def extend(self):
        self.add_segment(self.segments[-1].position())


    def move(self):
        for self.seq_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[self.seq_num - 1].xcor()
            new_y = self.segments[self.seq_num - 1].ycor()
            self.segments[self.seq_num].goto(new_x, new_y)
        self.segments[0].forward(20)



    def up(self):

        if self.segments[0].heading() != 270:
            self.segments[0].setheading(90)

    def down(self):

        if self.segments[0].heading() != 90:
            self.segments[0].setheading(270)

    def left(self):
        if self.segments[0].heading() != 0:
            self.segments[0].setheading(180)

    def right(self):
        if self.segments[0].heading() != 180:
            self.segments[0].setheading(0)




