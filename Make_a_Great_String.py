def makeGood(s):
    while(1):
        flag=0
        res=""
        for i in range(1,len(s)):
            if abs(ord(s[i-1])-ord(s[i]))==32:
                flag=1
                res=s[:i-1]+s[i+1:]
                break
        if flag==0:
            return res
        s=res
    return res
s="leeEetcode"
print("-->")
print(makeGood(s))