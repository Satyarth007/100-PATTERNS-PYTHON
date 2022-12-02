# square with decreasing alphabets
n=int(input("enter n :- "))
for i in range(n):
    print((chr(65+(n-i-1))+" ")*n)