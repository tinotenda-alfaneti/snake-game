from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-10, 0), (-20, 0)]
class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    # initialize snake
    def create_snake(self):
        for self.position in STARTING_POSITIONS:
            self.add_segment(self.position)

    # increase snake size
    def add_segment(self, position):

        name = Turtle("square")
        name.shapesize(stretch_len=0.5, stretch_wid=0.5)
        name.color("white")
        name.penup()
        name.goto(position)
        self.segments.append(name)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    # change the snake direction
    def move(self):
        for self.seq_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[self.seq_num - 1].xcor()
            new_y = self.segments[self.seq_num - 1].ycor()
            self.segments[self.seq_num].goto(new_x, new_y)
        self.segments[0].forward(10)


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





