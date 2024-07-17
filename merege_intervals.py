lst1=[[1,3],[2,6],[8,10],[15,18]]
i=0
l=[]
while(i<len(lst1)-1):
    j=i+1
    while(j<len(lst1)):
        if lst1[j][0] in range(lst1[i][0],lst1[i][1]):
            l.append([lst1[i][0],lst1[j][1]])
        else:
            if lst1[j] not in l:
                l.append(lst1[j])
            break            
        j+=1
    i+=1
print(l)