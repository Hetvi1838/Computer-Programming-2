def prime(n, divisor=2):
    if n==1:
        return []
    if n%divisor==0:
        return [divisor]+prime(n//divisor, divisor)
    else:
        return(prime(n,divisor+1))
f=prime(48)
print(f)
