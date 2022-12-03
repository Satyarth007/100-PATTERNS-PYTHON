#right angle traingle pattern with digits in ascending order in every row
n=int(input("enter n :- "))
for i in range(n):
    for j in range(i+1):
        print(str(j+1),end=" ")
    print()