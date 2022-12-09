#left half diamond with digits in descending order in every row
n= int(input('enter n :- '))
for i in range(n):
    print('  '*(n-i-1),end="")
    for j in range(i+1):
        print(str(n-j),end=" ")
    print()

for i in range(n-1):
    print('  '*(i+1),end="")
    for j in range(n-1-i):
        print(str(n-j),end=" ")
    print()