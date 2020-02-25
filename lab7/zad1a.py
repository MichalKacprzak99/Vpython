import random
import matplotlib.pyplot as plt
plt.style.use('classic')


list=[1,-1]
c=['b','g','r','c','m','y','k','orange','pink','cyan','purple','gray','lawngreen','salmon','gold']
n=10**5

for j in range(15):
    position=0
    X=[]
    Y=[]
    for i in range(n):
        x=random.choice(list)
        position+=x
        X.append(i)
        Y.append(position)
    plt.plot(X,Y,color=c[j])
plt.show()