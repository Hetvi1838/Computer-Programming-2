def stud_data():
    stud=[(48, "Diya", 18), (8, "Hetvi", 17), (27, "Kavya", 18), (31, "Veli", 17), (1, "Vraj", 17)]
    roll=[]
    name=[]
    age=[]
    for i in stud:
        roll.append(i[0])
        name.append(i[1])
        age.append(i[2])
    print(roll)
    print(name)
    print(age)
stud_data()
        
