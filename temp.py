input("Enter city name:")
x=int(input("Temperature:"))
if(x<5):
    print("Colder")
elif(5<x<15):
    print("Cold")
elif(15<x<37):
    print("MOderate")
else:
    print("Hot")
