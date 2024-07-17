#write a program that has a class circle use the class variable to define the constant pie use the class variable to calculate area and circumference in different function with the specific radius 7.5?
class circle():
    pi=3.14159
    def __init__(self,r):
        self.r=r
    def area(self):
        return circle.pi*self.r*self.r
    def circumference(self):
        return 2*circle.pi*self.r
n=circle(7.5)
print(n.area())
print(n.circumference())
