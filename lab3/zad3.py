import random 
x=random.randint(0,20)
#print("szukana liczba to:",x)
a=int(input("Write down a number: "))

while x!=a:
    if(x<a):
        print("musisz podac mniejsza zeby zgadnac")
    if(x>a):
        print("musisz podac wieksza zeby zgadnac")
    a=int(input("Write down a number: "))

print("zgadles")