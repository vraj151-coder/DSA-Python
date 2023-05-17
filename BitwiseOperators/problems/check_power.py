def check_power(num):
    
    return num!=0 and (num&(num-1)==0)

print(check_power(5))