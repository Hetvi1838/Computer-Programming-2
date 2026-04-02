def rev(lst):
    if len(lst)==0:
        return []
    return rev(lst[1:])+[lst[0]]
num=list(map(int, input("Enter numbers seperated by spaces:").split()))
print(rev(num))
