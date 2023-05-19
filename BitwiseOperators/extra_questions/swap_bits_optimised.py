def swap_bits(num):
    even_mask=0xAAAAAAAA
    odd_mask=0x55555555
    even=num&even_mask
    odd=num&odd_mask
    even>>=1
    odd<<=1
    res = even | odd
    return res

print(swap_bits(23))