import math
import random
import time

experiment=10000
N=[5,10,15,20,30,50]
position=0
average=[]
list=[1,-1]
flipsofcoin=0
allflips=0
for n in N:
    for i in range(0,experiment):
        distanceleft=n-1
        distanceright=n-1
        while abs(position)!=n:
            x=random.choice(list)
            flipsofcoin+=1
            position+=x
        allflips+=flipsofcoin
    average.append(allflips/experiment)
print(average)
