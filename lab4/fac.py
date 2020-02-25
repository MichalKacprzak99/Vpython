import math
def factorial(n):
    
        if(n==1):
            return 1
        elif(n==1/2):
            return math.sqrt(math.pi)/2
        else:
            return n*factorial(n-1)