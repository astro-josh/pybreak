import turtle


wn = turtle.Screen()
wn.title('PyBreak')
wn.bgcolor('black')
wn.setup(width=800, height=600)
wn.tracer(0)


paddle = turtle.Turtle()
paddle.speed(0)
paddle.shape('square')
paddle.shapesize(1, 5, 1)
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
    if(paddle.xcor() < 325):
        paddle.setx(paddle.xcor() + 40)

def paddle_left():
    if(paddle.xcor() > -325):
        paddle.setx(paddle.xcor() - 40)

wn.listen()
wn.onkeypress(paddle_right, 'Right')
wn.onkeypress(paddle_left, 'Left')

while True:
    wn.update()
