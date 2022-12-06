# Diamond pattern with * symbol
n=int(input("enter n:- "))
for i in range(n):
    print(" "*(n-i-1)+"* "*(i+1))
for i in range(n-1):
    print(" "*(i+1)+"* "*(n-i-1))

    # to make diamond we need to run two for loops
    # first loop till n times and second one upto n-1