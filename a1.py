n=int(input("enter a number "))
rev=0
while n>0:
    digt=n%10
    rev=rev*10+digt
    n=n//10
print("reverse number is",rev)