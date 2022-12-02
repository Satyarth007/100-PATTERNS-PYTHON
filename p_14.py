# right angle triangle with numbers
n = int(input("enter n:- "))
# 1st way :-
for i in range(n):
    for j in range(i+1):
        print(str(i+1),end=" ")
    print()
#===============================================
# 2nd way :-
for i in range(n):
    print((str(i+1)+" ")*(i+1))