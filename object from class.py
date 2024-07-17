class abc():
    var=10
    def dis(self):
        print('This is in class')
        v=100
obj=abc()
print(obj.var)
obj.dis()
#__init__ method is called constructor
class abc():
    def __init__ (self,val):
        self.val=val
        print("The val is",val)
obj=abc(1)
