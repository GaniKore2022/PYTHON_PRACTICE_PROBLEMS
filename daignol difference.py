arr=[[2,3,4,3,9],[5,6,7,4,2],[1,2,3,5,6],[2,5,8,6,2],[2,6,9,0,3]]
s1=0
s2=0
n=len(arr)
for i in range(n):
    s1 += arr[i][i]
    for j in range(n):
        if i+j==n-1:
            s2+=arr[i][j]
print(abs(s1-s2))