size=int(input())
x=[]
def fun():
    global p
    p=1
    for i in range(0,size):
        y=int(input())
        x.append(y)
    for i in x:
        p=p*i
fun()
if(p<750):
    print("Product is ",p)
else:
    print("Sum is ",sum(x))
print("**************************")
awdsssn=int(input())
def table():
    for i in range(1,11):
        print("{} * {} = {}".format(n,i,n*i))
table()
print("**************************")
n=int(input())
def prime():
    global c
    c=0
    for i in range(1,n+1):
        if int(n%i)==0:
            c=c+1
prime()
if(c==2):
    print("Prime")
else:
    print("Not prime")
print("**************************")
def rainbow():
    c=input()
    if (c in "VIBGYOR" or c in "vibgyor"):
        print("VIBGYOR")
    else:
        print("Enter rainbow chars")
        rainbow()
rainbow()
print("**************************")
a=int(input())
def hl():
    if(a<999):
        return "Lowest"
    else:
        return "Highest"
print(hl())    
