def swap():
    a=int(input("Enter a number:"))
    b=int(input("Enter a number:"))
    a=a+b
    b=a-b
    a=a-b
    print("The swapped values are", a, b)
swap()
