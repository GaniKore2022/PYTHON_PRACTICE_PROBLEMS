l=list(map(int,input().split()))
m=c=l[0]
for i in range(1,len(l)):
    if c>m:
        m=c
    c=l[i]
print(m)