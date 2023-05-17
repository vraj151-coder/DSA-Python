import time
def is_prime(num):
    if num==1:
        return False
    i=2
    while(i*i<=num):
        if num%i==0:
            return False
        i+=1
    return True

start=time.time()
print(is_prime(1000001))
stop=time.time()
print(f"{(stop-start)*10**3}")