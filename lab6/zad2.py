import random
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('classic')

x0=0
y0=0
X=[]
Y=[]
X.append(x0)
Y.append(y0)

sum=0
tmp=0
i=1

while(sum<10**6):
    
    r = random.uniform(0, 100)
    if r < 1.0:
        x = 0
        y = 0.16*y0
    elif r < 86.0:
        x = 0.85*x0 + 0.04*y0
        y = -0.04*x0 + 0.85*y0+1.6
    elif r < 93.0:
        x = 0.2*x0 - 0.26*y0
        y = 0.23*x0 + 0.22*y0 + 1.6
    else:
        x = -0.15*x0 + 0.28*y0
        y = 0.26*x0 + 0.24*y0+ 0.44
    x0 = x
    y0 = y
    if 1 <= x0 <= 1.3 and 2.5 <= y0 <= 3.1:

        sum+=1
        tmp+=1
            
        if tmp==i*10**4:
            print(tmp)
            tmp=0
            i+=1
        
        X.append(x);Y.append(y)
    
     
plt.axis([1,1.3,2.5,3.1])
plt.plot(X,Y,',',color ='blue')
ax=plt.gca()
ax.set_facecolor("black")
plt.show()