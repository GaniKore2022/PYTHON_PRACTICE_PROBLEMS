n=6
for i in range(1,n):
    for j in range(n-i-1):
        print(" ",end=" ")
    for k in range(2*i-1):
        print("*",end=" ")
    print()
for i in range(4,0,-1):
    for j in range(n-i-1):
        print(" ",end=" ")
    for k in range(2*i-1):
        print("*",end=" ")
    print()