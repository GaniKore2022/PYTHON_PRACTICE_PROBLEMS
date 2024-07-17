string=input()
s=string.replace(" ","")
if s==s[::-1]:
    print("Valid")
else:
    print("Not valid")
