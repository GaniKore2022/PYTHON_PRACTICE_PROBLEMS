def valid_pw(s,n):
    if n<4 or "0"<=s[0]<="9":
        return 0
    extra=[" ","/"]
    d=u=0
    for i in s:
        if i in extra:
            return 0
        elif "0"<=i<="9":
            d+=1
        elif "A"<=i<="Z":
            u+=1
    if u==0 or d==0:
        return 0
    else:
        return 1
n=int(input())
s=input()
print(valid_pw(s,n))