def kthBit(n,k):
    if n&(1<<(k-1))!=0:
        print("True")
    else:
        print("False")

kthBit(5,1)