def food():
    item=[("Pasta", 400), ("Sandwich", 200), ("Pizza", 700), ("Sizzler", 1000)]
    n=len(item)
    for i in range(n):
        for j in range(0, n-i-1):
            if item[j][1]<item[j+1][1]:
                item[j], item[j+1]= item[j+1], item[j]
    print("Sorted list:")
    for n in item:
        print(n)
food()
