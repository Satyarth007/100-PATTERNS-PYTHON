#to print inverted pyramid
n=int(input("enter n:- "))
for i in range(n): # i = 0,1,2,.....
    print(' '*i + "* "*(n-i) )
    # no. of space in every row = i
    # no. of stars in every row = n-i