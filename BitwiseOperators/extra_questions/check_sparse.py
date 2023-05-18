def check_sparse(num):
    while(num>0):
        x=num&1
        y=(num>>1)&1
        if x==1 and y==1:
            return False
        num>>=1
    return True

print(check_sparse(3))

#O(logn)