import math
def digis_in_factorial(num):
    if num<0:
        return 0
    if num<=1:
        return 1
    digits=0
    for i in range(2,num+1):
        digits+=math.log10(i)
    return math.floor(digits)+1

print(digis_in_factorial(120))