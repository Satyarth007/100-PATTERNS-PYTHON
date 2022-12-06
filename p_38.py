#inverted pyramid with fixed alphabet
n=int(input("enter n:- "))
for i in range(n): # i = 0,1,2,.....
    print(' '*i + (chr(65+i)+" ")*(n-i) )