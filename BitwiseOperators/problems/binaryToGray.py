def grayConverter(num):
    return num^(num>>1)

print(grayConverter(10))