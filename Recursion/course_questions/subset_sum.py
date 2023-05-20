def subset_sum(arr, ans, curr="", i=0):
    if i == len(arr):
        return 0
    if ans == 0:
        return 0
    sum = 0
    for items in curr:
        sum += int(items)
    if sum == ans:
        return 1
    x = subset_sum(arr, ans, curr, i+1)
    y = subset_sum(arr, ans, curr+str(arr[i]), i+1)
    return x+y


print(subset_sum([10, 20, 15], 8))
