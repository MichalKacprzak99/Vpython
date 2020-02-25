import random
import math
trafione = 0
proby = 10**6
f = open('zad1', 'w')
for i in range(1,proby+1):
    x = random.uniform(-1,1)
    y = random.uniform(-1,1)
    if x**2+y**2<=1:
        trafione+=1
        pi = 4*trafione/i
        if i<=100 or i==10**2 or i==10**3 or i==10**4 or i==10**5 or i==10**6:
            f.write(str(i)+') '+str(pi)+' '+str(pi/math.pi)+'\n')
    else:
        pi = 4*trafione/i
        if i<=100 or i==10**2 or i==10**4 or i==10**5 or i==10**6:
            f.write(str(i)+') '+str(pi)+' '+str(pi/math.pi)+'\n')
f.close()