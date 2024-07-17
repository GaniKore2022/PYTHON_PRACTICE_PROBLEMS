a=12.4
if(a is int):
    print("Integer")
else:
    print("Float")
print("***************")
p=int(input())
q=int(input())
r=int(input())
if(p<q):
    if(q<r):
        print("{} is greater".format(r))
    else:
        print("{} is greater".format(q))
else:
    print("{} is greater".format(p))
print("***************")
x=int(input())
while(x!=0):
    y=int(x%10)
    x=int(x/10)
    print(y)
print("***************") 
