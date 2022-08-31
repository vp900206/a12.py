n=int(input("Enter a number to check prime or not "))
if n<2:
    print("Not a prime number ")
else:
    for e in range(2,n):
        if n%e==0:
            print("Not a prime number ")
            break
    else:
        print("Prime number ")
