s1=input()
s=list(s1)
if len(s)%2==0:
    s[0],s[-1]=s[-1],s[0]
    print(str(s))
else:
    print(s1+s1[::-1])