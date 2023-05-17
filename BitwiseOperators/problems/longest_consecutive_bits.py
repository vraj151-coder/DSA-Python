def longest_consecutive_bits(num):
    cnt=0
    max_cnt=0
    while(num):
        if num&1==1:
            cnt+=1
            if cnt>max_cnt:
                max_cnt=cnt
        else:
            cnt=0
        num>>=1
    return max_cnt

print(longest_consecutive_bits(10))