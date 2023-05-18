import math
import decimal
def exactly_3_divisors(n):
    count=0
    for i in range (4,n+1):
        sqrt=math.sqrt(i)
        sqrt=decimal.Decimal(sqrt).normalize()
        print(type(sqrt))
        if isinstance(math.sqrt(i),int):
            count+=1

    return count

print(exactly_3_divisors(10))
