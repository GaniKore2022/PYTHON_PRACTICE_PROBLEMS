s1=input()
s2=input()
d={}
l=[]
flag=0
for i in s1:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
for i in s2:
    if i in d.keys():
        l.append(i)
        flag=1
if flag==1:
    print("Yes and the letters are:",*l)
else:
    print("No")