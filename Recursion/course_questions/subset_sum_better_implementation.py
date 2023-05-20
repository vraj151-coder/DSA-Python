def subset_sum(arr, n, sum):
    if n == 0:
        if sum == 0:
            return 1
        return 0
    return subset_sum(arr, n-1, sum)+subset_sum(arr, n-1, sum-arr[n-1])


arr = [2, 6, 8, 10]
print(subset_sum(arr, len(arr), 8))
