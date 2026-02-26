def str_frq():
    str=input("Enter a string:")
    words=str.split()
    freq={}
    for word in words:
        if word in freq:
            freq[word]+=1
        else:
            freq[word]=1
    print(freq)
    max_=max(freq.values())
    print("Most frequent words:")
    for word in freq:
        if freq[word]==max_:
            print(word)
str_frq()
