import random
import turtle as turtle
from turtle import *
screen = Screen()
screen.setup(width = 500 , height = 380)
user_bet = screen.textinput(title= "Make your bet!" , prompt="Witch turtle is going to win the race?")
t1 = Turtle()
t2 = Turtle()
t3 = Turtle()
t4 = Turtle()
t5 = Turtle()
t6 = Turtle()
def initialize_turtles():
    t1.color("red")
    t1.shape("turtle")
    t1.penup()
    t1.goto(x=-240, y=-80)

    t2.color("orange")
    t2.shape("turtle")
    t2.penup()
    t2.goto(x=-240, y=-50)

    t3.color("yellow")
    t3.shape("turtle")
    t3.penup()
    t3.goto(x=-240, y=-20)

    t4.color("green")
    t4.shape("turtle")
    t4.penup()
    t4.goto(x=-240, y=10)

    t5.color("blue")
    t5.shape("turtle")
    t5.penup()
    t5.goto(x=-240, y=40)

    t6.color("purple")
    t6.shape("turtle")
    t6.penup()
    t6.goto(x=-240, y=70)


def random_distance():
    return random.randint(1,10)

def start_race():
    t1.forward(random_distance())
    t2.forward(random_distance())
    t3.forward(random_distance())
    t4.forward(random_distance())
    t5.forward(random_distance())
    t6.forward(random_distance())

    if t1.xcor() >= 200:
        return "red"
    elif t2.xcor() >= 200:
        return "orange"
    elif t3.xcor() >= 200:
        return "yellow"
    elif t4.xcor() >= 200:
        return "green"
    elif t5.xcor() >= 200:
        return "blue"
    elif t6.xcor() >= 200:
        return "purple"
    else:
        return start_race()


initialize_turtles()
winner = start_race()

if user_bet == winner:
    print(f"You won! The winner is {winner}")
else:
    print(f"You lost. The winner is {winner}")

screen.exitonclick()
