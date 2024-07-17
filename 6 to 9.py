l=list(map(int,input().split()))
s=sum(l)
x=s
if 6 in l and 9 in l:
    p=l.index(6)
    q=l.index(9)
    for i in range(p,q+1):
        s-=l[i]
    print(s)
elif 6 in l and 9 not in l:
    print(s-6)
else:
    print(x)