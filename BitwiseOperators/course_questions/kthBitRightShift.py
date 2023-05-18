def kthBit(n,k):
    if (n>>(k-1))&1==1:
        print("True")
    else:
        print("False")

kthBit(5,1)