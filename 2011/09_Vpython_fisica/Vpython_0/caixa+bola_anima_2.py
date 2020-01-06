from visual import *
ball = sphere(pos=(-5,0,0), radius=0.5, color=color.cyan)
wallR = box(pos=(6,0,0), size=(0.2,12,12), color=color.green)
ball.velocity = vector(500,0,0)
t=0
varr = arrow(pos=ball.pos, axis=ball.velocity, color=color.yellow)
delta = 0.005
while t < 3:
	rate(50)
	if ball.pos.x > wallR.pos.x:
		ball.velocity.x = -ball.velocity.x
	ball.pos = ball.pos + ball.velocity*delta
	
	t = t + delta
	ball.velocity = vector(25,5,0)
