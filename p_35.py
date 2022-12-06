#pyramid with alphabets in reverse of dictionary order in every row
n=int(input("enter n:- "))
for i in range(n):
    print(' '*(n-i-1),end="")  #end="" no space in the same line
    for j in range(i+1):
        print(chr(65+(n-j-1)),end=' ') # consecutive no.  symbol = j+1
    print()