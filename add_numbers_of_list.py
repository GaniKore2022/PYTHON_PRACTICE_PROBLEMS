l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
n=len(l1)
for i in range(n):
    l1[i]=l1[i]+l2[i]
l=[]
c=0
for i in range(n-1,-1,-1):
    if c==1:
        l1[i]=l1[i]+c
        c=0
    if l1[i]<10:
        l.insert(0,l1[i])
    else:
        r=l1[i]%10
        if r>=0:
            l.insert(0,r)
            c=1
if c==1:
    l.insert(0,c)
print(l)