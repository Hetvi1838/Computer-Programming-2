def ch_frq():
    str=input("Enter a string:")
    freq={}
    for ch in str:
        if ch !=" ":
            if ch in freq:
                freq[ch]+=1
            else:
                freq[ch]=1
    print("Character frequency:")
    print(freq)
ch_frq()
