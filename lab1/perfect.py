for num in range(1, 10001):
    if sum(x for x in range (1,num) if num%x == 0) == num:
        print (num)
