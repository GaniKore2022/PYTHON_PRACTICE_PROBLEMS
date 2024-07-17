strs=["flower","flow","flight"]
if len(strs)==0:
    print("")
else:
    prefix=strs[0]
    for i in range(1,len(strs)):
        while not strs[i].startswith(prefix):
            prefix=prefix[:-1]
            if prefix=="":
                print("")
                break
    print(prefix)
