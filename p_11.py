#square with 5 4 3 2 1
n=int(input("enter n :- "))
for i in range(n):
    for j in range(n,0,-1):
        print(j,end=" ")
    print()

for i in range(n):
    for j in range(n):
        print(n-j,end=" ")
    print()
