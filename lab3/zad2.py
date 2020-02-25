import math
L=[]
for n in range(2,7):
    for a in range(1,101):
        for b in range(a,101):
            c=(a**n+b**n)**(1/n)
            if int(c)==c:
                tmp=[a,b,int(c)]
                L.append(tmp)
                #print("a=",a," ","b=",b," ","c=",c," ",)
for i in L:
    print(i)