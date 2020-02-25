import math

f = open('zad3', 'w')

x = [ i*2*math.pi/50 for i in range(0,51) ]
for i in x:
    y = int(50*math.sin(i))
    if y==0:
        f.write('0'+'\n')
    elif y>0:
        f.write('+'*y+'\n')
    else:
        f.write('-'*(-y)+'\n')
f.close()