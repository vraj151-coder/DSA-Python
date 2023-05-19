def print_number(num):
    if num == 0:
        return
    print_number(num-1)
    print(num-1, end=" ")


print_number(5)
