import numpy
import random
import math
how_many_with_the_same_birthday_at_least=2
for i in range(1,366):

    how_many_times_it_happened=0
    rooms=numpy.random.randint(100,1000)
    osoby=numpy.random.randint(1,366,(rooms,i))

    for j in osoby:
        tmp1=j
        tmp2=j

        tmp2=tmp2[:,numpy.newaxis]

        same_birthday=(tmp1==tmp2)#rray of bool
       
        #same_birthday=1*same_birthday#from bool to 0/1

        for k in same_birthday:
            if(k.sum()>=how_many_with_the_same_birthday_at_least):
                how_many_times_it_happened+=1
                break

    probability=how_many_times_it_happened/rooms

    print("probability for",i,"people:",probability)