def binary_converter(num):
    if num==0:
        return
    binary_converter(num//2)
    print(num%2,end="")

binary_converter(8)


