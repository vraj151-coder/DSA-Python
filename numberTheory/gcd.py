def gcd(num1,num2):
    min_num=min(num1,num2)
    for i in range(num1,0,-1):
        if num1%i==0 and num2%i==0:
            return i

print(gcd(2,3))