#inverted pyramid with reverse dictionary order in very row
n=int(input("enter n:- "))
for i in range(n): # i = 0,1,2,.....
    print(' '*i,end="")
    for j in range(n-i):
        print(chr(65+n-j-1),end=" ")
    print()