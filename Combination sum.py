candidates=[2,3,6,7]
target=7
arr=[]
candidates.sort()
def go_back(rs,lst,first):
    if rs==0:
        arr.append(list(lst))
        return
    elif rs<0:
        return
    for i in range(first,len(candidates)):
        if rs<candidates[i]:
            break
        lst.append(candidates[i])
        go_back(rs-candidates[i],lst,i)
        lst.pop()
go_back(target,[],0)
print(arr)