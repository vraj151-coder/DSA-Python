def num_with_bit_sets(pattern,arr):
    count=0
    for items in arr:
        if ((pattern&items)==pattern):
            count+=1
    return count

def max_and(arr):
    res=0
    for i in range(31,-1,-1):
        cnt=num_with_bit_sets(res|1<<i,arr)
        if cnt>1:
            res=res|(1<<i)
    return res

print(max_and([4,8,12,16]))
