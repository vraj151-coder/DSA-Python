def list_primes(num):
    all_primes=[True]*(num+1)
    idx=2
    while(idx*idx<=num):
        if all_primes[idx]:
            for j in range(idx*idx,num+1,idx):
                all_primes[j]=False
        idx+=1
    idx=2
    while(idx<len(all_primes)):
        if all_primes[idx]:
            print(idx,end=" ")
        idx+=1

list_primes(100)