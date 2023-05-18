def addition_under_modulo(a,b):
    M=10**9+7
    a=a%M
    b=b%M
    sum=(a+b)%M
    return sum

print(addition_under_modulo(9223372036854775807,9223372036854775807))