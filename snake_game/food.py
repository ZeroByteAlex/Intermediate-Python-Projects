import turtle
import random

class Food(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(20, 280)
        random_y = random.randint(20, 280)
        self.goto(random_x, random_y)
