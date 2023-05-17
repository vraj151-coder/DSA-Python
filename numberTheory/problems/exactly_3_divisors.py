def exactly_3_divisors(n):
    divisors_3=0
    for i in range (4,n+1):
        count=0
        j=1
        while(j*j<=i):
            if i%j==0:
                if i//j==j:
                    count+=1
                else:
                    count+=2
            j+=1
        if count==3:
            divisors_3+=1
    return divisors_3

print(exactly_3_divisors(6))