def count():
    a=input("Enter a string:")
    alphabets=0
    numbers=0
    for ch in a:
        if ch.isalpha():
            alphabets+=1
        elif ch.isdigit():
            numbers+=1
    print(f"The count of digits: {numbers}\nThe count of alphabets: {alphabets}")
count()
