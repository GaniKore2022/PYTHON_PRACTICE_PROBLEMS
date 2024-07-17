def magic_square(n):
    #creating the n*n matrix named magicSq
    magicSq=[]
    for i in range(n):
        k=[]
        for j in range(n):
            k.append(0)
        magicSq.append(k)
            
    #calculating the first position
    row=n//2
    col=n-1
    
    num=n*n
    count=1
    
    while(count<=num):
        if(row==-1 and col==n): #condition/step 4
            col=n-2
            row=0
        else:
            if(col==n): #if column comes at n, replace it with 0
                col=0
            if(row<0):  # if row comes at 0, replace it with n-1
                row=n-1
                
        if(magicSq[row][col]!=0): #step 3
            col=col-2
            row=row+1
            continue
        
        else:
            magicSq[row][col]=count  #insering the values
            count+=1
            
        row=row-1  #step 2( normal case)
        col=col+1
        
    #printing the Magic Square
    
    for i in range(n):
        for j in range(n):
            print(magicSq[i][j],end=" ")
        print()
n=int(input())
magic_square(n)