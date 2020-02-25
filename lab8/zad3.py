from vpython import *
import numpy as np

#create box

lenght = 4.0
thickness = 0.7
rad=0.4
s2 = 2*lenght - thickness
s3 = 2*lenght + thickness

wallRight = box (pos=vector( lenght, 0, 0), size=vector(thickness, s2, s3),  color = color.red)
wallLeft = box (pos=vector(-lenght, 0, 0), size=vector(thickness, s2, s3),  color = color.blue)
wallDown = box (pos=vector(0, -lenght, 0), size=vector(s3, thickness, s3),  color = color.orange)
wallUP = box (pos=vector(0,  lenght, 0), size=vector(s3, thickness, s3),  color = color.purple)
wallBack = box(pos=vector(0, 0, -lenght), size=vector(s2, s2, thickness), color = color.gray(0.6))


#create list of sphere
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
            List_of_balls.append(sphere(pos=vec(i,j,k),radius=rad,flag=a,color=color.red,p=vector (np.random.uniform(0,2),np.random.uniform(0.5,2),np.random.uniform(0,2))))
            a=a+1
            if a==n:
                break

space = lenght - thickness*0.5 - rad
t=0
dt = 0.01
while t<100:
    rate(5000)
    for ball in List_of_balls:
        ball.pos = ball.pos + ball.p*dt
        if not (space > ball.pos.x > -space):
            ball.p.x = -ball.p.x
            if ball.pos.x>lenght:
                ball.color=wallRight.color
            if ball.pos.x<-lenght:
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
    #collision
    x=5
    y=5
    z=5
    for ball1 in List_of_balls:
        for ball2 in List_of_balls:
            if ball1.flag!=ball2.flag:
                v=ball1.pos-ball2.pos
                if(v.mag<=2*rad): 
                    ball2.p=vector(0,0,0)
                    ball1.p=vector(0,0,0)                  
                    ball2.pos=vector(x,y,z)
                    y+=1
                    ball1.pos=vector(x,y,z)
                    y+=1
                    
    t+=dt