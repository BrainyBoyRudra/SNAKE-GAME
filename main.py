
from ctypes import alignment
import random
import time
import turtle
points = 0
delay = 0.1
old_fruit = []
screen = turtle.Screen()
screen.title('SNAPE THE TURTLE')
screen.setup(width = 700,height = 700)
screen.tracer(0)
screen.bgcolor('turquoise')
turtle.speed(5)
turtle.pensize(6)
turtle.penup()
turtle.goto(-310,250)
turtle.pendown()
turtle.color('red')
turtle.forward(600)
turtle.right(90)
turtle.color('white')
turtle.forward(500)
turtle.right(90)
turtle.color('red')
turtle.forward(600)
turtle.right(90)
turtle.color('white')
turtle.forward(500)
turtle.hideturtle()
SNAPE = turtle.Turtle()
SNAPE.speed(0)
SNAPE.shape('turtle')
SNAPE.color('darkgreen')
SNAPE.penup()
SNAPE.goto(0,0)
SNAPE.direction = 'stop'
fruit = turtle.Turtle()
fruit.speed(0)
fruit.shape('arrow')
fruit.color('magenta')
fruit.penup()
fruit.goto(50,50)
score = turtle.Turtle()
score.speed(0)
score.shape('turtle')
score.color('navy')
score.penup()
score.goto(0,270)
score.write('SCORE :0',align = 'center',font =('courier',24,'bold'))
def snake_go_up():
    if SNAPE.direction != "down":
        SNAPE.direction = "up"
def snake_go_down():
    if SNAPE.direction != "up":
        SNAPE.direction = "down"
def snake_go_left():
    if SNAPE.direction != "right":
        SNAPE.direction = "left"
def snake_go_right():
    if SNAPE.direction != "left":
        SNAPE.direction = "right"
def snake_move ():
    if SNAPE.direction == "up":
        y = SNAPE.ycor()
        SNAPE.sety(y+20)
    elif SNAPE.direction == "down":
        y = SNAPE.ycor()
        SNAPE.sety(y-20)
    elif SNAPE.direction == "right":
        x = SNAPE.xcor()
        SNAPE.setx(x+20)
    elif SNAPE.direction =="left":
        x = SNAPE.xcor()
        SNAPE.setx(x-20)
screen.listen()
screen.onkeypress(snake_go_up,"Up")
screen.onkeypress(snake_go_down,"Down")
screen.onkeypress(snake_go_right,"Right")
screen.onkeypress(snake_go_left,"Left")






while True :
    screen.update()
    if SNAPE.distance(fruit) < 20:
        x = random.randint(-290,290)
        y = random.randint(-240,240)
        fruit.goto(x,y)
        score.clear()
        points += 1
        score.write('score:{}'.format(points),align = 'center',font =('courier',24,'bold'))
        delay -= 0.001
        new_fruit = turtle.Turtle()
        new_fruit.speed(0)
        new_fruit.shape('circle')
        new_fruit.color('green')
        new_fruit.penup()
        old_fruit.append(new_fruit)
    for index in range(len(old_fruit)-1,0,-1):
        a = old_fruit[index -1].xcor()
        b = old_fruit[index -1].ycor()
        old_fruit[index].goto(a,b)
    if len(old_fruit)>0:
        a = SNAPE.xcor()
        b = SNAPE.ycor()
        old_fruit[0].goto(a,b)

    snake_move()
    if SNAPE.xcor() > 290 or SNAPE.xcor() < -290 or SNAPE.ycor() > 240 or SNAPE.ycor() < -240:
        time.sleep(1)
        screen.clear()
        screen.bgcolor('cyan')
        score.goto (0,0)
        score.write("Game OVer\n your score is:- {}".format(points),align = 'center',font =('courier',24,'bold'))
    for food in old_fruit :
        if food.distance(SNAPE) < 20 :
            time.sleep(1)
            screen.clear()
            screen.bgcolor('cyan')
            score.goto (0,0)
            score.write("Game OVer\n your score is:- {}".format(points),align = 'center',font =('courier',24,'bold'))  
    time.sleep(delay)

turtle.Terminator()