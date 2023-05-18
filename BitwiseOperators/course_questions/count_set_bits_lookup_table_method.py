def initialize():
    table=[0]*256
    for i in range(1,256):
        table[i]=(i&1)+table[i//2]
    return table

def count_set_bits(num):
    table=initialize()
    count=table[num&0xff]
    num=num>>8
    count+=table[num&0xff]
    num=num>>8
    count+=table[num&0xff]
    num=num>>8
    count+=table[num&0xff]
    return count

print(count_set_bits(13))