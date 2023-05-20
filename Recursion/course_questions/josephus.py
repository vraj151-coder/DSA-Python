def josephus(n, k):
    if n == 1:
        return 0
    killed_person = 0+k-1
    x = josephus(n-1, k)
    if x > killed_person:
        return x+1
    return x
