def diffofsum(n,m):
    d=0
    nd=0
    for i in range(1,m+1):
        if i%n==0:
            d+=i
        else:
            nd+=i
    return abs(d-nd)
n=int(input())
m=int(input())
print(diffofsum(n,m))