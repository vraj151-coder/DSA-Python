def all_divisors(num):
    divisors=[]
    i=1
    while(i*i<=num):
        if num%i==0:
            divisors.append(i)
        i+=1
    while(i>=1):
        if num%i==0:
            divisors.append(num//i)
        i-=1
    return divisors

print(all_divisors(15))