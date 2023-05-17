def check_sparse(num):
    return num&(num>>1)==0

print(check_sparse(3))

#O(1)