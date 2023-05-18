def _2_odd_occuring(arr):
    xor=0
    for items in arr:
        xor^=items
    sb=xor&(~(xor-1))
    res1=res2=0
    for items in arr:
        if items&sb!=0:
            res1^=items
        else:
            res2^=items
    print(res1,res2)


_2_odd_occuring([3,4,5,6,4,5])
