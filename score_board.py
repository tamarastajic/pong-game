from turtle import Turtle


# ~~~~~~~~~~~~~ Scoreboard Class ~~~~~~~~~~~~~
class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.pencolor("white")

    def draw_divider(self, screen):
        """A method that draws the divider in the middle of the screen."""
        start_y = 380
        for i in range(17):
            self.penup()
            self.goto(0, start_y)
            self.pendown()
            self.goto(0, start_y-50)
            self.penup()
            start_y -= 100

    def write_score(self, l_score, r_score, screen):
        """A method that writes the score."""
        self.clear()
        self.draw_divider(screen)
        self.goto(-100, 300)
        self.write(l_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 300)
        self.write(r_score, align="center", font=("Courier", 80, "normal"))
        screen.update()
