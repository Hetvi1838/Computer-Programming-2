def empty():
    list=[(2, 50), (), (3, 2), (), (), (9, 9)]
    list=[i for i in list if i!=()]
    print("List after removing empty tuple:", list)
empty()
