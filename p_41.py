#inverted pyramd with digits in descending order in every row
n=int(input("enter n:- "))
for i in range(n): # i = 0,1,2,.....
    print(' '*i,end="")
    for j in range(n-i):
        print(n-j,end=" ")
    print()