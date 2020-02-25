def product_list(L1):
    """Product of elements in list"""
    i=0
    product=1
    while i<len(L1):
        product*=L1[i]
        i+=1
    print(product)
    
L=[1,2,10]
product_list(L)