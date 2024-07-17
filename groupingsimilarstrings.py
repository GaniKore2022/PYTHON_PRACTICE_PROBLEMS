def similarstrings(string):
    dic={}
    s=string.split()
    for i in s:
        if i not in dic:
            dic[i]=1
        else:
            dic[i]+=1
    return dic
string=input()
x=similarstrings(string)
print(x)
