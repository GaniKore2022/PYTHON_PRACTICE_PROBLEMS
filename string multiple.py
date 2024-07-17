s=input()
count={}
for i in s:
    if i in count:
        count[i]+=1
    else:
        count[i]=1
for j,c in count.items():
    print(j,c,end=" ")
print("*******************")
s1=input()
s2=input()
if (s2.isupper()):
    s1=s1.replace(s2,chr(ord(s2)+32))
else:
    s1=s1.replace(s2,chr(ord(s2)-32))
print(s1)
