import math
def factorial_trailing_zeros(num):
    i=5
    trailing_zeros=0
    while(i<=num):
        trailing_zeros+=num//i
        i*=5
    return trailing_zeros

print(factorial_trailing_zeros(100))