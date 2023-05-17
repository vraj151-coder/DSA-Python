def power(n,pow):
    if pow==0:
        return 1
    temp=power(n,pow//2)
    if pow%2==0:
        return temp*temp
    return n*temp*temp

def gp_term(a,b,n):
    r=b/a
    return a*(power(r,n-1))

print(gp_term(2,3,2))