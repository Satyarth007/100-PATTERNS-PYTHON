#diamond with fixed alphabet in every row
n=int(input("enter n:- "))
for i in range(n):
    print(" "*(n-i-1)+(chr(65+i)+" ")*(i+1))
for i in range(n-1):
    print(" "*(i+1)+(chr(65+(n-1)-i-1)+" ")*(n-i-1))