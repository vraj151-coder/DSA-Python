def digital_root(num):
    sum=0
    while num:
        sum+=num%10
        num//=10
    if sum<10:
        return sum
    return digital_root(sum)

print(digital_root(99999))