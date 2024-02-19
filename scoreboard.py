from turtle import  Turtle
class Scoreboard(Turtle):
    def __init__(self, which_paddle):
        super().__init__()
        self.color("White")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        if which_paddle == "left":
            self.goto(-100, 200)
            self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
        elif which_paddle == "right":
            self.goto(+100, 200)
            self.write(self.r_score, align="center", font=("Courier", 80, "normal"))

    def update_board(self, which_paddle):
        if which_paddle == "left":
            self.clear()
            self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
        elif which_paddle == "right":
            self.clear()
            self.write(self.r_score, align="center", font=("Courier", 80, "normal"))


