from vpython import *
import numpy as np


def b(n):
    rad=0.3
    B = []
    a=0
    for i in range(-3,4):
        if a == n:
            break
        for j in range(-3,4):
            if a == n:
                break
            for k in range(-3,4):
                B.append(sphere(pos=vec(i,j,k),radius=rad, color=color.red))
                a=a+1
                if a==n:
                    break

    for i in B:
        i.vel = vec(np.random.uniform(0, 1), np.random.uniform(0, 1), np.random.uniform(0, 1))
    w = 0.4
    wallR = box(pos=vec(4, 0, 0), size=vec(w, 8 + w, 8), color=color.red)
    wallL = box(pos=vec(-4, 0, 0), size=vec(w, 8 + w, 8), color=color.green)
    wallU = box(pos=vec(0, -4, 0), size=vec(8 + w, w, 8), color=color.orange)
    wallD = box(pos=vec(0, 4, 0), size=vec(8 + w, w, 8), color=color.blue)
    wallB = box(pos=vec(0, 0, -4), size=vec(8+w, 8 + w, w), color=color.magenta)
    T=B[:]
    t = 0
    dt = 0.005
    while t < 100:
        rate(1000)
        for i in B:
            i.pos = i.pos + i.vel * dt

            if abs(i.pos.x) + i.radius >= wallR.pos.x - w and i.pos.x > 0:
                i.vel.x = -i.vel.x
                i.color = wallR.color

            elif abs(i.pos.y) + i.radius >= abs(wallD.pos.y) - w and i.pos.y > 0:
                i.vel.y = -i.vel.y
                i.color = wallD.color
            elif abs(i.pos.z) + i.radius >= abs(wallB.pos.z) - w and i.pos.z < 0:
                i.vel.z = -i.vel.z
                i.color = wallB.color
            elif abs(i.pos.x) + i.radius >= abs(wallR.pos.x) - w and i.pos.x < 0:
                i.vel.x = -i.vel.x
                i.color = wallL.color

            elif abs(i.pos.y) + i.radius >= abs(wallD.pos.y) - w and i.pos.y < 0:
                i.vel.y = -i.vel.y
                i.color = wallU.color
            elif abs(i.pos.z) + i.radius >= abs(wallB.pos.z) - w and i.pos.z > 0:
                i.vel.z = -i.vel.z
                i.color = color.white

        for c in range(n-1):
            for j in B[c+1:]:
                if(sqrt((j.pos.x-B[c].pos.x)**2+(j.pos.y-B[c].pos.y)**2+(j.pos.z-B[c].pos.z)**2)<=2*rad):
                    temp=B[c].vel.x
                    B[c].vel.x=j.vel.x
                    j.vel.x=temp
                    temp = B[c].vel.y
                    B[c].vel.y = j.vel.y
                    j.vel.y = temp
                    temp = B[c].vel.z
                    B[c].vel.z = j.vel.z
                    j.vel.z = temp
                    #print("there is a collision")
        t = t + dt


def main(args):

    #b(np.random.randint(1, 51))
    b(50)



if __name__ == '__main__':
    import sys

    sys.exit(main(sys.argv))
