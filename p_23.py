#inverted rt with fixed digit in every row
n=int(input("enter n:- "))

# 1st approach:-
for i in range(n):
    for j in range(n-i):
        print(str(n-i),end=" ")  # i = 0,1,2,3,4
    print()

# 2nd approach:-
for i in range(n):
    print((str(n-i)+" ")*(n-i))