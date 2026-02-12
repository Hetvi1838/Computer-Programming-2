import random
def dup():
    lst=[random.randint(1, 20) for x in range(50)]
    print("List:", lst)
    new_lst=[]
    for i in lst:
        if i not in new_lst:
            new_lst.append(i)
print("Unique list is:", new_lst)
dup()
    
