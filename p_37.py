#inverted pyramid with fixed digit
n=int(input("enter n:- "))
for i in range(n): # i = 0,1,2,.....
    print(' '*i + (str(i+1)+" ")*(n-i) )