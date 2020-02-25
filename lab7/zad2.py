import random
import matplotlib.pyplot as plt
import math
from math import sqrt
plt.style.use('classic')

flipsofcoin=[10,100,400,2500,10**4]
number_of_attemps=500
list=[1,-1]
sigma=[]
for j in range(len(flipsofcoin)):
    
    sum_of_distance=0
    for i in range(number_of_attemps):
        distance=0
        for k in range(flipsofcoin[j]):
            x=random.choice(list)
            distance+=x
        sum_of_distance+=(distance**2)
    sum_of_distance=sqrt(sum_of_distance/number_of_attemps)
    sigma.append(sum_of_distance)

plt.plot(flipsofcoin,sigma,'.',color='lime',ms=20)

X=[]
Y=[]
for i in range(flipsofcoin[4]):
    X.append(i)
    Y.append(sqrt(i))
plt.plot(X,Y,color='deeppink')

ax=plt.gca()
ax.set_facecolor("black")
plt.show()