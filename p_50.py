#right half diamond pattern with * symbols
n=int(input("enter n:- "))
for i in range(n): 
    print("* "*(i+1))
for i in range(n-1):
    print("* "*(n-i-1))