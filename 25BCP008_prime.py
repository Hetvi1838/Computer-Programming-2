def prime():
    a=int(input("Enter a number:"))
    Prime=True
    for i in range(2, a//2):
        if a%i==0:
           Prime=False
           break
    print(Prime)
prime()
