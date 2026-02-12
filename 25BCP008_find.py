import random
def q2_lst():
    lst=[random.randint(1, 20) for x in range(20)]
    print(lst)
    n=int(input("Enter a number:"))
    if lst.count(n)>1:
        for (i, v) in enumerate(lst):
             if v==n:
                  print(i)
    else:
        print(n," is not found")
q2_lst()
