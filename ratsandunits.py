def rats(req,n,arr):
    if n==0:
        return -1
    req=r*unit
    s=0
    c=0
    for i in range(n):
        if s>=req:
            break
        s+=arr[i]
        c+=1
    if s<req:
        return 0
    else:
        return c
r,unit=map(int,input().split())
n=int(input())
arr=list(map(int,input().split()))
req=r*unit
print(rats(req,n,arr))