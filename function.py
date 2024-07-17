def fun():
    x=int(input("Enter number:"))
    if(75<x<200):
       fun()
    else:
        print("It is over")
fun()
print("********************")
def triangle():
    x=int(input())
    y=int(input())
    z=int(input())
    if (x+y)>z or (y+z)>x or (x+z)>y:
        print("U can form traingle")
    else:
        print("You cannot")
triangle()
