#inverted pyramid with digits in ascending order in every row
n=int(input("enter n:- "))
for i in range(n): # i = 0,1,2,.....
    print(' '*i,end="")
    for j in range(n-i):# j runs n , n-1,n-2....times
        print(j+1,end=" ") #prints 1,2,3.....
    print()