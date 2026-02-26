def tuple_names():
    names=["Diya", "Hetvi", ("Kavya",), "Veli", ("Vraj",)]
    boys=0
    girls=0
    for ele in names:
        if isinstance(ele, tuple):
            boys+=1
        else:
            girls+=1
    print("number of boys:", boys)
    print("Number of girls:", girls)
tuple_names()
