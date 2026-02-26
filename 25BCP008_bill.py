def grocery():
    price={"Biscuit":20, "Milk":30, "Wheat": 150}
    quantity={"Biscuit":4, "Milk":3, "Wheat":1}
    tot=0
    for item in quantity:
        if item in price:
            tot+=price[item]*quantity[item]
    print("Total Bill=", tot)

grocery()
