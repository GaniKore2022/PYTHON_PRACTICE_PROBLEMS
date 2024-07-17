# def anagrams(words):
#     anag={}
#     for word in words:
#         sortedword="".join(sorted(word))
#         if sortedword in anag:
#             anag[sortedword].append(word)
#         else:
#             anag[sortedword]=[word]
#     result=list(anag.values())
#     return result
# words=list(map(str,input().split()))
# print(anagrams(words))
s1=input()
s2=input()
if len(s1)!=len(s2):
    print("Not Anagrams")
else:
    d={}
    for i in s1:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    for i in s2:
        if i in d:
            d[i]-=1
            if d[i]==0:
                del d[i]
    if len(d)==0:
        print("Anagrams")
    else:
        print("Not Anagrams")