for i in range(1,10):
    print("num=",i,":",end=" ")
    for j in range(1,10):
        print("{:>3}".format(i*j),end=" ")
    print()
        