# INVERTED RIGHT TRIANGLE PATTERN WITH * SYMBOL
n=int(input("enter n:- "))

# 1st approach:-
for i in range(n):
    for j in range(n-i):
        print("*",end=" ");
    print()

# 2nd approach:-
for i in range(n):
    print("* "*(n-i))