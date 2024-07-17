print([(x,y) for x in [10,20,30] for y in [30,10,40] if x!=y])
print("*******************************************\n")
import functools
def add(x,y):
    return x+y
l=list(map(int,input().split()))
print(functools.reduce(add,l))
