
import numpy
import random

for i in range(1,366):
    
    probability=0
    sala=numpy.random.randint(100,1000)
    osoby=numpy.random.randint(1,366,(sala,i))
    #print(osoby)
    for j in osoby:
        tmp1=j
        tmp2=j

        tmp2=tmp2[:,numpy.newaxis]

        same_birthday=(tmp1==tmp2)
           
        if( ( ( same_birthday.sum()-i ) / 2 ) >0):
            probability+=1
        
    print("probability for",i,"people:",probability/sala)

