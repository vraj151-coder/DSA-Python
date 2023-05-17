import time

def is_prime(num):
    if num==1:
        return False
    for i in range(2,num):
        if num%i==0:
            return False
    return True

start=time.time()
print(is_prime(104729))
stop=time.time()
print(f"{(stop-start)*10**3}")