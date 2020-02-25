def sum_list(L1):
    """Sum of elements in list"""
    i=0
    sum=0
    while i<len(L1):
        sum+=L1[i]
        i+=1
    print(sum)
    
L=[1,2,3]
sum_list(L)