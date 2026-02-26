def is_leap(year):
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        return True
    return False


def count_days(d, m, y):
    month_days = [31, 28, 31, 30, 31, 30, 
                  31, 31, 30, 31, 30, 31]

    total = 0
    for year in range(1, y):
        total += 366 if is_leap(year) else 365

    for month in range(1, m):
        if month == 2 and is_leap(y):
            total += 29
        else:
            total += month_days[month - 1]

    total += d

    return total
print("Enter first date:")
d1 = int(input("Day: "))
m1 = int(input("Month: "))
y1 = int(input("Year: "))

print("\nEnter second date:")
d2 = int(input("Day: "))
m2 = int(input("Month: "))
y2 = int(input("Year: "))

date1 = (d1, m1, y1)
date2 = (d2, m2, y2)

total1 = count_days(*date1)
total2 = count_days(*date2)

difference = abs(total2 - total1)

print("\nNumber of days between the two dates:", difference)
