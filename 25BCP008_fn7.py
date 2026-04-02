
def sum(lst):
    if len(lst)==0:
        return 0
    return lst[0] + sum(lst[1:])
def avg(lst):
    if len(lst)==0:
        return 0
    return sum(lst)/len(lst)
lst=list(map(int, input("Enter numbers:").split()))
print(avg(lst))
