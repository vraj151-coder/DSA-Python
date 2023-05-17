def all_divisors(num):
    divisors=[]
    i=1
    while(i*i<=num):
        if num%i==0:
            divisors.append(i)
            if i!=num/i:
                divisors.append(num//i)
        i+=1
    divisors.sort()
    return divisors

print(all_divisors(15))