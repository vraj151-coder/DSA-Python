def power_of_number(n,r):
    if r==1:
        return n
    mod=pow(10,9)+7
    power=1
    power=(n%mod*power_of_number(n,r-1)%mod)%mod
    return power

print(power_of_number(12,21))