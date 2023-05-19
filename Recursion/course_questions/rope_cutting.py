def rope_cut(n, a, b, c):
    if n < 0:
        return -1
    if n == 0:
        return 0

    res = max(rope_cut(n-a, a, b, c), rope_cut(n -
              b, a, b, c), rope_cut(n-c, a, b, c))
    if res == -1:
        return -1
    return res+1


print(rope_cut(5, 4, 2, 6))
