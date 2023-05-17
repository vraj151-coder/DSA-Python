def power(num,pow):
    res=1
    for i in range(pow):
        res*=num
    return res

print(power(2,5))