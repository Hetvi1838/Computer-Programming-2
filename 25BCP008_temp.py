import random
def temp():
    f_lst=[random.randint(200, 300) for x in range(5)]
    print(f_lst)
    c_lst=[(f-32)*5/9 for f in f_lst]
    print(c_lst)
temp()
