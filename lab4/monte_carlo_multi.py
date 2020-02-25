import fac
import math
import numpy
n=20
hits=10**6

for i in range(2,n+1):
    tab=numpy.random.uniform(-1,1,(hits,i))
    
    tab=tab**2
    tmp=tab.sum(axis=1)
   
    if_hit=(tmp<1)
    if_not=(tmp>=1)
    
    tmp[if_hit]=1
    tmp[if_not]=0
    
    number_of_hits=tmp.sum()
    
    v_cal=((2**i)*number_of_hits)/hits
    v_math=((math.pi)**(i/2))/fac.factorial(i/2)
    print(i,')',"calculate: ",v_cal,"is good? :",v_cal/v_math,"number of hits:",number_of_hits)
