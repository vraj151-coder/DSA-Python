def count_set_bits(num):
    count=0
    while(num!=0):
        count+=num&1
        num=num>>1
    return count

print(count_set_bits(13))