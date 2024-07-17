a=list(map(int,input().split()))
x=int(input())
flag=0
for i in range(len(a)):
    for j in range(i+1, len(a)):
        if a[i]+a[j]==x:
            flag=1
            k1,k2=a[i],a[j]
if flag==1:
    print("Yes")
    print("The solution is:",k1," ",k2)
else:
    print("No")