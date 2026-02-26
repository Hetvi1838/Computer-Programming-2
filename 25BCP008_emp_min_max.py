def empl():
    emp={1:[(1, 10), (48, 20), (8, 200)], 2:[(2, 30), (4, 90)]}
    for dept in emp:
        salaries=[]
        for e in emp[dept]:
            salaries.append(e[1])
        print("Department:", dept)
        print("Minimum Salary:", min(salaries))
        print("Maximum salary:", max(salaries))
        
empl()
            
