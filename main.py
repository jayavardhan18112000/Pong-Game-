import turtle
import winsound
import time
from PIL import Image

window = turtle.Screen()
window.title("Pong game")
window_width = 700
window_height = 500
window.setup(width=window_width, height=window_height)

image_filename = "pongbgpic.jpg"
background_image = Image.open(image_filename)
background_image = background_image.resize((window_width, window_height))

background_image = background_image.convert("RGB")
background_image.save("background.gif")

window.bgpic("background.gif")

import os
os.remove("background.gif")

window.tracer(0)

score1 = 0
score2 = 0

paddle1 = turtle.Turtle()
paddle1.speed(0)
paddle1.shape('square')
paddle1.color('cyan')
paddle1.shapesize(stretch_wid=5, stretch_len=1)
paddle1.penup()
paddle1.goto(-320, 0)

paddle2 = turtle.Turtle()
paddle2.speed(0)
paddle2.shape('square')
paddle2.color('magenta')
paddle2.shapesize(stretch_wid=5, stretch_len=1)
paddle2.penup()
paddle2.goto(320, 0)

ball = turtle.Turtle()
ball.speed(0)
ball.shape('circle')
ball.color('white')
ball.penup()
ball.goto(0, 0)
ballx = 0.1
bally = 0.1

pen = turtle.Turtle()
pen.speed(0)
pen.color('red')
pen.penup()
pen.hideturtle()
pen.goto(0, 220)
pen.write('Human: 0  Computer: 0', align='center', font=('Courier', 18, 'normal'))


def paddle1_up():
    y = paddle1.ycor()
    y += 20
    paddle1.sety(y)


def paddle1_down():
    y = paddle1.ycor()
    y -= 20
    paddle1.sety(y)


def paddle2_up():
    y = paddle2.ycor()
    y += 20
    paddle2.sety(y)


def paddle2_down():
    y = paddle2.ycor()
    y -= 20
    paddle2.sety(y)


window.listen()
window.onkeypress(paddle1_up, 'w')
window.onkeypress(paddle1_down, 's')


def wait_for_click():
    window.update()
    window.onclick(exit_game)


def exit_game(x, y):
    global game
    game = False


def computer_paddle():
    if ball.xcor() > 0:
        if paddle2.ycor() < ball.ycor() and abs(paddle2.ycor() - ball.ycor()) > 10:
            paddle2_up()
        elif paddle2.ycor() > ball.ycor() and abs(paddle2.ycor() - ball.ycor()) > 10:
            paddle2_down()



game = True

while game:
    window.update()

    ball.setx(ball.xcor() + ballx)
    ball.sety(ball.ycor() + bally)

    if ball.ycor() > 240:
        ball.sety(240)
        bally *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if ball.ycor() < -240:
        ball.sety(-240)
        bally *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if (ball.xcor() > 290 and ball.xcor() < 300) and (ball.ycor() < paddle2.ycor() + 40 and ball.ycor() > paddle2.ycor() - 40):
        ball.setx(290)
        ballx *= -1
        winsound.PlaySound("hit.wav", winsound.SND_ASYNC)

    if (ball.xcor() < -290 and ball.xcor() > -300) and (ball.ycor() < paddle1.ycor() + 40 and ball.ycor() > paddle1.ycor() - 40):
        ball.setx(-290)
        ballx *= -1
        winsound.PlaySound("hit.wav", winsound.SND_ASYNC)

    if ball.xcor() > 350 or ball.xcor() < -350:
        ball.goto(0, 0)
        ballx *= -1
        winsound.PlaySound("beeep-43965.mp3", winsound.SND_ASYNC)
        pen.clear()
        if ball.xcor() > 350:
            score1 += 1
        else:
            score2 += 1
        pen.write(f'Human: {score1}  Computer: {score2}', align='center', font=('Courier', 18, 'normal'))

    if score1 == 5 or score2 == 5:
        pen.goto(0, 0)
        pen.write('Game Over', align='center', font=('Courier', 24, 'normal'))
        window.update()
        time.sleep(3)
        pen.clear()
        wait_for_click()

    computer_paddle()


turtle.done()
