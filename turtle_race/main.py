from turtle import Turtle, Screen
import random

def turtle_colors():
    for turtle in racers:
        random_color = random.choice(colors)
        turtle.color(random_color)
        colors.remove(random_color)

def turtle_positions():
    for turtle in racers:
        turtle.penup()

    turtle1.goto(-230, 100)
    turtle2.goto(-230, 70)
    turtle3.goto(-230, 40)
    turtle4.goto(-230, 10)
    turtle5.goto(-230, -20)
    turtle6.goto(-230, -50)

def turtles_racing():
    for turtle in racers:
        turtle.forward(random.randint(1, 10))

def main():
    race_on = False
    while not race_on:
        player_bet = screen.textinput("Welcome to turtle racing!", "What color is your turtle?: ")
        if player_bet:
            race_on = True

    turtle_colors()
    turtle_positions()

    for turtle in racers:
        turtle.speed(1)
    while race_on:
        turtles_racing()
        for turtle in racers:
            if turtle.xcor() > 230:
                winning_color = turtle.pencolor()
                race_on = False

    print(f"The winner of the race is {winning_color}")
    if winning_color == player_bet:
        print("You've won!")
    else:
        print("You've lost!")

if __name__ == "__main__":
    turtle1 = Turtle("turtle")
    turtle2 = Turtle("turtle")
    turtle3 = Turtle("turtle")
    turtle4 = Turtle("turtle")
    turtle5 = Turtle("turtle")
    turtle6 = Turtle("turtle")
    screen = Screen()

    racers = [turtle1, turtle2, turtle3, turtle4, turtle5, turtle6]

    screen.title("Turtle Racing")
    screen.setup(500, 400)
    colors = ["red", "orange", "yellow", "green", "blue", "purple"]
    main()
    screen.bye()
