def leap(yr):
    if(yr%4==0):
        return True
    else:
        return False
def totdays(d, m, y):
    month=[31, 28, 31, 30, 31, 30, 31, 30, 31, 30, 31, 30]
    days=d
    for year in range(1,y):
        if leap(yr):
            days+=366
        else:
            days+=365
    for month in range (1,m):
        if month==2 and leap(yr):
            days+=29
        else:
            days+=month(month-1)
    return days
print("Enter 1st date:")
d1=int(input("Day:"))
m1=int(input("Month:"))
y1=int(input("Year:"))
print("Enter 2nd date:")
d2=int(input("Day:"))
m2=int(input("Month:"))
y2=int(input("Year:"))
days1=totdays(d1, m1, y1)
days2=totdays(d2, m2, y2)
difference=(days2-days1)
print("Number of days between two dates:", difference)
