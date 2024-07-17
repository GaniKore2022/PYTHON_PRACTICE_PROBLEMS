l=list(map(int,input().split()))
ms=cs=l[0]
for i in range(1,len(l)):
    cs+=l[i]
    if cs>ms:
        ms=cs
    if cs<0:
        cs=0
print(ms)