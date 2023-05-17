import time

def is_prime(num):
    if num==1:
        return False
    if num>3:
        if num%2==0 or num%3==0:
            return False
    i=5
    while (i*i<=num):
        if num%i==0:
            return False
        i+=1
    return True

start=time.time()
print(is_prime(104729))
stop=time.time()
print(f"{(stop-start)*10**3}")