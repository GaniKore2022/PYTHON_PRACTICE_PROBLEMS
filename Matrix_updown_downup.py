def printmatrix(matrix):
    rows=len(matrix)
    cols=len(matrix[0])
    arr=[]
    i=rows-1
    j=cols-1
    while(1):
        arr,i,j=updown(arr,matrix,i,j)
        j-=1
        if i==rows-1 and j==0:
            break
        arr,i,j=downup(arr,matrix,i,j)
        j-=1
        if i==0 and j==0:
            break
    return arr
def updown(arr,matrix,i,j):
    for k in range(i,-1,-1):
        arr.append(matrix[k][j])
    return arr,k+1,j
def downup(arr,matrix,i,j):
    for k in range(i):
        arr.append(matrix[k][j])
    return arr,k,j
matrix=[[1,2,3,4],
        [5,6,7,8],
        [9,10,11,12]]     #[12,8,4,3,7,11,10,6,2,1,5,9]
res=printmatrix(matrix)
print(res)