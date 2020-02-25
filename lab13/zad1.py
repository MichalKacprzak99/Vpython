from vpython import *
k=2

scene = canvas(width=1800, height=980, center=vec(0, 0, 0))
box1=box(pos=vec(0,0,0),size=vec(1,1,0.1),color=color.red)
box2=box(pos=vec(1,0,0),size=vec(1,1,0.1),color=color.blue)
wall=box(pos=vec(2,4,0),size=vec(0.1,9,0.1),color=color.green)
walld=box(pos=vec(0,-0.5,0),size=vec(20,0.1,0.1),color=color.green)

box1.vel=vec(1,0,0)
box2.vel=vec(0,0,0)
box1.m=100**k
box2.m=1
collision_label = label(pos=vec(0, -1, 0))
t=0
dt = 0.00001
collisions=0
while( t<1000 ):
    
    if box1.pos.x+1>box2.pos.x:
        vel1 = ((box1.m - box2.m) / (box1.m + box2.m)) * box1.vel + ((2 * box2.m) / (box1.m + box2.m)) * box2.vel
        vel2 = ((box2.m - box1.m) / (box1.m + box2.m)) * box2.vel + ((2 * box1.m) / (box1.m + box2.m)) * box1.vel

        box1.vel = vel1
        box2.vel = vel2

        collisions +=1
    elif box2.pos.x+0.55>wall.pos.x:
        box2.vel = -box2.vel
        collisions += 1

    box1.pos=box1.pos+box1.vel*dt
    box2.pos=box2.pos+box2.vel*dt

    collision_label.text = "Number of collisions= " + str(collisions)
    t+=dt