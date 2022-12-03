#right angle triangle pattern with digits in descending order in eery row
n=int(input("enter n :- "))
for i in range(n):
    for j in range(i+1):
        print(str(n-j),end=" ")
    print()