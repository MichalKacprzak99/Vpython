import random
import matplotlib.pyplot as plt
plt.style.use('classic')

X = [0]
Y = [0]

for n in range(1,10**6+1):
    r = random.uniform(0, 100)
    if r < 1.0:
        x = 0
        y = 0.16*Y[n-1]
    elif r < 86.0:
        x = 0.85*X[n-1] + 0.04*Y[n-1]
        y = -0.04*X[n-1] + 0.85*Y[n-1]+1.6
    elif r < 93.0:
        x = 0.2*X[n-1] - 0.26*Y[n-1]
        y = 0.23*X[n-1] + 0.22*Y[n-1] + 1.6
    else:
        x = -0.15*X[n-1] + 0.28*Y[n-1]
        y = 0.26*X[n-1] + 0.24*Y[n-1] + 0.44
    X.append(x);Y.append(y)

plt.plot(X,Y,',',color ='blue')

#my finger
A1=[1,1.3]
A2=[2.5,2.5]
A3=[3.1,3.1]
B1=[2.5,3.1]
B2=[1,1]
B3=[1.3,1.3]
plt.plot(A1,A2,'-',color='red')
plt.plot(A1,A3,'-',color='red')
plt.plot(B2,B1,'-',color='red')
plt.plot(B3,B1,'-',color='red')

ax=plt.gca()
ax.set_facecolor("black")

plt.show()