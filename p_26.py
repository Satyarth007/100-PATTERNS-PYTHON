#inverted rt with alphabet in dictionary order in every row
n=int(input("enter n:- "))

for i in range(n):
    for j in range(n-i):
        print(chr(65+j),end=" ")  # j = 0,1,2,3,4
    print()