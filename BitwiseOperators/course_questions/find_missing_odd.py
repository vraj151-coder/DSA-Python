def find_missing_odd(list1):
    max_num=max(list1)
    res=0
    for i in range(max_num+1):
        res=res^i
    for i in list1:
        res=res^i
    return res

print(find_missing_odd([1,5,3,2]))