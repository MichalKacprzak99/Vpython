import fac
import math
import random
n=5 
hits=10**6


for i in range(2,n+1):
    number_of_hits=0
    
    for j in range(0,hits):
        sum=0
        for k in range(0,i):
            point=random.uniform(-1,1)
            sum+=point**2
        if sum<1:
            number_of_hits+=1
    
    v_cal=((2**i)*number_of_hits)/hits
    v_math=((math.pi)**(i/2))/fac.factorial(i/2)
    print(i,')',"calculate: ",v_cal,"is good? :",v_cal/v_math,"number of hits:",number_of_hits)