n=5
for i in range(1,n+1):
    for j in range(0,i+1):
        print(" ",end="")
    for j in range(2*(n-i)+1):
        print("*",end="")
    print()
