def factorial(num):
    fact=1
    for i in range(2,num+1):
        fact*=i
    return fact

print(factorial(5))