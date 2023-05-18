def binary_converter(num):
    res=num
    while num:
        num>>=1
        res=res^num
    return res

print(binary_converter(15))


#DONT UNDERSTAND
