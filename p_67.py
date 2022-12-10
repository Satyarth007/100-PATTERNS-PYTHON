#half hallow diamond with numbers in descening order
n=int(input("enter n :- "))
for i in range(n):
    print("  "*(n-i-1)+(str(n-i)+" "),end="")
    if i >= 1:
        print("  "*(2*i-1)+(str(n-i)+" "),end="")
    print()