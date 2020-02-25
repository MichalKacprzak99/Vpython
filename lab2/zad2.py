import math

result=0.0
proby = 10**7
f = open('zad2', 'w')
for i in range(1,proby+1):
    result += 4* (-1.0)**(i-1)/(2.0*(i-1)+1.0)
    if i<=100 or i==10**2 or i==10**3 or i==10**4 or i==10**5 or i==10**6 or i==10**7:
            f.write(str(i)+') '+str(result)+' '+str(result/math.pi)+'\n')
f.close()