#pyramid with digits in descending order in every row
n=int(input("enter n:- "))
for i in range(n):
    print(' '*(n-i-1),end="")  #end="" no space in the same line
    for j in range(i+1):
        print(n-j,end=' ') # consecutive no.  symbol = j+1
    print()