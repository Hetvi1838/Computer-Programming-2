def merge():
    d1={"C101":2000,"C102":3000, "C103":4000}
    d2={"C101":3000, "C104":2000, "C105":1000}
    merged={}
    for n in d1:
        merged[n]=d1[n]
    for n in d2:
        if n in merged:
            merged[n]+=d2[n]
        else:
            merged[n]=d2[n]
    print("Merged Dictionary:")
    print(merged)
    max_=max(merged.values())
    print("\nProduct with highest sale:")
    for n in merged:
        if merged[n]==max_:
            print(n, "->", max_)
    sorted={}
    while merged:
        max_key=""
        max_value=0
        for n in merged:
            if merged[n]>max_value:
                max_value=merged[n]
                max_key=n
        sorted[max_key]=max_value
        del merged[max_key]
    print(sorted)
merge()
