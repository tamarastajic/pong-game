from turtle import Turtle


# ~~~~~~~~~~~~~ Ball Class ~~~~~~~~~~~~~
class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self. shape("circle")
        self.color("white")
        self.goto(0, 0)
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.07

    def move(self, screen):
        """A method that moves the ball."""
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
        screen.update()

    def bounce_y(self):
        """A method that bounces the ball vertically."""
        self.y_move *= -1

    def bounce_x(self):
        """A method that bounces the ball horizontally and speeds it up."""
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        """A method that resets the balls position."""
        self.goto(0, 0)
        self.move_speed = 0.07
        self.bounce_x()

