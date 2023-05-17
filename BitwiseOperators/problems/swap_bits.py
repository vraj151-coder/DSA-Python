def swap_bits(num):
    new=""
    while num:
        odd_bit=num&1
        even_bit=(num>>1)&1
        new+=str(even_bit)
        new+=str(odd_bit)
        num=num>>2
    new=new[::-1]
    res=0
    for i in range(len(new)-1,-1,-1):
        res+=(int(new[i]))*(2**(len(new)-1-i))
    return res

print(swap_bits(2))
