import numpy as np
import math
import random
import matplotlib.pyplot as plt

n=15
c=['b','g','r','c','m','y','k','orange','pink','cyan','purple','gray','lawngreen','salmon','gold']
for j in range(n):
    a=np.random.uniform(0,2*np.pi,10**5)
    X=[0]
    Y=[0]
    x=0
    y=0
    for i in a:
        x+=np.cos(i)
        y+=np.sin(i)
        X.append(x)
        Y.append(y)

    plt.plot(y,x,'o',color=c[j],ms=20)
    plt.plot(Y,X,lw=0.1,color=c[j])

plt.show()