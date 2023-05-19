from turtle import Turtle


# ~~~~~~~~~~~~~ Paddle Class ~~~~~~~~~~~~~
class Paddle(Turtle):

    def __init__(self, x_location, y_location):
        super().__init__()
        self.penup()
        self.x_location = x_location
        self.y_location = y_location
        self.setpos(self.x_location, self.y_location)
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.score = 0

    def move_up(self):
        """A method that moves the paddle up."""
        if self.ycor() < 345:
            y_pos = self.ycor() + 30
            self.goto((self.xcor(), y_pos))

    def move_down(self):
        """A method that moves the paddle down."""
        if self.ycor() > -345:
            y_pos = self.ycor() - 30
            self.goto((self.xcor(), y_pos))

    def reset_position(self):
        """A method that resets the paddle's position."""
        self.setpos(self.x_location, self.y_location)


