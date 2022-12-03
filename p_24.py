#inverted rt with fixed alphabet in every row in reverse dictionary order
n=int(input("enter n:- "))

# 1st approach:-
for i in range(n):
    for j in range(n-i):
        print(chr(65+n-i-1),end=" ")  # i = 0,1,2,3,4
    print()

# 2nd approach:-
for i in range(n):
    print((chr(65+n-i-1)+" ")*(n-i))  # ..E D C B A