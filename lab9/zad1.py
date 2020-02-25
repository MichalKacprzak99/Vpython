from vpython import *
scene=canvas()
G = 6.67*10**(-11)
Weight_of_Sun = 2*10**30
rad=10**10

Distance_from_sun=[vector(70*10**9,0,0),vector(110*10**9,0,0),vector(150*10**9,0,0),vector(250*10**9,0,0)]
V=[vector(0,47000,0),vector(0,35000,0),vector(0,30000,0),vector(0,24000,0)]

Sun=sphere(pos=vector(0,0,0),color = color.yellow, radius =3.5*rad )

Planets=[]
Planets.append(sphere(pos=Distance_from_sun[0],radius=rad, vel=V[0] , color=color.white, make_trail=True))
Planets.append(sphere(pos=Distance_from_sun[1],radius=rad, vel=V[1] , color=color.magenta,make_trail=True))
Planets.append(sphere(pos=Distance_from_sun[2],radius=rad, vel=V[2] , texture=textures.earth, make_trail=True))
Planets.append(sphere(pos=Distance_from_sun[3],radius=rad, vel=V[3] , color=color.red, make_trail=True))

t=0
#dt=1000
dt=3600
t_end=60*60*24*365
while t<=t_end:
    rate(1000)
    #rate(30)
    for planet in Planets:
        a = -G * Weight_of_Sun * planet.pos / ((mag(planet.pos)) ** 3)
        planet.vel += a * dt
        planet.pos += planet.vel * dt
    t = t + dt
