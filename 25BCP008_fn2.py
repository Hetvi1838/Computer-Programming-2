def bin(n):
    if n==0:
        return ""
    return bin(n//2)+str(n%2)
num= int(input("Enter a positive number:"))
print("Binary :", bin(num) or "0")
