def is_prime(number):
    if number>2:
        for i in range(2,(number//2)+1):
            if( number%i )==0:
                return 0
        else:
            return 1
    else:
        return 0
    



def is_even_odd_prime(num):
    if num%2 == 0 :
        print("even")
    if num%2 == 1 :
       print("odd")
    if is_prime(num)==1:
        print("prime")

a=int(input("Write down a number: "))
is_even_odd_prime(a)