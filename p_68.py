# hallow half diamond with alphabets in reverse of dictionary order
n=int(input("enter n :- "))
for i in range(n):
    print("  "*(n-i-1)+(chr(65+n-1-i)+" "),end="")
    if i >= 1:
        print("  "*(2*i-1)+(chr(65+n-1-i)+" "),end="")
    print()