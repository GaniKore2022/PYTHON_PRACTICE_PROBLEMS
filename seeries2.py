n=int(input())
s=0.0
for i in range(1,n+1):
    a=float(i)/(i+1)
    s += a
print(s)
print("*****************************")
n1=int(input())
s1=0
while(n1>=0):
    print(n1,end=" ")
    n1 -= 1
print("**************")
#write a program to take a 3 digit input let n=123 print a number in reversee order
n2=int(input())
s2=0
while(n2!=0):
    r=n2%10
    print(r,end="")
    n2=n2//10
print("**************")
#armstrong
n3=int(input())
s2=0
x=n3
c=1
y=n3
while(1):
    n3=n3//10
    if(n3!=0):
        c +=1
    else:
        break
while(y!=0):
    r=(y%10)**c
    s2 += r
    y=y//10
if x==s2:
    print("Armstrong")
else:
    print("Not armstrong")
