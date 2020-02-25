from vpython import *
Balls=[]
for i in range(1,4):
    Balls.append(sphere(pos=vector(i*2,0,0),radius=0.75 ,vel=vector(0,0,0), weight=1,color=color.white))
Balls[0].pos=vector(2,2,0)   
Helixes=[]
Helixes.append(helix(pos=vector(0,0,0),a=vector(0,0,0), radius=0.5, axis=Balls[0].pos,color=color.green))

for i in range(2):
    Helixes.append(helix(pos=Balls[i].pos, radius=0.5, axis=Balls[i+1].pos-Balls[i].pos,color=color.green))
Helixes.append(helix(pos=Balls[2].pos, radius=0.5, axis=vector(8,0,0)-Balls[2].pos,color=color.green))

wallLeft= box(pos=vector(-0.5,0,0), size=vector(1,5,5))
wallRight= box(pos=vector(8.5,0,0), size=vector(1,5,5))

t=0
dt=0.05
k=2
Force=[0,0,0]
while t<10**10:
    rate(1000)
   
    for i in range(3):
        if i==0:
            Force[i]=(k*(Balls[i+1].pos-2*Balls[i].pos))
        if i==2:
            Force[i]=(k*(Balls[i-1].pos-2*Balls[i].pos+vector(8,0,0)))
        if i==1 :
            Force[i]=(k*(Balls[i-1].pos+Balls[i+1].pos-2*Balls[i].pos))
    for i in range(3):
        Balls[i].a=Force[i]/Balls[i].weight
        Balls[i].vel=Balls[i].vel+Balls[i].a*dt
        Balls[i].pos=Balls[i].pos+Balls[i].vel*dt
    
        if i==0:
            Helixes[i].axis=Balls[i].pos
        if i+1==3:
            Helixes[i+1].axis=vector(8,0,0)-Balls[i].pos
            Helixes[i+1].pos=Balls[i].pos
        if i==1 or i==2:
            Helixes[i].axis=Balls[i].pos-Balls[i-1].pos
            Helixes[i].pos= Balls[i-1].pos
    t+=dt

ll = label(pos=(0,20,0), text='',color=color.cyan, height=20, linecolor=color.green)

while 1:
    rate(1000)
    Ekin=0
    Epot=0
    for i in range(3):
        Ekin+=Balls[i].weight*(Balls[i].vel**2)/2
    for i in range(4):
        Epot+=Helixes[i].axis**2*k/2
    ll.text='Ekin= '+'%.4f'%(Ekin)+'\n'+\
            'Epot= '+'%.4f'%(Epot)+'\n'+\
            'Etotal= '+'%.4f'%(Ekin+Epot)