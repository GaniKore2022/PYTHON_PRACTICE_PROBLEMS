def bop(s):
    if not s:
        return -1
    a=s[0]
    for i in range(1,len(s)-1,2):
        if i=="A":
            a=a & s[i+1]
        elif i=="B":
            a=a | s[i+1]
        elif i=="C":
            a=a^s[i+1]
    return a
s=input()
print(bop(s))