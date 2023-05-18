def prime_list(num):
    primes=[True]*(num+1)
    all_primes=[]
    idx=2
    while(idx*idx<=num):
        if primes[idx]:
            for i in range(idx*idx,num+1,idx):
                primes[i]=False
        idx+=1
    idx=2
    while(idx<len(primes)):
        if primes[idx]==True:
            all_primes.append(idx)
        idx+=1
    return all_primes

def prime_factors(n):
    primes=prime_list(n)
    idx=0
    while(idx<len(primes)):
        if n%primes[idx]==0:
            print(primes[idx])
            n//=primes[idx]
            if n==1:
                break
            idx=0
        else:
            idx+=1

prime_factors(315)