#bottom half hollow diamond with no. in ascending order
n=int(input("enter n:- "))
for i in range(n): # i =0,1,2,3,..........
    print("  "*i + (str(i+1)+" "),end="")
    if i!=n-1:
        print("  "*(2*n-2*i-3)+(str(i+1)+" "))
