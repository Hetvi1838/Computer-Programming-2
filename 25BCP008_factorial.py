def factorial():
    a=int(input("Enter a number:"))
    b=1
    i=1
    for i in range(1, a+1):
        b*=i
        i+=1
    print(b)
factorial()
        
