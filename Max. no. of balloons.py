def balloon(text):
    x={}
    target="balon"
    for i in text:
        if i in target:
            if i not in x:
                x[i]=1
            else:
                x[i]+=1
    x['l']=x['l']//2
    x['o']=x['o']//2
    string=""
    for i in x.keys():
        string+=i
    if sorted(string)==sorted(target):
        return min(x.values())
    else:
        return 0
text="nlaebolko"
print(balloon(text))