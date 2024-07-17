B=[10,20,10,20,30]
d={}
for i in B:
    if i in d:
        d[i]=d[i]+1
    else:
        d[i]=1
for i in d.keys():
    print(i,"Count:",d[i])