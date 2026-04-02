def zero(lst):
    if len(lst)==0:
        return[]
    first=0 if lst[0]<0 else lst[0]
    return [first] + zero(lst[1:])
num=list(map(int, input("Enter numbers with spaces:").split()))
print(zero(num))
