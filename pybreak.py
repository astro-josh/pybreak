import turtle


wn = turtle.Screen()
wn.title('PyBreak')
wn.bgcolor('black')
wn.setup(width=800, height=600)
wn.tracer(0)


paddle = turtle.Turtle()
paddle.speed(0)
paddle.shape('square')
paddle.shapesize(stretch_wid=1, stretch_len=5)
paddle.color('blue')
paddle.penup()
paddle.goto(0, -250)

ball = turtle.Turtle()
ball.speed(0)
ball.shape('square')
ball.color('white')
ball.penup()
ball.goto(0, 0)

def paddle_right():
    paddle.setx(paddle.xcor() + 20)

def paddle_left():
    paddle.setx(paddle.xcor() - 20)

wn.listen()
wn.onkeypress(paddle_right, 'Right')
wn.onkeypress(paddle_left, 'Left')

while True:
    wn.update()
