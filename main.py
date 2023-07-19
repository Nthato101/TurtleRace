import turtle
from turtle import Turtle,Screen
import random
window = Screen()
window.setup(width=1000, height=800)

bet = window.textinput(title="Make your bet",prompt="Which Turtle will win,pick a colour: ")

# Racer_1 initialize
racer_1 = Turtle(shape="turtle")
racer_1.color("red")
racer_1.penup()
racer_1.goto(x=-485,y=-300)

# Racer_2 initialize
racer_2 = Turtle(shape="turtle")
racer_2.color("orange")
racer_2.penup()
racer_2.goto(x=-485,y =-200)

# Racer_3 initialize
racer_3 = Turtle(shape="turtle")
racer_3.color("yellow")
racer_3.penup()
racer_3.goto(x=-485,y =-100)

# Racer_4 initialize
racer_4 = Turtle(shape="turtle")
racer_4.color("green")
racer_4.penup()
racer_4.goto(x=-485,y =0)

# Racer_5 initialize
racer_5 = Turtle(shape="turtle")
racer_5.color("blue")
racer_5.penup()
racer_5.goto(x=-485,y =100)

# Racer_6 initialize
racer_6 = Turtle(shape="turtle")
racer_6.color("violet")
racer_6.penup()
racer_6.goto(x=-485,y =200)

if bet:
    racing = True
start_list = [racer_1,racer_2,racer_3,racer_4,racer_5,racer_6]
finish_list = []
count = 0
while racing:

    if racer_1.xcor() < 450:
        racer_1.forward(random.randint(0,10))
    else:
        #finish_list.append(racer_1.color())
        racer_1.setx(470)
    if racer_2.xcor() < 450:
        racer_2.forward(random.randint(0, 10))
    else:
        #finish_list.append(racer_2.color())
        racer_2.setx(470)
    if racer_3.xcor() < 450:
        racer_3.forward(random.randint(0, 10))
    else:
        #finish_list.append(racer_3.color())
        racer_3.setx(470)
    if racer_4.xcor() < 450:
        racer_4.forward(random.randint(0, 10))
    else:
        #finish_list.append(racer_4.color())
        racer_4.setx(470)
    if racer_5.xcor() < 450:
        racer_5.forward(random.randint(0, 10))
    else:
        #finish_list.append(racer_5.color())
        racer_5.setx(470)
    if racer_6.xcor() < 450:
        racer_6.forward(random.randint(0, 10))
    else:
        #finish_list.append(racer_6.color())
        racer_6.setx(470)

    for i in range(0,6):
        if start_list[i].xcor() >= 450 and start_list[i].pencolor() not in finish_list:
            finish_list.append(start_list[i].pencolor())
    count = len(finish_list)
    if count == 6:
        racing = False



print(f"Your bet is {bet}")
print(f"Winner is {finish_list[0]}")
if bet == finish_list[0]:
    print("You win")
else:
    print("You lose")

















window.exitonclick()