import turtle 
import time
import random

speed=0.15

window=turtle.Screen()
window.title("Snake Game")
window.bgcolor('lightgray')
window.setup(width=600, height=600)
window.tracer(0)  #this func is prevent update of window

head=turtle.Turtle()
head.speed(0)
head.shape('square')
head.color('green')
head.penup()  # won't write any word on screen when head moving   
head.goto(0,100)
head.direction="stop"

food=turtle.Turtle()
food.speed(0)
food.shape('circle')
food.color('red')
food.penup()  # won't write any word on screen when head moving   
food.goto(0,0)
food.shapesize(0.80,0.80)


tails=[]

puan=0

score=turtle.Turtle()
score.speed(0)

score.color('white')
score.penup()  # won't write any word on screen when head moving   
score.hideturtle()
score.goto(0,260)
score.write("Puan:{}".format(puan),align='center',font=('Arial',24,'normal','bold'))

def move():
    
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

def goUp():
    if head.direction !="down":
        head.direction="up"

def goDown():
    if head.direction!="up":
        head.direction="down"

def goRight():
    if head.direction!="left":
        head.direction="right"

def goLeft():
    if head.direction!="right":
        head.direction="left"         





window.listen()
window.onkey(goUp, "Up")
window.onkey(goDown, "Down")
window.onkey(goRight, "Right")
window.onkey(goLeft, "Left")





while True:
    window.update()


    if head.xcor()>300 or head.xcor()<-300  or head.ycor() > 300 or head.ycor() < -300:
       time.sleep(1)
       head.goto(0,0)
       head.direction="stop"

       for tail in tails:
           tail.goto(1000,1000)

       tails=[]
       puan=0
       speed=0.1
       score.clear()
       score.write("Puan:{}".format(puan),align='center',font=('Arial',24,'normal','bold'))

    if head.distance(food)<20:
        x=random.randint(-250,250)
        y=random.randint(-250,250)
        food.goto(x,y)
       

        newTail=turtle.Turtle()
        newTail.speed(0)
        newTail.shape('square')
        newTail.color('lightgreen')
        newTail.penup()
        tails.append(newTail)

        speed=speed- 0.001
        puan=puan+10
        score.clear()
        score.write("Puan:{}".format(puan),align='center',font=('Arial',24,'normal','bold'))



    for i in range(len(tails)-1,0,-1):
        x= tails[i-1].xcor()
        y=tails[i-1].ycor()
        tails[i].goto(x,y)

    if len(tails)>0:
        x=head.xcor()
        y=head.ycor()
        tails[0].goto(x,y)      

    move()
    for segment in tails:
        if segment.distance(head)<20:
            time.sleep(1)
            head.goto(0,0)
            head.direction="stop"
            for segment in tails:
                segment.goto(1000,1000)
            tails=[]
            puan=0
            score.clear()
            score.write("Puan:{}".format(puan),align='center',font=('Arial',24,'normal','bold'))
            speed=0.15
    time.sleep(speed)    




    
    
