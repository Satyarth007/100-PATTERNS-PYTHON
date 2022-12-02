# square with A B C ......
n=int(input("enter n :- "))
for i in range(n):
    for j in range(n):
        print(chr(65+j),end=" ")
    print()

    # output:-
    # enter n :- 4
    # A B C D
    # A B C D
    # A B C D
    # A B C D