#inverted pyramid with alphabets in dictiionary order in every roe
n=int(input("enter n:- "))
for i in range(n): # i = 0,1,2,.....
    print(' '*i,end="")
    for j in range(n-i):
        print(chr(65+j),end=" ")
    print()