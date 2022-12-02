#reverse square n n n...
n=int(input("enter n :- "))
for i in range(n):
    for j in range(n):
        print(n-i,end=" ")
    print()
for i in range(n):
    print((str(n-i)+" ")*n)
    #output
    # 3 3 3
    # 2 2 2
    # 1 1 1