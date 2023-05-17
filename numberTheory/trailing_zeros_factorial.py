def factorial(num):
    fact=1
    for i in range(2,num+1):
        fact*=i
    return fact

def trailing_zeros(num):
    fact_val=factorial(num)
    count=0
    while(fact_val%10==0):
        count+=1
        fact_val//=10
    return count

print(trailing_zeros(100))