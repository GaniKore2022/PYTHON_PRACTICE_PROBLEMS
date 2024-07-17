A=list(map(int,input().split()))
x=int(input())
A.sort()
i=0
j=len(A)-1
while(i<j):
    if (A[i]+A[j]==x):
        print(A[i],A[j],"True")
        break
    elif A[i]+A[j]:
        j-=1
    else:
        i+=1