from vpython import *
import math


phi1=math.pi
teta1=math.pi-0.1

phi2=math.pi
teta2=math.pi-0.1

g1=9.8
g2=9.800000000000001

L1=1
L2=1.0000000000001

rad=0.1
dt=0.001
t=0
##############################
ball1_radio_vel=0
ball2_radio_vel=0

ball1=sphere(pos=vector(L1*math.sin(phi1),-L1*math.cos(phi1),0), radius=rad,color=color.blue)
ball2=sphere(pos=vector(L1*(math.sin(phi1)+math.sin(teta1)),-L1*(math.cos(phi1)+math.cos(teta1)),0), radius=rad,color=color.blue)

con1=cylinder(pos=vector(0,0,0), axis=ball1.pos , radius=0.01)
con2=cylinder(pos=ball1.pos, axis=ball2.pos-ball1.pos , radius=0.01)
############################
ball3_radio_vel=0
ball4_radio_vel=0
ball3=sphere(pos=vector(L1*math.sin(phi2),-L1*math.cos(phi2),0), radius=rad,color=color.blue)
ball4=sphere(pos=vector(L1*(math.sin(phi2)+math.sin(teta2)),-L1*(math.cos(phi2)+math.cos(teta2)),0), radius=rad,color=color.blue)

con3=cylinder(pos=vector(0,0,0), axis=ball3.pos , radius=0.01)
con4=cylinder(pos=ball3.pos, axis=ball4.pos-ball3.pos , radius=0.01)

label1=label(pos=vec(3,3,0), text=str(0))

while t<1000:
    rate(1000)
    tmp1=1+(math.sin(phi1-teta1))**2

    ball1_radio_acc=(-g1/L1*(2*math.sin(phi1)-math.sin(teta1)*math.cos(phi1-teta1))-1/2*ball1_radio_vel**2*math.sin(2*phi1-2*teta1)-ball2_radio_vel*math.sin(phi1-teta1))/tmp1
    ball2_radio_acc=(-g1/L1*(2*math.sin(teta1)-2*math.sin(phi1)*math.cos(phi1-teta1))+1/2*ball2_radio_vel**2*math.sin(2*phi1-2*teta1)+2*ball1_radio_vel**2*math.sin(phi1-teta1))/tmp1
    
    ball1_radio_vel=ball1_radio_vel+ball1_radio_acc*dt
    ball2_radio_vel=ball2_radio_vel+ball2_radio_acc*dt

    phi1=phi1+ball1_radio_vel*dt
    teta1=teta1+ball2_radio_vel*dt

    ball1.pos=vector(L1*math.sin(phi1),-L1*math.cos(phi1),0)
    ball2.pos=vector(L1*(math.sin(phi1)+math.sin(teta1)),-L1*(math.cos(phi1)+math.cos(teta1)),0)

    con1.axis=ball1.pos
    con2.pos=ball1.pos
    con2.axis=ball2.pos-ball1.pos

    Energy1=g1*ball1.pos.y+g1*ball2.pos.y+1/2*L1**2*(ball1_radio_vel**2+ball1_radio_vel**2+ball2_radio_vel**2+2*ball2_radio_vel*ball1_radio_vel*math.cos(phi1-teta1))
    
    label1.text=str(Energy1)
   #########################################################3
    tmp2=1+(math.sin(phi2-teta2))**2
    ball3_radio_acc=(-g2/L1*(2*math.sin(phi2)-math.sin(teta2)*math.cos(phi2-teta2))-1/2*ball3_radio_vel*math.sin(2*phi2-2*teta2)-ball4_radio_vel*math.sin(phi2-teta2))/tmp2
    ball4_radio_acc=(-g2/L1*(2*math.sin(teta2)-2*math.sin(phi2)*math.cos(phi2-teta2))+1/2*ball4_radio_vel*math.sin(2*phi2-2*teta2)+2*ball3_radio_vel**2*math.sin(phi2-teta2))/tmp2
    
    ball3_radio_vel=ball3_radio_vel+ball3_radio_acc*dt
    ball4_radio_vel=ball4_radio_vel+ball4_radio_acc*dt

    phi2=phi2+ball3_radio_vel*dt
    teta2=teta2+ball4_radio_vel*dt

    ball3.pos=vector(L1*math.sin(phi2),-L1*math.cos(phi2),0)
    ball4.pos=vector(L1*(math.sin(phi2)+math.sin(teta2)),-L1*(math.cos(phi2)+math.cos(teta2)),0)

    con3.axis=ball3.pos
    con4.pos=ball3.pos
    con4.axis=ball4.pos-ball3.pos
   
    t=t+dt
    