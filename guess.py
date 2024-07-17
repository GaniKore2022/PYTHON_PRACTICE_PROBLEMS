import random as r
g=r.randint(1,100)
x=int(input())
while(1):
    if(x<g):
        print("enter greater")
        x=int(input())
    elif(x>g):
        print("enter lesser")
        x=int(input())
    elif(x==g):
        print("Guessed correct")
        break

        
