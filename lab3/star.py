import math
import random
import time
def draw(distaceright,distanceleft):
    print('|', end =" ")
    for i in range(0,distanceleft):
        print(end =" ")
    print('*', end =" ")
    for i in range(0,distaceright):
        print(end =" ")
    print('|', end =" ")
n=10
position=0
distanceleft=n-1
distaceright=n-1
list=[1,-1]
flipsofcoin=0
print(" "*8,"START")
while abs(position)!=n:
    
    draw(distaceright,distanceleft)

    if position>0:
        print("+",abs(position))
    else:
        print("-",abs(position))

    time.sleep(0.1)
    x=random.choice(list)
    flipsofcoin+=1
    position+=x
    distanceleft+=x
    distaceright-=x
if position==-10:
    print('*', " "*(2*n-1),"|","-",abs(position))
else:
    print("|", " "*(2*n-1),'*',"+",abs(position))


print("coin was flipped:",flipsofcoin )