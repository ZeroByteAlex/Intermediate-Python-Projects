from snake import Snake
import turtle
import time
import food
import scoreboard

screen = turtle.Screen()

def main():
    screen.title("Snake Game")
    screen.setup(600, 600)
    screen.bgcolor("black")
    screen.tracer(0)
    game_on = True
    snake = Snake()
    food_obj = food.Food()
    screen.listen()
    score = scoreboard.Scoreboard()

    while game_on:
        screen.update()
        time.sleep(0.1)

        snake.move()
        screen.onkeypress(snake.up, "Up")
        screen.onkeypress(snake.down, "Down")
        screen.onkeypress(snake.left, "Left")
        screen.onkeypress(snake.right, "Right")

        if snake.head.distance(food_obj) < 15:
            food_obj.refresh()
            snake.extend()
            score.increase_score()

        if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
            game_on = False
            score.game_over()

        for segment in snake.snake_body[1:]:
            if snake.head.distance(segment) < 10:
                game_on = False
                score.game_over()


if __name__ == "__main__":
    main()
    screen.exitonclick()
