def product(s,n,arr):
    if n<2:
        return -1
    fmin=smin=float('inf')
    for i in range(n):
        if arr[i]<fmin:
            smin=fmin
            fmin=arr[i]
        elif arr[i]<smin and arr[i]!=fmin:
            smin=arr[i]
    if fmin+smin<=s:
        return fmin*smin
    else:
        return 0
s=int(input())
n=int(input())
a=list(map(int,input().split()))
print(product(s,n,a))