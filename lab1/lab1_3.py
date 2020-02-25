def odd_or_even(b):
    while b != 'the end':
        if int(b)%2==0:
            print("That is an even number")
        else:
            print("That is odd number")
        b = input("Please")

b=input("Please insert a number: ")
odd_or_even(b)
