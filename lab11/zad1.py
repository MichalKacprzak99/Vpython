from vpython import *
import random
import math
import numpy as np
m1 = 10
m2= 1000
balls = int(input("Enter number of balls: "))
rad_small=0.2
rad_big=1
ring=ring(pos=vector(0,0,0),axis=vector(0,0,1),radius=10, color=color.green)
def random_color():
    return vector(random.uniform(0,1),random.uniform(0,1),random.uniform(0,1))
Balls =  []
a=0
for i in range(10):
    if a == balls:
        break
    for j in range(10):
        if a==balls:
            break
        Balls.append(sphere(pos=vec(i,j,0)*3*rad_small,radius=rad_small,m=m1, color=random_color()))
        a=a+1
        
for i in range(balls):
    Balls[i].vel = vector(random.uniform(-10,10), random.uniform(-10,10), 0)

Big = sphere(pos = vector(-2,2,0), radius = rad_big, m = m2, color = color.red,make_trail = True)
Big.vel = vector(0,0,0)
Balls.append(Big)

t = 0
dt = 0.01

while t<100:
    rate(8000)
    for i in range(balls + 1):
        #collision with ring
        if (mag(Balls[i].pos + Balls[i].vel * dt) + Balls[i].radius) >= 10 - ring.thickness:
            Balls[i].vel -= 2 * (Balls[i].pos / mag(Balls[i].pos) * dot(Balls[i].vel, Balls[i].pos / mag(Balls[i].pos)))
            Balls[i].pos += Balls[i].vel * dt
        else:
            Balls[i].pos += Balls[i].vel * dt
            for j in range(i + 1, balls + 1):
                #collision with other ball
                if(mag((Balls[i].pos + Balls[i].vel * dt) - (Balls[j].pos + Balls[j].vel * dt)) < (Balls[i].radius + Balls[j].radius)):
                    
                    pos_of_ball_1 = (Balls[i].pos + Balls[i].vel * dt)
                    pos_of_ball_2 = (Balls[j].pos + Balls[j].vel * dt)

                    a = (mag(Balls[i].vel - Balls[j].vel)) ** 2
                    b = -2 * ((pos_of_ball_1 - pos_of_ball_2).dot(Balls[i].vel - Balls[j].vel))
                    c = (mag(pos_of_ball_1 - pos_of_ball_2) ** 2) - ((Balls[i].radius + Balls[j].radius) ** 2)

                    delta = b ** 2 - 4 * a * c
                    dt_prim = (-b + sqrt(delta)) / (2 * a)
                    if a==0 or delta<0:
                        continue
                    else:
                        pos_of_ball_1 -= Balls[i].vel * dt_prim
                        pos_of_ball_2 -= Balls[j].vel * dt_prim

                        new_vel_of_ball_1 = Balls[i].vel - 2 * (Balls[j].m/(Balls[i].m + Balls[j].m)) * ((Balls[i].vel - Balls[j].vel).dot((pos_of_ball_1 - pos_of_ball_2)/mag(pos_of_ball_1 - pos_of_ball_2))) * ((pos_of_ball_1 - pos_of_ball_2)/mag(pos_of_ball_1 - pos_of_ball_2))
                        new_vel_of_ball_2 = Balls[j].vel + 2 * (Balls[i].m/(Balls[i].m + Balls[j].m)) * ((Balls[i].vel - Balls[j].vel).dot((pos_of_ball_1 - pos_of_ball_2)/mag(pos_of_ball_1 - pos_of_ball_2))) * ((pos_of_ball_1 - pos_of_ball_2)/mag(pos_of_ball_1 - pos_of_ball_2))

                        new_pos_of_ball_1 = pos_of_ball_1 + new_vel_of_ball_1 * dt_prim
                        new_pos_of_ball_2 = pos_of_ball_2 + new_vel_of_ball_2 * dt_prim

                        Balls[i].pos = new_pos_of_ball_1
                        Balls[j].pos = new_pos_of_ball_2

                        Balls[i].vel = new_vel_of_ball_1
                        Balls[j].vel = new_vel_of_ball_2
    t += dt
