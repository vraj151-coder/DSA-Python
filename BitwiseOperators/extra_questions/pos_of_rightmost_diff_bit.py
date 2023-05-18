def pos_of_rightmost_diff_bit(m,n):
    max_num=max(m,n)
    pos=1
    while(max_num>0):
        if m&1!=n&1:
            return pos
        pos+=1
        m>>=1
        n>>=1
        max_num>>=1
    return -1

print(pos_of_rightmost_diff_bit(52,4))