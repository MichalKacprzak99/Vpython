import vpython
import numpy as np

lenght = 4.0
thickness = 0.7
rad=0.4
s2 = 2*lenght - thickness
s3 = 2*lenght + thickness
#create box
wallRight=box(pos=vector(lenght,0,0),size=vector(thickness,s2,s3), color=color.red)
wallLeft = box (pos=vector(-lenght, 0, 0), size=vector(thickness, s2, s3),  color = color.blue)
wallDown = box (pos=vector(0, -lenght, 0), size=vector(s3, thickness, s3),  color = color.orange)
wallUP = box (pos=vector(0,  lenght, 0), size=vector(s3, thickness, s3),  color = color.purple)
wallBack = box(pos=vector(0, 0, -lenght), size=vector(s2, s2, thickness), color = color.gray(0.6))
#create sphere
ball=sphere(color = color.green, radius =rad, p=vector(np.random.uniform(0,3),np.random.uniform(0,3),np.random.uniform(0,3)))
space = lenght - thickness*0.5 - rad
t=0
dt=0.01
while t<100:
    rate(5000)
    ball.pos = ball.pos + ball.p*dt
    if not (space > ball.pos.x > -space):
        ball.p.x = -ball.p.x
        if ball.pos.x>space:
            ball.color=wallRight.color
        if ball.pos.x<-space:
            ball.color=wallLeft.color

    if not (space > ball.pos.y > -space):
        ball.p.y = -ball.p.y
        if ball.pos.y>space:
            ball.color=wallUP.color
        if ball.pos.y<-space:
            ball.color=wallDown.color

    if not (space > ball.pos.z > -space):
        ball.p.z = -ball.p.z
        if ball.pos.z>space:
            ball.color=color.white
        if ball.pos.z<-space:
            ball.color=wallBack.color