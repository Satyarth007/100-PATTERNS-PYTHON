#inverted rt with alpha in reverse of dictionary order in every row
n=int(input("enter n:- "))

for i in range(n):
    for j in range(n-i):
        print(chr(65+n-j-1),end=" ")  # j = 0,1,2,3,4
    print()