import turtle
import time
import random

# Screen
wn = turtle.Screen()
wn.colormode(255)
wn.title("PONG Game")
wn.bgcolor(44, 57, 71)
wn.setup(width=800, height=600)
wn.tracer(0)

# Score
score_l = 0
score_r = 0

#--------------------------paddeles-------------------------------------

# Paddle l
paddle_l = turtle.Turtle()
paddle_l.speed(0)
paddle_l.shape("square")
paddle_l.color("#BED4CB")
paddle_l.penup()
paddle_l.goto(-350,0)
paddle_l.shapesize(stretch_wid=5, stretch_len=1)

# Paddle r
paddle_r = turtle.Turtle()
paddle_r.speed(0)
paddle_r.shape("square")
paddle_r.color("#BED4CB")
paddle_r.penup()
paddle_r.goto(350,0)
paddle_r.shapesize(stretch_wid=5, stretch_len=1)

#---------------------Balll---------------------------
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("#B35656")
ball.penup()
ball.goto(0,0)
ball.shapesize(stretch_wid=1.2, stretch_len=1.2)
ball.pensize(2)                
ball.pencolor("white")   

# Moving the Ball-
ball.dx = 1.5
ball.dy = 1.5

#-------------------Scoring----------------------------
score = turtle.Turtle()
score.speed(0)
score.color("#BF124D")
score.penup()
score.hideturtle()
score.goto(0,260)
score.write("PlayerA: 0     PlayerB: 0", align ="center", font=("courier", 24,"normal"))

#--------------------------Moving the Paddles----------------------------------

#----------Paddle_l Movements
# Paddle_l --> up movement
def paddle_l_up():
    y = paddle_l.ycor()
    y += 20
    paddle_l.sety(y)

# Paddle_l --> Down Movement
def paddle_l_down():
    y = paddle_l.ycor()
    y += -20
    paddle_l.sety(y)



#----------Paddle_r Movements
# Paddle_r --> up movement
def paddle_r_up():
    y = paddle_r.ycor()
    y += 20
    paddle_r.sety(y)

# Paddle_r --> Down Movement
def paddle_r_down():
    y = paddle_r.ycor()
    y += -20
    paddle_r.sety(y)

def clamp_paddle(paddle):
    if paddle.ycor() > 250:
        paddle.sety(250)
    elif paddle.ycor() < -250:
        paddle.sety(-250)


#---------------Keyboard listening---------------
wn.listen()

# Paddle_l
wn.onkeypress(paddle_l_up, "w")
wn.onkeypress(paddle_l_down, "s")

# Paddle_r
wn.onkeypress(paddle_r_up, "Up")
wn.onkeypress(paddle_r_down, "Down")




#-----------------------------Main game loop--------------------------------
while True:
    wn.update()

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    clamp_paddle(paddle_l)
    clamp_paddle(paddle_r)

#--Boundary Checking Balls---------------------------------
# Top
    if ball.ycor() > 280:
        ball.sety(280)
        ball.dy *= -1

# Bottom
    if ball.ycor() < -280:
        ball.sety(-280)
        ball.dy *= -1

# Right
    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx = random.choice([2, -2])
        ball.dy = random.choice([1.5, -1.5])
        score_l += 1
        score.clear()
        score.write("PlayerA: {}     PlayerB: {}".format(score_l, score_r), align ="center", font=("courier", 24,"normal"))

# Left
    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx = random.choice([2, -2])
        ball.dy = random.choice([1.5, -1.5])
        score_r += 1
        score.clear()
        score.write("PlayerA: {}     PlayerB: {}".format(score_l, score_r), align ="center", font=("courier", 24,"normal"))

#--Boundary Checking---------------------------------
#-----Paddles_l
# Top
    if paddle_l.ycor() > 250:
        paddle_l.sety(250)
        

# Bottom
    if paddle_l.ycor() < -250:
        paddle_l.sety(-250)
        

#-----Paddles_r
# Top
    if paddle_r.ycor() > 250:
        paddle_r.sety(250)
        

# Bottom
    if paddle_r.ycor() < -250:
        paddle_r.sety(-250)
        

# Paddle Collision with ball----------
# Right Paddle
    if (ball.xcor() > 320  and ball.xcor() < 360) and (ball.ycor() < paddle_r.ycor()+50 and ball.ycor() > paddle_r.ycor() - 50):
        ball.setx(320)
        ball.dx *= -1

# left Paddle
    if (ball.xcor() < -320  and ball.xcor() > -360) and (ball.ycor() < paddle_l.ycor()+50 and ball.ycor() > paddle_l.ycor() - 50):
        ball.setx(-320)
        ball.dx *= -1


    time.sleep(0.01)

