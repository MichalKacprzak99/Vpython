from vpython import *
import numpy as np
lenght = 4.0
thickness = 0.7
rad=0.4
s2 = 2*lenght - thickness
s3 = 2*lenght + thickness

#create box
wallRight = box (pos=vector( lenght, 0, 0), size=vector(thickness, s2, s3),  color = color.red)
wallLeft = box (pos=vector(-lenght, 0, 0), size=vector(thickness, s2, s3),  color = color.blue)
wallDown = box (pos=vector(0, -lenght, 0), size=vector(s3, thickness, s3),  color = color.orange)
wallUP = box (pos=vector(0,  lenght, 0), size=vector(s3, thickness, s3),  color = color.purple)
wallBack = box(pos=vector(0, 0, -lenght), size=vector(s2, s2, thickness), color = color.gray(0.6))

#create spheres
List_of_balls=[]
n=40#np.random.randint(1,51)
a=0
for i in range(-1,3):
    if a == n:
        break
    for j in range(-3,1):
        if a == n:
            break
        for k in range(0,4):
            List_of_balls.append(sphere(pos=vec(i,j,k),radius=rad, color=color.magenta,p=vector (np.random.uniform(0,2),np.random.uniform(0.5,2),np.random.uniform(0,2))))
            a=a+1
            if a==n:
                break


space = lenght - thickness*0.5 - rad
t=0
dt=0.01
while t<100:
    rate(5000)
    for ball in List_of_balls:
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