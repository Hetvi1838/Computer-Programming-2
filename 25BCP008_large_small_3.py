def larg_small_3():
    a=int(input("Enter a number:"))
    b=int(input("Enter another number:"))
    c=int(input("Enter one more number:"))
    if(a>b and a>c):
        print(f"The largest number is {a}.")
        if(b>c):
            print(f"The smallest number is {c}")
        else:
            print(f"The smallest number is {b}")
    elif(b>a and b>c):
        print(f"The largest number is {b}.")
        if(a>c):
            print(f"The smallest number is {c}")
        else:
            print(f"The smallest number is {a}")
    else:
        print(f"The greatest number is {c}.")
        if(a>b):
            print(f"The smallest number is {b}")
        else:
            print(f"The smallest number is {a}")

larg_small_3()
