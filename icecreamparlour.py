t=int(input())
for k in range(t):
    m=int(input())
    n=int(input())
    cost=list(map(int,input().split()))
    for i in range(0,len(cost)-1):
        for j in range(i+1,len(cost)):
            if cost[i]+cost[j]==m:
                print(i+1,j+1)
                break
            else:
                continue