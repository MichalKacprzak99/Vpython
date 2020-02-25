L=[]
for n in range(2,7):
    print(n)
    for a in range(1,100):
        for b in range(1,100):
            for c in range(1,100):
                if(a**n+b**n==c**n):
                    tmp=[a,b,c]
                    L.append(tmp)
                    print("a=",a," ","b=",b," ","c=",c," ",)
    #for i in L:
     #   print(i)