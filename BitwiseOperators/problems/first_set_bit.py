def first_set_bit(num):
    pos=1
    while(num>0):
        if num&1:
            return pos
        num=num>>1
        pos+=1
    return 0

print(first_set_bit(12))