#inverted rt pattern with fixd alphabet symbol in every row
n=int(input("enter n:- "))

# 1st approach:-
for i in range(n):
    for j in range(n-i): #j will run  5,4,3,2,1 times
        print(chr(65+i),end=" ")  # i = 0,1,2,3,4
    print()

# 2nd approach:-
for i in range(n):
    print((chr(65+i)+" ")*(n-i))