#lefthalf diamond with alphabets in reverse of dictionary order in every row
n= int(input('enter n :- '))
for i in range(n):
    print('  '*(n-i-1),end="")
    for j in range(i+1):
        print(chr(65+n-1-j),end=" ")
    print()

for i in range(n-1):
    print('  '*(i+1),end="")
    for j in range(n-1-i):
        print(chr(65+n-1-j),end=" ")
    print()