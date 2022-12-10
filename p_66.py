#half hallow diamond with fixed alphabet in every row
n=int(input("enter n :- "))
for i in range(n):
    print("  "*(n-i-1)+(chr(65+i)+" "),end="")
    if i >= 1:
        print("  "*(2*i-1)+(chr(65+i)+" "),end="")
    print()