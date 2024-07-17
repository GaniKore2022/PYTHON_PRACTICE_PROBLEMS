message=input()
index=0
while index<len(message):
    letter=message[index]
    print(chr(ord(letter)+1),end="")
    index+=1
