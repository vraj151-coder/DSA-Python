def checkKthbit(n,k):
    return (n>>k)&1==1


print(checkKthbit(500,3))