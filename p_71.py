#bottom half hollow diamond pattern with fixed alphabets symbols
n=int(input("enter n:- "))
for i in range(n): # i =0,1,2,3,..........
    print("  "*i + (chr(65+(n-1)-i)+" "),end="")
    if i!=n-1:
        print("  "*(2*n-2*i-3)+(chr(65+n-1-i)+" "))
