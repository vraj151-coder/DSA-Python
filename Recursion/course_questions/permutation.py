def permutation(str, curr="", n=0):
    if n == len(str):
        for items in curr:
            if curr.count(items) > 1:
                return
        print(curr)
        return
    for i in range(len(str)):
        permutation(str, curr+str[i], n+1)


permutation("ABC")
