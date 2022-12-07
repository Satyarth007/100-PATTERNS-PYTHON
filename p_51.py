#right half dimond with fixed digit in every row
n=int(input("enter n:- "))
for i in range(n):
    print((str(i+1)+" ")*(i+1))
for i in range(n-1):
    print((str(n-i-1)+" ")*(n-i-1))