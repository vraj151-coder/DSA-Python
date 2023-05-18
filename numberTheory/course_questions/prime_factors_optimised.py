def prime_factors(num):
    i=2
    while(i*i<=num):
        while(num%i==0):
            print(i)
            num//=i
        i+=1
    if num>1:
        print(num)

prime_factors(12)