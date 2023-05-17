def longest_consecutive_bits(num):
    count=0
    while(num):
        num=num&(num>>1)
        count+=1
    return count

print(longest_consecutive_bits(222))