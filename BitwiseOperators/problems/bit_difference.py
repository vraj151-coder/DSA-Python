def bit_difference(a,b):
    max_num=max(a,b)
    diff_bits=0
    while max_num>0:
        if a&1!=b&1:
            diff_bits+=1
        a>>=1
        b>>=1
        max_num>>=1
    return diff_bits
    
print(bit_difference(10,20))