def count_digits(num):
    if num==0:
        return 0
    return 1+count_digits(num//10)