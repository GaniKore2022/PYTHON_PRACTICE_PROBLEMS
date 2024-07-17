def largesmallsum(arr):
    if len(arr)<=3:
        return 0
    fmax=smax=float('-inf')
    fmin=smin=float('inf')
    for i in range(len(arr)):
        if i%2==0:
            if arr[i]>fmax:
                smax=fmax
                fmax=arr[i]
            elif arr[i]>smax and arr[i]!=fmax:
                smax=arr[i]
        else:
            if arr[i]<fmin:
                smin=fmin
                fmin=arr[i]
            elif arr[i]<smin and arr[i]!=fmin:
                smin=arr[i]
    return smax+smin
arr=list(map(int,input().split()))
print(largesmallsum(arr))