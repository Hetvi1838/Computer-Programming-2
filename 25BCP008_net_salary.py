def net_salary():
    gs=int(input("Enter your gross salary:"))
    a=gs*0.1
    d=gs*0.03
    net=gs+a-d
    print("The net salary is: ", net)
net_salary()
