def list_primes(num):
    primes=[True]*(num+1)
    idx=2
    while(idx*idx<=num):
        for i in range(idx*2,num+1,idx):
            primes[i]=False
        idx+=1
    idx=2
    while(idx<len(primes)):
        if primes[idx]==True:
            print(idx,end=" ")
        idx+=1

list_primes(100)
