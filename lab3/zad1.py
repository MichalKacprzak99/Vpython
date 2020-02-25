import math
import random
import time
def draw(distanceright,distanceleft):
    print('|', end =" ")
    print(" "*(distanceleft),end =" ")
    print('*', end =" ")
    print(" "*(distanceright),end =" ")
    print('|', end =" ")

n=15
position=0
distanceleft=n-1
distanceright=n-1
list=[1,-1]
flipsofcoin=0

print(" "*8,"START")

while abs(position)!=n:
    
    draw(distanceright,distanceleft)

    if position>0:
        print("+",abs(position))
    else:
        print("-",abs(position))

    time.sleep(0.01)
    x=random.choice(list)
    flipsofcoin+=1
    position+=x
    distanceleft+=x
    distanceright-=x

if position==-n:
    print('*', " "*(2*n+1),"|","-",abs(position))
else:
    print("|", " "*(2*n+1),'*',"+",abs(position))


print("coin was flipped:",flipsofcoin )