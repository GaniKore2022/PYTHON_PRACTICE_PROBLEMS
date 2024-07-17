n=5
for i in range(1,n+1):
    for k in range(n,i,-1):
        print(" ",end=" ")
    for j in range(1,i+1):
        print(j,end=" ")
    for l in range(i-1,0,-1):
        print(l,end=" ")
    print()
print("******************************")
n1=5
num=1
i=1
while(i<=n1):
    j=1
    while(j<=i):
        print(num,end=" ")
        num=num+1
        j=j+1
    i=i+1
    print()
