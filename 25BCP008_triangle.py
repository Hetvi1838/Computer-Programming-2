def triangle():
    a=int(input("Enter first angle of the triangle:"))
    b=int(input("Enter second angle of the triangle:"))
    c=int(input("Enter third angle of the triangle:"))
    if(a+b+c==180):
        print("The triangle is valid.")
    else:
        print("The triangle is not valid.")
triangle()
