import turtle
import os
import math
import random

wn=turtle.Screen()
wn.bgcolor("black")
wn.title("Space Invaders")
wn.bgpic("space_invaders_background.gif")

turtle.register_shape("invader.gif")
turtle.register_shape("player.gif")


bpen=turtle.Turtle()
bpen.speed(0)
bpen.color("white")
bpen.penup()
bpen.setposition(-300,-300)
bpen.pendown()
bpen.pensize(3)
for side in range(4):
	bpen.fd(600)
	bpen.lt(90)
bpen.hideturtle()	

score = 0
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-290, 280)
scorestring = "Score: %s" %score
score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))
score_pen.hideturtle()

p=turtle.Turtle()
p.color("blue")
p.shape("player.gif")
p.shape("triangle")
p.penup()
p.speed(0)
p.setposition(0,-250)
p.setheading(90)

pspeed=15



number_of_enemies = 5
enemies = []
for i in range(number_of_enemies):
	enemies.append(turtle.Turtle())

for enemy in enemies:
	enemy.color("red")
	enemy.shape("invader.gif")
	enemy.penup()
	enemy.speed(0)
	x = random.randint(-200, 200)
	y = random.randint(100, 250)
	enemy.setposition(x, y)

enemyspeed = 2

bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()

bulletspeed = 20
bulletstate = "ready"

def move_left():
	x=p.xcor()
	x-=pspeed
	if x<-280:
		x=-280
	p.setx(x)

def move_right():
	x=p.xcor()
	x+=pspeed
	if x>280:
		x=280
	p.setx(x)

def fire_bullet():
	global bulletstate
	if bulletstate == "ready":
		bulletstate = "fire"
		x = p.xcor()
		y = p.ycor() + 10
		bullet.setposition(x, y)
		bullet.showturtle()

def isCollision(t1, t2):
	distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
	if distance < 15:
		return True
	else:
		return False

turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")
turtle.onkey(fire_bullet, "space")


while True:
	
	for enemy in enemies:
		x=enemy.xcor()
		x+=enemyspeed
		enemy.setx(x)
		
		if enemy.xcor() > 280:
			for e in enemies:
				y = e.ycor()
				y -= 40
				e.sety(y)
			enemyspeed *= -1
		
		if enemy.xcor() < -280:
			for e in enemies:
				y = e.ycor()
				y -= 40
				e.sety(y)
			enemyspeed *= -1

		if isCollision(bullet, enemy):
			bullet.hideturtle()
			bulletstate = "ready"
			bullet.setposition(0, -400)
			x = random.randint(-200, 200)
			y = random.randint(100, 250)
			enemy.setposition(x, y)
			score += 10
			scorestring = "Score: %s" %score
			score_pen.clear()
			score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))

		if isCollision(p, enemy):
			p.hideturtle()
			enemy.hideturtle()
			print ("Game Over")
			break

	if bulletstate == "fire":
			y = bullet.ycor()
			y += bulletspeed
			bullet.sety(y)
		
	if bullet.ycor() > 275:
		bullet.hideturtle()
		bulletstate = "ready"	
		

delay=input("Press enter to finish.")