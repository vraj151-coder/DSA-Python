def sum_of_digits(num):
    if num <= 9:
        return num
    return num % 10+sum_of_digits(num//10)


print(sum_of_digits(58))
