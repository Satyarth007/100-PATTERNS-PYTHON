# square with decreasing alphabets D C B A
n = int(input("enter n:- "))
for i in range(n):
    for j in range(n):
        print(chr(65+(n-j-1)),end=" ")
    print()