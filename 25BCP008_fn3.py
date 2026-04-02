def vow(str):
    if len(str)==0:
        return 0
    first=str[0].lower()
    count=1 if first in "aeiou" else 0
    return count + vow(str[1:])
str=input("Enter a string:")
print("The number of vowels in the string are:", vow(str)) 
