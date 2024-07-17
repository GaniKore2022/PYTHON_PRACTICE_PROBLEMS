def findcount(arr,num,diff):
    c=0
    for i in arr:
        if abs(i-num)<=diff:
            c+=1
    if c==0:
        return -1
    return c
arr=list(map(int,input().split()))
num=int(input())
diff=int(input())
print(findcount(arr,num,diff))