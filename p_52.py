#right half diamond with fixed alphabet
n=int(input("enter n:- "))
for i in range(n):
    print((chr(65+i)+" ")*(i+1))
for i in range(n-1):
    print((chr(65+(n-1)-i-1)+" ")*(n-i-1))