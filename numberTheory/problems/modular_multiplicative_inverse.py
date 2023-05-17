def modular_multiplicative_inverse(a,m):
    for i in range(1,m):
        if ((a%m)*(i%m))%m==1:
            return i
        elif i==m-1:
            return -1
    
print(modular_multiplicative_inverse(10,17))