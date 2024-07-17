arr=list(map(int,input().split()))
cs=ms=arr[0]
for i in range(1,len(arr)):
    if cs<0:
        cs=0
    cs+=arr[i]
    if cs>ms:
        ms=cs
print(ms)