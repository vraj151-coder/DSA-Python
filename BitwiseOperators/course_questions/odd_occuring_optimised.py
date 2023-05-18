def odd_occuring(array):
    res=0
    for i in array:
        res=res^i
    print(res)

odd_occuring([1,4,3,6,1,4,6])