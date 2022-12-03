#right triangle with alphbet symbols in reverse of dictionary order in every row
n=int(input("enter n :- "))
for i in range(n):
    for j in range(i+1):
        print(chr(65+n-j-1),end=" ")
    print()