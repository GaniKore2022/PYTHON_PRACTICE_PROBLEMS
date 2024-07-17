class number:
    even=[]
    odd=[]
    def __init__(self,num):
        self.num=num
        if num%2==0:
            number.even.append(num)
        else:
            number.odd.append(num)
n1=number(21)
n2=number(32)
n3=number(43)
n4=number(54)
n5=number(65)
print("Even no.s are:",number.even)
print("Odd no.s are:",number.odd)
