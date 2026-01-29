def multiplication():
    a=int(input("Enter a number whose table is wanted:"))
    for i in range(1, 11):
        print(f"{a} × {i} = ", a*i)
multiplication()
