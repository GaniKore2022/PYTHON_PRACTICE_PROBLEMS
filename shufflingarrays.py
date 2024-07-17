n1=list(map(int,input().split()))
n2=list(map(int,input().split()))
n3=[]
if len(n1)==len(n2):
    for i in range(len(n1)):
        n3.append(n1[i])
        n3.append(n2[i])
    print(n3)
else:
    print("Enter two arrays with same size only")
    
    
