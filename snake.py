import turtle

SNAKE_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]
        self.move()
        self.up()
        self.down()
        self.right()
        self.left()

    def create_snake(self):
        for square in SNAKE_POSITIONS:  # This for loop creates the three squares
            self.add_segment(square)
            ###################### OLD CODE ######################
        #     snake = turtle.Turtle("square")  # snake_body = [snake[0], snake[1], snake[2]]
        #     self.snake_body.append(snake)
        #     self.snake_body[square].penup()
        #     self.snake_body[square].color("white")
        # for position in range(3):  # This for loop arranges the squares to form a snake
        #     self.snake_body[position].goto(SNAKE_POSITIONS[position])
            ###################### OLD CODE ######################

    def add_segment(self, position):
        snake = turtle.Turtle("square")
        snake.color("white")
        snake.penup()
        snake.goto(position)
        self.snake_body.append(snake)

    def extend(self):
        self.add_segment(self.snake_body[-1].position())

    def move(self):
        for seg_num in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[seg_num - 1].xcor()
            new_y = self.snake_body[seg_num - 1].ycor()
            self.snake_body[seg_num].goto(new_x, new_y)
        self.snake_body[0].forward(MOVE_DISTANCE) # This code will make the entire snake_body go forward.

    def up(self):
        if self.snake_body[0].heading() != DOWN:
            self.snake_body[0].setheading(UP)

    def down(self):
        if self.snake_body[0].heading() != UP:
            self.snake_body[0].setheading(DOWN)

    def left(self):
        if self.snake_body[0].heading() != RIGHT:
            self.snake_body[0].setheading(LEFT)

    def right(self):
        if self.snake_body[0].heading() != LEFT:
            self.snake_body[0].setheading(RIGHT)
