from turtle import Turtle
class Paddle(Turtle):
    def __init__(self, coordinate):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.setpos(coordinate)

    def paddle_up(self):
        y_coordinate = self.ycor() + 20
        x_coordinate = self.xcor()
        self.goto(y=y_coordinate, x=x_coordinate)

    def paddle_down(self):
        y_coordinate = self.ycor() - 20
        x_coordinate = self.xcor()
        self.goto(y=y_coordinate, x=x_coordinate)

