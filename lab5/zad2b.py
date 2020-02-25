import numpy
import random

number_of_rooms=500
how_many_with_the_same_birthday_at_least=4#any number
f = open('zad1', 'w')
flag=0
for i in range(1,367):
    how_many_times_it_happened=0
    rooms=numpy.random.randint(1,366,(number_of_rooms,i))
    for room in rooms:

        tmp1=room
        tmp2=room

        tmp2=tmp2[:,numpy.newaxis]

        same_birthday=(tmp1==tmp2)

        for k in same_birthday:
            if(k.sum()>=how_many_with_the_same_birthday_at_least):
                how_many_times_it_happened+=1
                break

    probability=how_many_times_it_happened/number_of_rooms
    f.write( "probability for "+str(i)+" people: "+str(probability) +'\n')
    if probability>0.50 and flag==0:
        f.write("For "+str(i)+" people we get probability greater than 50%"+'\n')
        flag=1