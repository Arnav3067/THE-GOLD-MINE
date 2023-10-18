import turtle
import random
import math
import time

def draw_border(): 
    border = turtle.Turtle()
    border.speed(50)
    border.penup()
    border.color('white')
    border.setposition(-300, -300)
    border.pendown()
    border.pensize(4)
    for i in range(4):
        border.forward(600)
        border.left(90)
    border.hideturtle()


wn = turtle.Screen()
wn.bgcolor('black')
wn.title('GAME OF THE YEAR')

draw_border()

p = turtle.Turtle()
p.color('white')
p.penup()
p.speed(0)
speed = 1
speed_vic = 1
score = 0
victims = turtle.Turtle()
victims.setposition(random.randint(-300, 300), random.randint(-300, 300))
victims.penup()
victims.shape('square')
victims.color('white')
victims.speed(0)


def border_check(character):
    character = str(character)
    character.lower()
    if character.isalpha():
        if character == 'victims':
            if victims.xcor() > 295 or victims.xcor() < -305:
                victims.left(50)
                global speed_vic
                if speed_vic < 15 :
                    speed_vic += 1
            elif victims.ycor() > 295 or victims.ycor() < -305:
                victims.left(50)
        elif character == 'player':
            if p.xcor() > 295 or p.xcor() < -305:
                p.left(180)
            elif p.ycor() > 295 or p.ycor() < -305:
                p.left(180)
        else:
            NameError
            exit()
    else:
       NameError
       exit()

Score = turtle.Turtle()
Score.penup()
Score.color('white')
Score.hideturtle()

task = turtle.Turtle()
task.penup()
task.setposition(0,310)
task.color('white')
task.hideturtle()
task.write('chase the square', move=False, align='center', font=('source code pro', 16, 'normal'))




def draw_score() :
    Score.clear()
    Score.write(f'Score : {score}/20', move=False, align='center', font=('Source code pro', 14, 'bold'))


   


def left():
    p.left(45)


def right():
    p.right(45)


def speed_up():
    global speed
    if speed < 25 :
        speed += 1


def speed_down():
    global speed
    speed = speed - 1


def random_positioning():
    victims.setposition(random.randint(-285, 285), random.randint(-285, 285))
    victims.left(random.randint(0, 360))
    victims.showturtle()


def collision_check():
    S = math.sqrt(math.pow((p.xcor() - victims.xcor()), 2) + math.pow((p.ycor() - victims.ycor()), 2))
    if S < 30:
        victims.hideturtle()
        random_positioning()
        global score
        score += 1
        draw_score()

def draw_end():
    wn.bgcolor('black')
    finish = turtle.Turtle()
    finish.color('red')
    finish.hideturtle()
    finish.write('YOU WIN !!', move=False, align='center', font=('source code pro', 40, 'normal'))

turtle.listen()
turtle.onkey(left, 'a')
turtle.onkey(right, 'd')
turtle.onkey(speed_up, 'w')
turtle.onkey(speed_down, 's')
running = True

while running :
    p.forward(speed)
    border_check('player')
    border_check('victims')
    collision_check()
    victims.forward(speed_vic)
    if score == 20:
        wn.clearscreen()
        running = False
draw_end()

turtle.exitonclick()
    

