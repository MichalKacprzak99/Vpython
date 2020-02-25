from vpython import *

scene=canvas()
rad=10**10
G = 6.67*10**(-11)
Weight_of_Sun = 2*10**30
Weight_of_Earth = 6*10**24

Distance_from_sun=[vector(70*10**9,0,0),vector(110*10**9,0,0),vector(250*10**9,0,0)]
Distance_beetwen_Sun_Earth=vector(150*10**9,0,0)
V=[vector(0,47000,0),vector(0,35000,0),vector(0,24000,0)]

Earth=sphere(pos=vector(0,0,0),texture=textures.earth, radius =rad)
Sun=sphere(pos=-Distance_beetwen_Sun_Earth,color = color.yellow, radius =3.5*rad ,vel=-vector(0,30000,0),make_trail=True)

Planets=[]
Planets.append(sphere(pos=(Distance_from_sun[0]+Sun.pos) ,radius=10**10, vel=V[0]+Sun.vel , color=color.white, make_trail=True))
Planets.append(sphere(pos=(Distance_from_sun[1]+Sun.pos) ,radius=10**10, vel=V[1]+Sun.vel , color=color.orange,make_trail=True))
Planets.append(sphere(pos=(Distance_from_sun[2]+Sun.pos),radius=10**10, vel=V[2]+Sun.vel , color=color.red, make_trail=True))

t=0
dt=1000

while t<10**10:
    
    rate(5000)

    Sun.a=-G * Weight_of_Sun * (Sun.pos) / ((mag(Sun.pos)) ** 3)
    Sun.vel += Sun.a * dt
    Sun.pos = Sun.pos + Sun.vel * dt
    
    for planet in Planets:   
        planet.a = Sun.a +( planet.pos-Sun.pos) * (- G * Weight_of_Sun / (mag(Sun.pos-planet.pos)**3 ) )
        planet.vel += planet.a * dt
        planet.pos += planet.vel * dt
    t = t + dt