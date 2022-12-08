#right half diamind with alphabets in reverse of dictionru order in every row
n=int(input("enter n:- "))
for i in range(n):
       for j in range(i+1):
           print(chr(65+n-j-1),end=" ")
       print()
for i in range(n-1):
    for j in range(n-i-1):
        print(chr(65+n-j-1),end=" ")
    print()