def minion_game(string):
    # your code goes here
    substrs=[]
    for i in range(len(string)):
        for j in range(1,len(string)+1):
            substrs.append(string[i:j])
    vowels=[]
    cons=[]
    while("" in substrs):
        substrs.remove("")
    print(substrs)
    for k in substrs:
        if k[0]=='A' or k[0]=='E' or k[0]=='I' or k[0]=='O' or k[0]=='U':
            vowels.append(k)
        else:
            cons.append(k)
    if len(vowels)>len(cons):
        print("Kevin",len(vowels))
    else:
        print("Stuart",len(cons))
string = input()
minion_game(string)