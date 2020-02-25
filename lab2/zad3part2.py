import math

f = open('zad3_part2', 'w')

tablica_2d = [[' ' for x in range(0,51)] for x in range(0,97)]

x = [ i*2*math.pi/50 for i in range(0,51) ]
for j in range(0,51):
    y = int(50*math.sin(x[j]))
    if y==0:
        tablica_2d[48+y][j] = 0
        
    elif y>0:
        for ilosc in range(0,y):
            tablica_2d[48-ilosc][j] = '+'
    else:
        for ilosc in range(0,-y):
            tablica_2d[48+ilosc][j] = '-'

for i in range(0,97):
    for j in range(0,51):
        f.write(str(tablica_2d[i][j])+' ')
    f.write('\n')
    
f.close()