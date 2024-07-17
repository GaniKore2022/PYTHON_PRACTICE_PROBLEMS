n=5
for i in range(n+1):
    for j in range(n-i):
        print(" ",end=" ")
    x=1
    for k in range(1,i+1):
        print(x," ",sep=' ',end=" ")
        x=x*(i-k)//k
    print()
