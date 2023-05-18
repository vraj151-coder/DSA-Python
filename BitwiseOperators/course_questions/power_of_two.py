def power_of_two(num):
    if num==0:
        return False
    while(num!=1):
        if num%2==1:
            return False
        num//=2
    return True

print(power_of_two(6))