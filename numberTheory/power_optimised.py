def power(num,pow):
    if pow==0:
        return 1
    temp=power(num,pow//2)
    temp=temp*temp
    if pow%2==0:
        return temp
    return num*temp

print(power(2,5))