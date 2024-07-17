L=[]
s=0
n=int(input())
for i in range(n):
    x=int(input())
    s=s+x
    L.append(x)
print(L)
print(s)
if(s%2==0 and s%5==0):
    print("Yes,Sum is divisible by 2 and 5")
else:
    print("No,Sum is not divisible by 2 and 5")
