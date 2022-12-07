#diamond pattern with digits in descending order in every row
n=int(input("enter n:- "))
for i in range(n):
    print(" "*(n-i-1),end="")
    for j in range(i+1):
        print((str(n-j)+" "),end="")
    print()

for i in range(n-1): # 0,1,2..
    print(" "*(i+1),end="")
    for j in range(n-i-1):
        print((str(n-j)+" "),end="")
    print()