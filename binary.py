n=list(map(str,input("Enter a string: ").split(",")))
for i in n:
    k=0
    for j in range(len(i)):
        k=k+int(i[j])*(2^len(i)-1)
    if(k%5==0):
        print(k,end=" ")
