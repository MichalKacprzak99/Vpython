from vpython import *

scene1=graph(x=60,y=400,width=700,height=400,xtitle='s',ytitle='pos')


ball1=sphere(pos=vec(0,1,0),radius=0.1,color=color.red)
ball2=sphere(pos=vec(0,1.25,0),radius=0.1,color=color.white)
ball3=sphere(pos=vec(0,1.5,0),radius=0.1,color=color.red)

walld=box(pos=vec(0,-0.5,0),size=vec(20,0.1,0.1),color=color.green)

ball1.m=10
ball2.m=1
ball3.m=0.1

ball1.vel=vec(0,0,0)
ball2.vel=vec(0,0,0)
ball3.vel=vec(0,0,0)

g=vec(0,-9.8,0)
f1=gcurve(color=color.red)
f2=gcurve(color=color.blue)

tt = label(pos=vec(0, -2, 0))

tt.text = "pos.y= " + str(ball3.pos.y) + " Total Energy= "+ str(ball1.pos.y*ball1.m*9.8+ball2.pos.y*ball2.m*9.8+ball3.pos.y*ball3.m*9.8)
t = 0
dt = 0.00001

while t<60 :

    if ball3.pos.y  <= ball2.pos.y+0.1:
        vel1 = ((ball3.m - ball2.m) / (ball3.m + ball2.m)) * ball3.vel + ((2 * ball2.m) / (ball3.m + ball2.m)) * ball2.vel
        vel2 = ((ball2.m - ball3.m) / (ball3.m + ball2.m)) * ball2.vel + ((2 * ball3.m) / (ball3.m + ball2.m)) * ball3.vel

        ball3.vel = vel1
        ball2.vel = vel2

    elif ball2.pos.y <= ball1.pos.y+0.1:
        vel1 = ((ball2.m - ball1.m) / (ball2.m + ball1.m)) * ball2.vel + ((2 * ball1.m) / (ball2.m + ball1.m)) * ball1.vel
        vel2 = ((ball1.m - ball2.m) / (ball2.m + ball1.m)) * ball1.vel + ((2 * ball2.m) / (ball2.m + ball1.m)) * ball2.vel

        ball2.vel = vel1
        ball1.vel = vel2

    elif ball1.pos.y - 0.1 <= walld.pos.y:
        ball1.vel = -ball1.vel

    ball1.vel = ball1.vel+g*dt
    ball2.vel = ball2.vel+g*dt
    ball3.vel = ball3.vel+g*dt

    ball1.pos = ball1.pos + ball1.vel * dt
    ball2.pos = ball2.pos + ball2.vel * dt
    ball3.pos = ball3.pos + ball3.vel * dt

    f1.plot(pos=(t,ball2.pos.y))
    f2.plot(pos=(t,ball3.pos.y))


    energy_pot = ball1.pos.y*ball1.m*9.8+ball2.pos.y*ball2.m*9.8+ball3.pos.y*ball3.m*9.8

    energy_kin = ball1.m * ball1.vel.y ** 2 / 2 + ball2.m * ball2.vel.y ** 2 / 2 + ball3.m * ball3.vel.y ** 2 / 2

    total_energy = energy_pot + energy_kin

    tt.text = "pos.y= " + str(ball3.pos.y) + " Total Energy= "+ str(total_energy)

    t+=dt