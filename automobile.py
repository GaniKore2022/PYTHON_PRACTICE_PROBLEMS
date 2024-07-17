v=int(input())
w=int(input())
if not v<w and w%2==0:
    print("Invalid Input")
else:
    x=((4*v)-w)//2
    print(x)
    print(v-x)
